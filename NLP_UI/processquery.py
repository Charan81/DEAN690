import subprocess
from subprocess import Popen, PIPE
import csv
import os
import pandas as pd
import sqlite3
import sys
import shlex

def Process(searchQuery):

    resultDataframe = None
    searchQuery = '\"' + searchQuery + '\"'
    string_in_string = 'python -m ln2sql.main -d database_store/product.sql -l lang_store/english.csv -j output.json -i {} '.format(searchQuery)

    subprocessCommand = shlex.split(string_in_string)
    print(subprocessCommand)
    ############### Stop the print of subprocess ######################
    try:
        output = subprocess.check_output(subprocessCommand, stderr=subprocess.STDOUT).decode()
        print("Output: " + output)
        resultDataframe = SqlProcessing(output)
    except Exception as ex:
        resultDataframe = None

    return resultDataframe



def SqlProcessing(output):
    ######################################################## SQL ###########################################################################

    try:
        flattenedOutput = output.replace('\n', ' ')
        sql_query = flattenedOutput.replace(';', ' limit 1000;')
        # connecting to the database  
        connection = sqlite3.connect("final_all.db") 
        

        crsr = connection.cursor() 
        crsr.execute(sql_query)  #new_sql_call
        
        # store all the fetched data in the ans variable 
        ans = crsr.fetchall()  
        
        # Since we have already selected all the data entries  
        # using the "SELECT *" SQL command and stored them in  
        # the ans variable, all we need to do now is to print  
        # out the ans variable 

        ##################### Data Frame #######################

        df = pd.DataFrame(ans)

        ################## Add Column Names #####################
        
        if len(df.columns) == 1:
            df_new = df.rename(columns={0: ' '})
        else :
            df_new = df.rename(columns={0:'ID', 1 : 'business_unit', 2:'psc_code', 3:'obj_code', 4:'sub_obj_descr', 5:'order_date',6:'order_title',7:'line_description',8:'vendor_name',9:'vendor_country',10:'cost'})
        
        #########################################################
        return df_new
    except Exception as ex:
        return ex

""" if __name__ == "__main__":
    main() """