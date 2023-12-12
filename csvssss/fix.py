import csv

csv_file = "airlines.csv"
csv_file1 = "airliness.csv"
list1 = []
with open(csv_file, "r") as file:
    csvreader = csv.reader(file)

    for i in csvreader:
        list1.extend(i)

list2 = []
for i in range(len(list1)):
    a = list1[i]
    print(a.replace("\t", ","))

#for i in range(998):
    #print(f"{list1[i][0][0:2]}, {list1[i][0][2:6]}, {list1[i][0][6:21]}")
#    print(type(list1[i][0]))
"""
with open(csv_file1, "w") as file1:
    csvreader1 = csv.writer(file1)

    for i in list1:

        csvreader1.writerow(i)
"""
"""
for i in range(999):
    if "\t" in list1[i][0]:
        s = list1[i][0].split("\t")

        with open(csv_file, "w") as shit:
            csv_shit = csv.writer(shit)

            csv_shit.writerows(s)
"""

