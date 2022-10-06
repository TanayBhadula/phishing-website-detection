from xml.sax.xmlreader import InputSource
 
from flask import Flask,render_template,request
 
import inputScript
import pickle
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/getURL',methods=['GET','POST'])
def getURL():
    if request.method == 'POST':
        url = request.form['url']
        print(url)
        URLfeatures = inputScript.main(url)
          
        api ='http://1079582b-459b-41f0-9e68-c2d6b3f2cf55.eastus2.azurecontainer.io/score'

        data = {
            "data": URLfeatures,
            "method": "predict" 
            }

        headers = {'Content-Type': 'application/json'}

        r = requests.post(api, str.encode(json. dumps (data)), headers = headers) 
        s = r.json()
        predicted_value = s['predict']

        print(predicted_value)
        if predicted_value == 1:
            value = "Legitimate"
            return render_template("home.html",error=value)
        if predicted_value == -1:
            value = "Phishing"
            return render_template("home.html",error=value)
 
        #RFmodel = pickle.load(open('stack_fish.pkl', 'rb'))
        #predicted_value = RFmodel.predict(data)
         
         

if __name__ == "__main__":
    app.run(debug=True)