def main():

    import subprocess
    from subprocess import Popen, PIPE
    import csv
    import os
    import pandas as pd
    import sqlite3
    import sys

    # Set working Directory
    os.chdir("C:/Users/majaa/Desktop/DAEN-690/UI")

    # Store the question from the csv file created by main.py .
    with open('nameList.csv', newline='') as f:
        reader = csv.reader(f)
        data = list(reader)

    # Pass the question to a variable.
    x=(data[0])

    ## Change the qustion to string from list.
    def listToString(s):  
        
        # initialize an empty string 
        str1 = ""  
        
        # traverse in the string   
        for ele in s:  
            str1 += ele   
        
        # return string   
        return str1  
            

    x=listToString(x)

    x_2=x

    string_in_string = 'python -m ln2sql.main -d database_store/procurment.sql -l lang_store/english.csv -j output.json -i {} '.format(x_2)

    #print(string_in_string)


    ############### Stop the print of subprocess ######################
    # Run the ln2sql file.
    import os
    import subprocess
    FNULL = open(os.devnull, 'w')


    # create two files to hold the output and errors, respectively
    with open('out.txt','w+') as fout:
        with open('err.txt','w+') as ferr:
            out= subprocess.call( string_in_string,shell=True, stdout=fout, stderr=ferr , cwd= "C:/Users/majaa/Desktop/DAEN-690/ln2sql")
            #out=subprocess.call(["ls",'-lha'],stdout=fout,stderr=ferr)
            # reset file to read from it
            fout.seek(0)
            # save output (if any) in variable
            output=fout.read()

            # reset file to read from it
            ferr.seek(0) 
            # save errors (if any) in variable
            #errors = ferr.read()


    with open('out.txt', 'r') as file:
        data = file.read().replace('\n', ' ')


    output_1 = output.replace('\n', ' ')
    sql_call_1 = output_1.replace(';', '')


    ######################################################## SQL ###########################################################################


    # connecting to the database  
    connection = sqlite3.connect("final_all.db") 
    

    crsr = connection.cursor() 
    crsr.execute(sql_call_1)  #new_sql_call
    
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

if __name__ == "__main__":
    main()