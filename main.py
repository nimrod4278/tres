from services.etl import ETL
from services.graph import Graph
from util.const import DEFAULT_ADDRESS
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    g = Graph()
    g.traverse_and_fetch(DEFAULT_ADDRESS)