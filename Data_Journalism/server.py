from flask import Flask
from flask import request
from flask import render_template
import json


app = Flask(__name__, static_url_path='/Static', static_folder='Static')

@app.route('/')
def about():
    #load a current view of the data
    f = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "r")
    data = json.load(f)
    f.close()

    f2 = open("Sem2/Data_Journalism/data/Data_BoroCount.json", "r")
    boro_count_dict = json.load(f2)
    f2.close()
    
    zip_codes = set()
    for boros in data.keys():
        for store in data[boros].keys():
            zip_codes.add(str(boros) + ": " + str(data[boros][store]["Zip Code"]))

    zip = request.args.get('zip_choose')

    #render the template with the apporpriate data
    return render_template('about.html', boro_count_dict = boro_count_dict, boroughs=list(data.keys()), data=data, zip=zip, zip_codes=sorted(list(zip_codes)))


@app.route('/macro')
def macro():
    #load a current view of the data
    f = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "r")
    data = json.load(f)
    f.close()

    f2 = open("Sem2/Data_Journalism/data/Data_BoroCount.json", "r")
    boro_count_dict = json.load(f2)
    f2.close()


    farm,cart,bar,rest = 0,0,0,0
    total_dict = {}
    boro_eatery_dict = {}

    zip_codes = set()

    for boros in data.keys():
        boro_farm, boro_cart, boro_bar, boro_rest = 0,0,0,0
        for store in data[boros].keys():
            zip_codes.add(str(boros) + ": " + str(data[boros][store]["Zip Code"]))
            if data[boros][store]["Type"] == "Farmer's Market":
                farm += 1
                boro_farm+=1
            elif data[boros][store]["Type"] == "Food Cart":
                cart += 1
                boro_cart+=1
            elif data[boros][store]["Type"] == "Snack Bar":
                bar += 1
                boro_bar+=1
            else: 
                rest+=1
                boro_rest += 1
        boro_eatery_dict[boros] = [boro_farm, boro_cart, boro_bar, boro_rest]
        total_dict[boros] = [farm,cart,bar,rest]

    zip = request.args.get('zip_choose')

    macro_avg = round(332/len(zip_codes),2)

    #render the template with the apporpriate data
    return render_template('Macro_Page.html', macro_avg = macro_avg, total_dict=total_dict, singular_dict = boro_eatery_dict, boro_count_dict = boro_count_dict, boroughs=list(data.keys()), data=data, zip=zip, zip_codes=sorted(list(zip_codes)))



@app.route('/micro')
def micro():
    #load a current view of the data
    f = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "r")
    data = json.load(f)
    f.close()

    f2 = open("Sem2/Data_Journalism/data/Data_BoroCount.json", "r")
    boro_count_dict = json.load(f2)
    f2.close()

    boro = request.args.get('boro_choose')
    zip = request.args.get('zip_choose')

    zip_codes = set()
    zip_eateries = list()
    zip_farm = 0
    zip_cart = 0
    zip_bar = 0
    zip_rest = 0
    all_zip_counts = {}
    for boros in data.keys():
        for store in data[boros].keys():
            all_zip_counts[data[boros][store]["Zip Code"]] = all_zip_counts.get(data[boros][store]["Zip Code"], 0)+1 # d[key] = d.get(key, 0) + 1
            zip_codes.add(str(boros) + ": " + str(data[boros][store]["Zip Code"]))
            if str(data[boros][store]["Zip Code"]) in zip:
                zip_eateries.append(str(data[boros][store]["Type"])+"__"+store)
                if data[boros][store]["Type"] == "Farmer's Market":
                    zip_farm += 1
                elif data[boros][store]["Type"] == "Food Cart":
                    zip_cart += 1
                elif data[boros][store]["Type"] == "Snack Bar":
                    zip_bar += 1
                else: zip_rest += 1
    
    zip_types = ["Farmers Markets", "Food Carts", "Snack Bars", "Restaurants"]
    zip_unordered = [zip_farm, zip_cart, zip_bar, zip_rest]
    zip_pievals = []
    zip_total = 0
    zip_actual = []
    for i in range(4):
      temp_max = max(zip_unordered)
      zip_pievals.append(zip_types[zip_unordered.index(temp_max)]+"_"+str(temp_max+zip_total))
      zip_actual.append(zip_types[zip_unordered.index(temp_max)]+"_"+str(temp_max))
      zip_types.remove(zip_types[zip_unordered.index(temp_max)])
      zip_unordered.remove(temp_max)
      zip_total += temp_max

    macro_avg = round(332/len(zip_codes),2)

    #render the template with the apporpriate data
    return render_template('Micro_Page.html', macro_avg=macro_avg, all_zip_counts=all_zip_counts, zip_actual=zip_actual, zip_pie=zip_pievals, zip_eateries = zip_eateries, boro_count_dict = boro_count_dict, boroughs=list(data.keys()), boro = boro, data=data, zip=zip, zip_codes=sorted(list(zip_codes)))



@app.route('/format_data')
def format_data():
    #load a current view of the data

    #render the template with the apporpriate data
    return render_template('Sem2/Data_Journalism/data/format_data.py')



app.run(debug=True)
