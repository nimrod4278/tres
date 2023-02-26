from services.graph import Graph
from util.const import DEFAULT_ADDRESS

if __name__ == "__main__":
    g = Graph()
    g.traverse_and_fetch(DEFAULT_ADDRESS)