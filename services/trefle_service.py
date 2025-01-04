import requests
import os

class TrefleService:
    def __init__(self):
        api_url = os.environ.get("TrefleApiURL")
        api_key = os.environ.get("TrefleApiKey")
        if api_url is None:
            print("Could not retrieve Trefle API URL")
        if api_key is None:
            print("Could not retrieve Trefle API key")
        
        self.url = api_url.strip('\n')
        self.key = api_key.strip('\n')
        self.default_params = { "token": self.key }
    
    def get_url(self, route: str):
        return f'{self.url}{route}'
        
    async def get_plants(self):
        URL = self.get_url('plants')
        print(URL)
        response = requests.get(url=URL, params=self.default_params)
        data = response.json()
        return data
    