'''
Created on Mar 25, 2019

@author: Chairman
'''
from httplib2 import Http
from urllib.parse import urlencode
from flask import Flask,render_template,request,jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("TestIndex.html")

@app.route('/test')
def testResult():
    return "TestIndex.html"

@app.route('/square/', methods=['POST'])
def square():
    urlString = request.form.get('urlString')
    methodType = request.form.get('methodType')
    httpTest = Http();
    resp, content = httpTest.request(urlString, methodType, urlencode(""))
    data = str(resp.status)+" "+resp.reason
    return data

if __name__ == "__main__":
    app.run(debug = True)