import requests
from pprint import pprint


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self):
        self.iata_list = []
        self.header = None
        self.IATA_EP = None
        self.param = None
        self.FLIGHT_APPNAME = "FlightDeal_d39-40"
        self.FLIGHT_APIKEY = "1RWd57QpF2GBsHTZltJxxADfisZrcAxk"
        self.FLIGHT_APISECRET = "XI4jGRE3Wb7J63G0"

    def get_iata(self, access_token, city_list):

        self.header = {
            "Authorization": f"Bearer {access_token}"
        }

        for city in city_list:
            self.IATA_EP = f"https://test.api.amadeus.com/v1/reference-data/locations?subType=CITY&keyword={city}"
            response = requests.get(url=self.IATA_EP, headers=self.header)
            self.iata_list.append(response.json()['data'][0]['iataCode'])

    def get_access_token(self, city_list):
        url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'client_credentials',
            'client_id': self.FLIGHT_APIKEY,
            'client_secret': self.FLIGHT_APISECRET
        }

        response = requests.post(url, headers=headers, data=data)
        if response.status_code == 200:
            print("GOOD")
            print(response.json()['access_token'])
            self.get_iata(response.json()['access_token'], city_list)
        else:
            print("NOT GOOD")
            raise Exception(f"Error: {response.status_code}, {response.text}")
