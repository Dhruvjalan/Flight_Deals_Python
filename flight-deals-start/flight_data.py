import requests
from pprint import pprint
from datetime import datetime
from datetime import datetime, timedelta


class FlightData:
    #This class is responsible for structuring the flight data.
    def __init__(self):
        self.city_code_list = None
        self.further_date = None
        self.body = ""
        self.EP = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        self.FLIGHT_APPNAME = "FlightDeal_d39-40"
        self.FLIGHT_APIKEY = "1RWd57QpF2GBsHTZltJxxADfisZrcAxk"
        self.FLIGHT_APISECRET = "XI4jGRE3Wb7J63G0"
        self.credentials = "Dhruv Jalan"
        self.headers = {}
        self.access_token = ""
        self.bprice = {}

    def getdata(self, citycode):

        for n in range(1, 61):
            self.further_date = datetime.today().date() + timedelta(days=n)
            self.body = {
                "currencyCode": "GBP",
                "originDestinations": [
                    {
                        "id": "1",
                        "originLocationCode": "LON",
                        "destinationLocationCode": f"{citycode}",
                        "departureDateTimeRange": {
                            "date": self.further_date,
                            "time": "10:00:00"
                        }
                    }
                ],
                "travelers": [
                    {
                        "id": "1",
                        "travelerType": "ADULT"
                    }
                ],
                "sources": [
                    "GDS"
                ],
                "searchCriteria": {
                    "flightFilters": {
                        "cabinRestrictions": [
                            {
                                "cabin": "ECONOMY",
                                "coverage": "MOST_SEGMENTS",
                                "originDestinationIds": [
                                    "1"
                                ]
                            }
                        ]
                    }
                }
            }
            response = requests.post(url=self.EP, json=self.body, headers=self.headers)
            pprint(response.json()['data'][0]['price']['base_price'])

    def get_access_token(self):
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
            self.access_token = response.json()['access_token']
            self.headers = {
                "Authorization": f"Bearer {self.access_token}"
            }

        else:
            print("NOT GOOD")
            raise Exception(f"Error: {response.status_code}, {response.text}")

    def find_cheapest_flight(self, code_list):

        self.city_code_list = code_list
        for city_code in self.city_code_list:
            self.getdata(city_code)

        pass
