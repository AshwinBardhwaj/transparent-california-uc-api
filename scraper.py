from flask import Flask
import os
import requests
import urllib.request
import json
import ssl
import html_to_json

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

ssl._create_default_https_context = ssl._create_unverified_context

def readPage(pageNum):
    try:
        os.remove("dataset")
    except OSError:
        print("No such file exists.")
    opener = AppURLopener()
    
    with opener.open(f"https://transparentcalifornia.com/salaries/2022/university-of-california/?page={pageNum}") as url:
        #print(url.read())
        #print(url.getcode())
        data = html_to_json.convert(url.read()) 
        #data = json.loads(url.read())

    new_data = data["html"][0]["body"][0]["div"][2]["div"][1]["div"][0]["table"][0]["tbody"][0]["tr"]
    d = open("dataset", "w")
    d.write(json.dumps(new_data, indent=4))
    d.close()
    opener.close()

#webpage = opener.open('https://transparentcalifornia.com')
#print(webpage.getcode())
#data = json.load(webpage)
#print(data)
#webpage = urllib.request.urlopen('https://transparentcalifornia.com', context=context).read()

#print("result code: " + str(webpage.getcode()))

"""
app = Flask(__name__)

@app.route("/")
def say_hello():
    return "Hello World"

@app.route("/pika")
def pika():
    return "Pik Pika Pikachu"
    """