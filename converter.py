import re
from bs4 import BeautifulSoup
import requests


class FlightInfo:
    def __init__(self, airline_code, flight_number, cabin_class, date, passenger_count, route):
        self.airline_code = airline_code
        self.flight_number = flight_number
        self.cabin_class = cabin_class
        self.date = date
        self.passenger_count = passenger_count
        self.route = route


url = "https://en.wikipedia.org/wiki/List_of_airline_codes"

data1 = requests.get(url)
soup = BeautifulSoup(data1.content, "html.parser")
# class_="wikitable sortable jquery-tablesorter"
codes = soup.find("table")
if codes:
    rows = []
    for row in codes.find("tbody").find_all("tr"):
        cells = [td.text for td in row.find_all("td")]
        rows.append(cells)

    for row in rows:
        print(row)
# print(list1)
