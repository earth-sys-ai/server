# import web and transection requirements
from flask import Flask
from flask import request
from flask import render_template
from flask_cors import CORS
from os import listdir
from transect import transect
import json
import sys

# main vector var
data = []
levels = []

# get location from query string
app = Flask(__name__)
CORS(app)
@app.route('/')
def display():
    
    # url parameters
    com = request.args.get('com', type = str)
    level = request.args.get('level', type = int)
    response = json.dumps({
        "error": "Invalid command!"
    })

    # check for 500 
    try:
        
        # list level information
        if (com == "listLevels"):
            response = json.dumps({
                "levelCount": len(data),
                "levels": levels
            })

        # dump data from given level
        elif (com == "getData"):
            response = json.dumps(data[levels.index(level)])

        # polygonal transection
        elif (com == "transect"):
            response = transect(data[levels.index(level)], request.args.get('line'))

    # alert
    except:
        response = json.dumps({
            "error": "Error in computation!"
        })

    # return as json
    return app.response_class(
        response=response,
        status=200,
        mimetype='application/json'
    )

# startup
if __name__=='__main__':

    # cache files
    cacheDir = sys.argv[1] 
    names = listdir(cacheDir)
    for filename in names:
        with open(cacheDir + "/" + filename) as f:
            level = int(filename[:-5])
            data.append(json.load(f))
            levels.append(level)
            print("Loaded cache: " + filename)

    # begin web server
    print("\nStarting webserver...")
    app.run(host='0.0.0.0', port=5000)
