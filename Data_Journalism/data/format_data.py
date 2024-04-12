import json


f1 = open("/Users/jasiellediaz/Library/Mobile Documents/com~apple~CloudDocs/ADV_CS/Sem2/Data_Journalism/data/DATA - data journalsm project - Farmers Markets in NYC.csv", "r")
lines = f1.read().splitlines()
line0 = lines[0].split(",")

dictionary ={}


count = 0

for entry in lines:
    tempdict = {}
    betterentry = entry.split(",")
    for columnplace in range(len(line0)):
        tempdict[line0[columnplace]] = betterentry[columnplace]
    dictionary[count] = tempdict
    count+=1
# Create the dictionary here

f1.close()

#Save the json object to a file
f2 = open("/Users/jasiellediaz/Library/Mobile Documents/com~apple~CloudDocs/ADV_CS/Sem2/Data_Journalism/data/Data_Farmers.json", "w")
json.dump(dictionary, f2, indent = 4)

f2.close()




f3 = open("/Users/jasiellediaz/Library/Mobile Documents/com~apple~CloudDocs/ADV_CS/Sem2/Data_Journalism/data/DATA - data journalsm project - Eateries in NYC Parks.csv", "r")
lines2 = f3.read().splitlines()
line02 = lines2[0].split(",")

dictionary2 ={}


count2 = 0

for entry2 in lines2:
    tempdict2 = {}
    betterentry2 = entry2.split(",")
    for columnplace2 in range(len(line02)):
        tempdict2[line02[columnplace2]] = betterentry2[columnplace2]
    dictionary2[count2] = tempdict2
    count2+=1
# Create the dictionary here

f3.close()

#Save the json object to a file
f4 = open("/Users/jasiellediaz/Library/Mobile Documents/com~apple~CloudDocs/ADV_CS/Sem2/Data_Journalism/data/Data_Eateries.json", "w")
json.dump(dictionary, f4, indent = 4)

f4.close()
