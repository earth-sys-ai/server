# import flask modules
from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS

# data retrieval code
import sys
sys.path.append('database')
from data import *

# get location from query string
app = Flask(__name__)
CORS(app)
@app.route('/')
def display():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    add = request.args.get('add')
    clr = request.args.get('clr')
    red = request.args.get('red')
    lis = request.args.get('lis')
    rad = request.args.get('rad')

    if (red == "true"):
        return getData(lat, lng)
    
    elif (clr == "true"):
        clearData(lat, lng)
        return ""

    elif (lis == "true"):
        return listData(lat, lng, rad)

    elif(add != ""):
        addData(lat, lng, add)
        return ""

# begin web server
if __name__=='__main__':
    app.run(port=5000)
