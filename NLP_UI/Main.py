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

        resultSet = processquery.Process(name) 

        if resultSet is None:
            return render_template("error.html", variable = resultSet,  data="Please check if your query is compatible with our system!")
        
        numberOfColumns = len(resultSet.columns)
        if numberOfColumns == 1:
            if resultSet[' '].iloc[0] is not None:
                splitValue = str(round(resultSet[' '].iloc[0], 2))
            else:
                splitValue = 'None'
            return render_template("singlevaluetemplate.html", variable = resultSet,  data=splitValue, query = name)
        else:
            return render_template("tabletemplate.html", variable = resultSet,  data=resultSet.to_html(classes=["table-sm"],header=True) , query = name)

        return None

        
""" if __name__ == "__main__":
    app.run() """


  