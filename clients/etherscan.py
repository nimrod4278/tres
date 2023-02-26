import os
import requests
from util.const import DEFAULT_ADDRESS, ETHERSCAN_DEFAULT_OFFSET, MAX_PAGES_TO_FETCH
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get('ETHERSCAN_API_KEY')

class EtherscanClient():
    def __init__(self) -> None:
        pass

    def get_tx_page(self, page, address, offset=ETHERSCAN_DEFAULT_OFFSET):
        response = {}
        try:
            req_url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&startblock=0&endblock=99999999&page={page}&offset={offset}&sort=asc&apikey={API_KEY}"
            print(req_url)
            response = requests.get(req_url)
            response = response.json()
            response = response["result"]
        except Exception as e:
            print(e)
        return response
    
    def get_all_tx_pages(self, address, offset=ETHERSCAN_DEFAULT_OFFSET):
        response = []
        page_response = []
        page = 1

        try:
            while (len(response) == offset or page == 1) and page <= MAX_PAGES_TO_FETCH:
                page_response = self.get_tx_page(page=page, address=address, offset=offset)
                response += page_response
                page += 1
        except Exception as e:
            print(e)
        
        return response

if __name__ == "__main__":
    etherscan = EtherscanClient()
    response = etherscan.get_all_tx_pages(address=DEFAULT_ADDRESS)
    print(response)