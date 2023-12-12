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
airlines = "csvssss/airliness.csv"
airlines_rows = []

with open(aircodes_file, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    for row in csvreader:
        airport_rows.append(row)

with open(airlines, "r") as file:
    csv_lines = csv.reader(file)

    for row in csv_lines:
        airlines_rows.append(row)

with open(week_file, "r") as week_days:
    csv_days = csv.reader(week_days)

    for row1 in csv_days:
        week_rows.append(row1)


def parse_pnr_data(pnr_data):
    # Define a regular expression pattern to extract information
    # LH 433Y 15DEC F ORDFRA*SS1 1035P 1500P 16DEC J /DCLH /E -> pattern1
    # KE  12Q 18MAR 1 LAXICN*SS1  2340  0510   20MAR 3 /DCKE /E -> pattern2
    # AZO 433Y 15DEC F ORDFRA*SS1 1035P 1500P 16DEC J /DCLH /E -> test
    # QR 740S 18MAR 1 LAXDOH*SS1  1615  1750 19MAR 2 /DCQR /E
    # FI 630J 07MAR Q BOSKEF SS2 800P 615A 08MAR F /DCFI /E

    pattern1 = r"([A-Z]{2})\s*(\d{3})([A-Z]{1})\s*(\d{2}[A-Z]{3})\s*([A-Z]{1})\s*([A-Z]{3})([A-Z]{3})\*([A-Z]{2}\d{1})\s*(\d{4}[A-Z]{1})\s*(\d{4}[A-Z]{1})\s*(\d{2}[A-Z]{3})\s*([A-Z]{1})\s*(/[A-Z]{4})\s*(/[A-Z]{1})"
    pattern2 = r"([A-Z]{2})\s*(\d{2})([A-Z]{1})\s*(\d{2}[A-Z]{3})\s*(\d{1})\s*([A-Z]{3})([A-Z]{3})\*([A-Z]{2}\d{1})\s*(\d{4})\s*(\d{4})\s*(\d{2}[A-Z]{3})\s*(\d{1})\s*(/[A-Z]{4})\s*(/[A-Z]{1})"
    pattern3 = r"([A-Z]{2})"
    patterns = [pattern1, pattern2, pattern3]
    for pattern in patterns:
        if re.match(pattern, pnr_data):
            result = re.match(pattern, pnr_data)
            if result:
                # Extract information from the matched groups
                for row in airlines_rows:
                    if row[0] == result.group(1):
                        operated_airline = f"{row[2]}, {row[-1]}"
                # airline_code = result.group(1)
                flight_number = result.group(2)
                # flight_class = result.group(3)
                for row in week_rows:
                    if row[0] == result.group(5):
                        # (result.group(4), row[1])
                        # f"{result.group(5)}, {row[1]}"
                        departure_date = f"{result.group(4)}, {row[1]}"
                    else:
                        departure_date = f"{result.group(4)}, unknown"
                for row1 in airport_rows:
                    if row1[0] == result.group(6):
                        where_from = row1[1]
                for row2 in airport_rows:
                    if row2[0] == result.group(7):
                        where_to = row2[1]
                for row3 in week_rows:
                    if row3[0] == result.group(12):
                        arrival_date = f"{result.group(11)}, {row3[1]}"
                    else:
                        arrival_date = f"{result.group(11)}, unknown"

                # route = result.group(6)
                # .strftime("%I:%M%p")
                # .strftime("%H:%M%p")
                departure_time_date = f"""{datetime.strptime(
                    result.group(9)[0:4], '%H%M').strftime('%H:%M %p')} {departure_date}"""

                #date1 = datetime.strptime(result.group(9)[0:4], "%H%M").strftime('%H:%M %p')
                #date2 = datetime.strptime(result.group(11), "%H%M").strftime('%H:%M %p')
                arrival_time_date = f"""{datetime.strptime(
                    result.group(10)[0:4], '%H%M').strftime('%H:%M %p')} {arrival_date}"""

                # calculate duration
                time_format = "%H:%M %p" # Hour:Minute AM/PM format
                date_1 = departure_time_date[0:8]
                date_2 = arrival_time_date[0:8]
                date_1_duration = datetime.strptime(date_1, time_format)
                date_2_duration = datetime.strptime(date_2, time_format)
                flight_duration = str(date_2_duration - date_1_duration)
                print(flight_duration)
                # Return the extracted information as a dictionary
                return [
                    (
                        operated_airline,
                        flight_number,
                        departure_time_date,
                        where_from,
                        arrival_time_date,
                        flight_duration,
                        "Layover time"
                    )
                ]
            else:
                return None
    """
    elif re.match(pattern2, pnr_data):
        result = re.match(pattern2, pnr_data)
        if result:
            return [("matched",)]
    """

# Example usage
#pnr_data = "AZO 433Y 15DEC F ORDFRA*SS1 1035P 1500P 16DEC W /DCLH /E"
#result = parse_pnr_data(pnr_data)

time_str1 = "11:40 PM"
time_str2 = "05:10 AM"

# Convert time strings to datetime objects
time_format = "%I:%M %p"
time1 = datetime.strptime(time_str1, time_format)
time2 = datetime.strptime(time_str2, time_format)

# Calculate the time difference
time_difference = time2 - time1
# Print the result
print("Time Difference:", time_difference)
