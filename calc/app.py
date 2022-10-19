# Put your app in here.
from urllib import request
from flask import Flask
from flask import request

from operations import add, sub, mult, div


app = Flask(__name__)

@app.route("/add")

def add_args(): 
    """return the 2 query string paramters added"""
    
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    added = add(a, b)
    return str(added)

@app.route("/sub")
def sub_args(): 
    """return the 2 query string paramters subtracted"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    subtracted = sub(a, b)
    return str(subtracted)

@app.route("/mult")
def mult_args(): 
    """return the 2 query string paramters multiplied"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    multiplied = mult(a, b)
    return str(multiplied)

@app.route("/div")
def div_args(): 
    """return the 2 query string paramters divided"""
    a = int(request.args["a"])
    b = int(request.args["b"])
    
    divided = div(a, b)
    
    return str(divided)
