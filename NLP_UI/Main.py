from flask import Flask, render_template, request
from flask import request, redirect
from flask import jsonify
import csv
import time
import subprocess
from subprocess import Popen, PIPE
import processquery
import pandas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/query",methods=['GET','POST'])
def query():
    if request.method=='POST':
       
        name = request.form['name']
        #fieldnames = ['name']
        time.sleep(1)

        result_2 = processquery.Process(name) # Run temp.py 

        if result_2 is None:
            return render_template("error.html", variable = result_2,  data="Please check if your query is compatible with our system!")
        
        print(type(result_2))

        print(result_2)
        
        n = len(result_2.columns)
        if n==1:
            return render_template("error.html", variable = result_2,  data=result_2.to_html(index=True,header=True))
        else:
            return render_template("tabletemplate.html", variable = result_2,  data=result_2.to_html(classes=["table-sm"],header=True) , query = name)

        #return None

        
""" if __name__ == "__main__":
    app.run() """


  