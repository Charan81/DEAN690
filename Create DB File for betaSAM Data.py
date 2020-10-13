import pandas as pd
import sqlite3
from sqlalchemy import create_engine

# Connect to database file
conn = sqlite3.connect('FPDS Practice.db')
c = conn.cursor()

# Create sqlalchemy engine
engine = create_engine('sqlite://', echo=False)

# read in file
df = pd.read_excel("FPDS Sample Report.xlsx")

# turn file into sql
df.to_sql('fpds', con=engine)

# check to see it worked
engine.execute("SELECT * FROM fpds").fetchall()

# Commit and close
conn.commit()
conn.close()
