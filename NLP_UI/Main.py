from flask import Flask, render_template, request
from flask import request, redirect
from flask import jsonify
import csv
import time
import subprocess
from subprocess import Popen, PIPE
import query_1
import pandas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/query",methods=['GET','POST'])
def query():
    if request.method=='POST':
       
        name = request.form['name']
        fieldnames = ['name']

        # the Input text is going to be written in csv.
        with open('nameList.csv','w') as inFile:

            
            writer = csv.DictWriter(inFile, fieldnames=fieldnames)

            # writerow() will write a row in your csv file
            writer.writerow({'name': name})
        
        # Add a sleep time for the above process to excute
        time.sleep(1)

        result_2= query_1.main() # Run temp.py 
         
        n=len(result_2.columns) 
        if n==1:
            return render_template("query.html", variable = result_2,  data=result_2.to_html(index=True,header=True)) #print(result)
        else:
            return render_template("query2.html", variable = result_2,  data=result_2.to_html(index=True,header=True)) #print(result)


        
if __name__ == "__main__":
    app.run()


  