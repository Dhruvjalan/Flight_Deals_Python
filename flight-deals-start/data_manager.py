import requests
from pprint import pprint


class DataManager:
    def __init__(self):
        self.response = None
        self.SHEETY_USN = "Dhruv Jalan"
        self.SHEETY_PROJNAME = "Python d38_My Workouts"
        self.SHEETY_SHEETNAME = "prices"
        self.SHEETY_PUT_EP=""
        self.put_headers={}
        self.new_data={}
        self.SHEET_NAME = "prices"
        self.SHEETY_EP = "https://api.sheety.co/852527fb5a33178507bc563cf260bba5/pythonD38MyWorkouts/workouts"
        self.SHEETY_EP2 = f"https://api.sheety.co/{self.SHEETY_USN}/{self.SHEETY_PROJNAME}/{self.SHEETY_PROJNAME}"
        self.SHEETY_GET_EP = "https://api.sheety.co/852527fb5a33178507bc563cf260bba5/flightDealsD39/prices"
        self.SHEETY_TOKEN = "sheety_token_DHRUVJALAN"
        self.SHEETY_HEADER = f"Bearer {self.SHEETY_TOKEN}"
        self.headers = {
            "Authorization": self.SHEETY_HEADER
        }

    def getdata(self):
        self.response = requests.get(self.SHEETY_GET_EP, headers=self.headers)
        return self.response.json()


    def add_iata(self,flight):
        for i in range(0, len(flight.iata_list)):
            print(i)
            self.SHEETY_PUT_EP = f"https://api.sheety.co/852527fb5a33178507bc563cf260bba5/flightDealsD39/prices/{i + 2}"  # Replace with your actual endpoint
              # Replace with the name of your sheet
            row_id = i + 2  # The ID of the row you want to update
            self.new_data = {
                "price": {
                    "iataCode": flight.iata_list[i],
                }
            }

            self.put_headers = {
                "Authorization": f"Bearer {self.SHEETY_TOKEN}",  # Replace with your actual token
            }
            response = requests.put(self.SHEETY_PUT_EP, json=self.new_data, headers=self.put_headers)

            if response.status_code == 200:
                print("Row updated successfully!")
            else:
                print("Failed to update row:", response.text)