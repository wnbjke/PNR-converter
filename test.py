import re
import csv
from datetime import datetime

aircodes_file = "csvssss/airport_codes.csv"
airport_fields = []
airport_rows = []
date_file = "csvssss/date.csv"
date_fields = []
date_rows = []
week_file = "csvssss/week.csv"
week_fields = []
week_rows = []

with open(aircodes_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    airport_fields = next(csvreader)

    for row in csvreader:
        airport_rows.append(row)
'''
with open(date_file, "r") as date_months:
    csv_dates = csv.reader(date_months)

    for row in csv_dates:
        date_rows.append(row)
'''
with open(week_file, "r") as week_days:
    csv_days = csv.reader(week_days)

    for row1 in csv_days:
        week_rows.append(row1)


def parse_pnr_data(pnr_data):
    # Define a regular expression pattern to extract information
    # LH 433Y 15DEC F ORDFRA*SS1 1035P 1500P 16DEC J /DCLH /E -> pattern1
    # QR 740S 18MAR 1 LAXDOH*SS1  1615  1750 19MAR 2 /DCQR /E
    pattern = r"([A-Z]{3})\s*(\d{3})([A-Z]{1})\s*(\d{2}[A-Z]{3})\s*([A-Z]{1})\s*([A-Z]{3})([A-Z]{3})\*([A-Z]{2}\d{1})\s*(\d{4}[A-Z]{1})\s*(\d{4}[A-Z]{1})\s*(\d{2}[A-Z]{3})\s*([A-Z]{1})\s*(/[A-Z]{4})\s*(/[A-Z]{1})"
    pattern2 = r"([A-Z]{3})"
    if re.match(pattern, pnr_data):
        result = re.match(pattern, pnr_data)
        if result:
        # Extract information from the matched groups
            for row in airport_rows:
                if row[0] == result.group(1):
                    operated_airline = row[2]
            # airline_code = result.group(1)
            flight_number = result.group(2)
            # flight_class = result.group(3)
            for row in week_rows:
                if row[0] == result.group(5):
                    # (result.group(4), row[1])
                    # f"{result.group(5)}, {row[1]}"
                    departure_date = f"{result.group(4)}, {row[1]}"
            for row in airport_rows:
                if row[0] == result.group(6):
                    where_from = row[1]
            for row in airport_rows:
                if row[0] == result.group(7):
                    where_to = row[1]
            for row in week_rows:
                if row[0] == result.group(12):
                    arrival_date = f"{result.group(11)}, {row[1]}"
            # route = result.group(6)
            # .strftime("%I:%M%p")
            # .strftime("%H:%M%p")
            departure_time_date = f"""{datetime.strptime(
                result.group(9)[0:4], '%H%M').strftime('%H:%M %p')} {departure_date}"""

            arrival_time_date = f"""{datetime.strptime(
                result.group(10)[0:4], '%H%M').strftime('%H:%M %p')} {arrival_date}"""

            # Return the extracted information as a dictionary
            return [
                (
                    operated_airline,
                    flight_number,
                    departure_time_date,
                    where_from,
                    arrival_time_date,
                    # where_to,
                    "temporary unknown",
                    "Layover time"
                )
            ]
        else:
            return None
        
    elif re.match(pattern2, pnr_data):
        result = re.match(pattern2, pnr_data)
        if result:
            return [("matched",)]
    # Use the regular expression to match the pattern in the data
    
    
    '''
    {
            "Departure Date": departure_date,
            "Airline": operated_airline,
            "Flight Number": flight_number,
            "Departure Time": departure_time,
            "Where_from": where_from,
            "Arrival Time": arrival_time,
            "Where_to": where_to,
            "Duration": "unknown for a moment",
            # "Class": flight_class,
            # "Arrival Date": arrival_date,
            # "Booking Code": booking_code
        }
    '''


# Example usage
pnr_data = "AZO 433Y 15DEC F ORDFRA*SS1 1035P 1500P 16DEC W /DCLH /E"
result = parse_pnr_data(pnr_data)
print(result)

# if result:
#    for key, value in result.items():
#        print(f"{key}: {value}")
# else:
#    print("Unable to parse PNR data.")
