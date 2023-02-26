from clients.mongo import MongoClient
from services.etl import ETL
from util.const import DEFAULT_ADDRESS, DEFAULT_MAX_DEPTH, GRAPH_DB_NAME, NODES_COLLECTION_NAME

class Graph():
    def __init__(self) -> None:
        self.mongo = MongoClient()
        self.etl = ETL()

    def get_graph(self, address=DEFAULT_ADDRESS, max_depth=DEFAULT_MAX_DEPTH):
        addresses_collection = self.mongo.get_collection("graph", "addresses")
        res = addresses_collection.aggregate([
                {
                    "$match": {
                        "address": address
                    }
                },
                {
                    "$graphLookup": {
                        "from": "transactions",
                        "startWith": "$address",
                        "connectFromField": "to",
                        "connectToField": "from",
                        "maxDepth": max_depth,
                        "as": "transactedWith",
                        "depthField": "depth",
                    },

                },
                {
                    "$unwind": "$transactedWith"
                },
                {
                    "$group": {
                        "_id": {
                            "$setUnion": [
                                [
                                    "$transactedWith.from"
                                ],
                                [
                                    "$transactedWith.to"
                                ]
                            ]
                        },
                        "volume": {
                            "$sum": 1
                        },
                        "depth": {
                            "$min": "$transactedWith.depth"
                        }
                    }
                },
                {
                    "$sort": {
                        "depth": 1,
                        "volume": -1
                    }
                }
            ]
        )

        return res
    
    def traverse_and_fetch(self, address=DEFAULT_ADDRESS, max_depth=DEFAULT_MAX_DEPTH):
        children_per_node = 10
        queue = [address]
        visited = []

        while len(queue) > 0 and len(visited) < 1000:
            print(len(visited))
            current = queue.pop(0)
            self.mongo.insert_one(db_name=GRAPH_DB_NAME, collection_name=NODES_COLLECTION_NAME, doc={"address": current})
            visited.append(current)
            self.etl.start(address=current)
            g = list(self.get_graph(address=current, max_depth=0))
            
            if len(g) > children_per_node:
                g = g[:children_per_node]
            
            for edge in g:
                if len(edge["_id"]) == 2:
                    neighboor = edge["_id"][0] if edge["_id"][0] not in visited else edge["_id"][1]
                else:
                    neighboor = edge["_id"][0]

                if neighboor not in visited:
                    queue.append(neighboor)