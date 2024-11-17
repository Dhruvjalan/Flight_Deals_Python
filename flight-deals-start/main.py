#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from pprint import pprint


city_list = []

sheet = DataManager()
sheet_details = sheet.getdata()
pprint(sheet_details)
for row in sheet_details['prices']:
    city_list.append(row['city'])

print(city_list)

flightsearcher = FlightSearch()
flightsearcher.get_access_token(city_list)
print(flightsearcher.iata_list)

sheet.add_iata(flightsearcher)

print("\n", sheet.getdata())

flight_data_manager = FlightData()
flight_data_manager.find_cheapest_flight(flightsearcher.iata_list)
