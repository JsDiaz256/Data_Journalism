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

    boro = request.args.get('boro_choose')
    
    zip_codes = set()
    for boros in data.keys():
        for store in data[boros].keys():
            zip_codes.add(data[boros][store]["Zip Code"])

    zip = request.args.get('zip_choose')
    if zip == "":
        zip = sorted(list(zip_codes))[0]

    #render the template with the apporpriate data
    return render_template('about.html', boroughs=sorted(data.keys()), boro = boro, data=data, zip=zip, zip_codes=sorted(list(zip_codes)))


@app.route('/macro')
def macro():
    #load a current view of the data
    f = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "r")
    data = json.load(f)
    f.close()

    boro = request.args.get('boro_choose')

    zip_codes = set()
    for boros in data.keys():
        for store in data[boros].keys():
            zip_codes.add(data[boros][store]["Zip Code"])

    zip = request.args.get('zip_choose')
    if zip == "":
        zip = sorted(list(zip_codes))[0]

    #render the template with the apporpriate data
    return render_template('Macro_Page.html', boroughs=sorted(data.keys()), boro = boro, data=data, zip=zip, zip_codes=sorted(list(zip_codes)))



@app.route('/micro')
def micro():
    #load a current view of the data
    f = open("Sem2/Data_Journalism/data/Data_Boroughs.json", "r")
    data = json.load(f)
    f.close()

    boro = request.args.get('boro_choose')

    zip_codes = set()
    for boros in data.keys():
        for store in data[boros].keys():
            zip_codes.add(data[boros][store]["Zip Code"])

    zip = request.args.get('zip_choose')
    if zip == "":
        zip = sorted(list(zip_codes))[0]


    #render the template with the apporpriate data
    return render_template('Micro_Page.html', boroughs=sorted(data.keys()), boro = boro, data=data, zip=zip, zip_codes=sorted(list(zip_codes)))



@app.route('/format_data')
def format_data():
    #load a current view of the data

    #render the template with the apporpriate data
    return render_template('Sem2/Data_Journalism/data/format_data.py')



app.run(debug=True)
