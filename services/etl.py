from clients.etherscan import EtherscanClient
from clients.mongo import MongoClient
from util.const import DEFAULT_ADDRESS, ETHERSCAN_DEFAULT_OFFSET, GRAPH_DB_NAME, EDGES_COLLECTION_NAME


class ETL:
    def __init__(self) -> None:
        self.etherscan = EtherscanClient()
        self.mongo = MongoClient()

    def extract(self, address=DEFAULT_ADDRESS, offset=ETHERSCAN_DEFAULT_OFFSET):
        return self.etherscan.get_all_tx_pages(address=address, offset=offset)

    def load(self, transaction_list):
        self.mongo.insert_many(db_name=GRAPH_DB_NAME, collection_name=EDGES_COLLECTION_NAME, docs=transaction_list)

    def start(self, address=DEFAULT_ADDRESS, offset=ETHERSCAN_DEFAULT_OFFSET):
        transaction_list = self.extract(address=address, offset=offset)
        self.load(transaction_list=transaction_list)


if __name__ == "__main__":
    etl = ETL()
    etl.start()
