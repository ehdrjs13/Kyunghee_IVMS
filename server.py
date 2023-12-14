from flask import Flask, request, jsonify
import requests
import pandas as pd 

app = Flask(__name__)

@app.route('/mainEntrial/<id>', methods = ['POST'])
def search(id):
    
