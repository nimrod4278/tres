import argparse
from services.graph import Graph
from clients.mongo import MongoClient
from util.const import GRAPH_DB_NAME, NODES_COLLECTION_NAME, EDGES_COLLECTION_NAME
import json

allowed_dbs = [GRAPH_DB_NAME]
allowed_collections = [NODES_COLLECTION_NAME, EDGES_COLLECTION_NAME]


def quey_input_validity(args):
    res = True
    if args.db not in allowed_dbs:
        print(f"DB name entered is not allowed. Please choose one of {allowed_dbs}")
        res = False
    if args.collection not in allowed_collections:
        print(f"Collection name entered is not allowed. Please choose one of {allowed_collections}")
        res = False
    return res

def main():
    parser = argparse.ArgumentParser(description='Traverse transaction graph')
    parser.add_argument('--action', help="select query/traverse", default="traverse")
    parser.add_argument('--db', help="what kind of query - default to find", default=GRAPH_DB_NAME)
    parser.add_argument('--collection', help="what kind of query - default to find", default=NODES_COLLECTION_NAME)
    parser.add_argument('--filter', help="what filter to use", default="{}")
    parser.add_argument('--address', help='the address you need to traverse')
    parser.add_argument('--depth', help='the depth of traversal', default=3)
    args = parser.parse_args()

    if args.action == "query":
        try:
            if quey_input_validity(args=args):
                mongo = MongoClient()
                filter_json = json.loads(args.filter)
                res = mongo.find(db_name=args.db, collection_name=args.collection, query=filter_json)
                print(list(res))
        except Exception as e:
            print(f"Filtered entered is not in json format: \n{args.filter}")
    elif args.action == "traverse":
        g = Graph()
        graph = g.get_graph(address=args.address, max_depth=args.depth)
        print(list(graph))
    else:
        print(f"Unalloowed action chosen - {args.action}- please select one the following [query, traverse]")



if __name__ == "__main__":
    main()