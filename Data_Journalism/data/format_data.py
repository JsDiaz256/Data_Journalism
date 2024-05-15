import json


f1 = open("Sem2/Data_Journalism/data/DATA - data journalsm project - Farmers Markets in NYC.csv", "r")
lines = f1.read().splitlines()
line0 = lines[0].split(",")

borodict = {}

for borough in ["Manhattan", "Brooklyn", "Bronx", "Queens", "Staten Island"]:
    borodict[borough] = {}
    for line in lines:
        splitline = line.split(",")
        if splitline[0] == borough:
            tempdict = {}
            for place in range(2,4):
                tempdict[line0[place]] = splitline[place]
            borodict[borough][splitline[1]] = tempdict
# Create the dictionary here

f1.close()

f2 = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "w")
json.dump(borodict, f2, indent = 4)

f2.close()
