# Categorical Analysis of beta.SAM / FPDS 
import pandas as pd

## UPDATE ##
fpds = pd.read_excel(r"FPDS Sample Report.xlsx")

cols = []

for col in fpds.columns: 
    new_col = col.replace(" ","_")
    fpds = fpds.rename(columns={col:new_col})
    if fpds[new_col].dtype == 'object':
        cols.append(new_col)
del col

def review_categorical():
    print('########### REVIEW CATEGORICAL FIELDS ###########')
    print('')
    for col in cols:
        print('.........................................')
        print('### '+col+' ###')
        print('')
        df = pd.DataFrame(fpds[col])
        df['freq'] = df.groupby(col)[col].transform('count')
        df = df.drop_duplicates().sort_values(by='freq',ascending=False).reset_index()
        print('Number of Unique Values: '+str(len(df)))
        print('Number of Occurences: '+str(int(df['freq'].sum()))+" / "+str(len(fpds)))
        print('Top 10 Frequent Values:')
        print(df[[col,'freq']][:10])
        print('.........................................')
        print('')

review_categorical()

print('########### REVIEW DUPLCIATE FIELDS ###########')
print('')
duplicate = fpds[fpds.duplicated(['Description_of_Requirement', 'Product_or_Service_Code'])]
#print(duplicate)
print('Number of Records Duplicated by Description, PSC: ')
print(len(duplicate))

#duplicate.to_csv(r'all_duplicates.csv', index = False, header=True)

#All duplicates grouped by count
print('')
print('Counts of Duplicate Records Grouped by Description, PSC')
groupByCols = duplicate[['Description_of_Requirement', 'Product_or_Service_Code']].reset_index(level=0)
groupByCols = groupByCols.groupby(['Description_of_Requirement', 'Product_or_Service_Code'])["index"].count().reset_index(name="freq").sort_values(by="freq",ascending=False)
print(len(groupByCols))
print('Top 10 Frequent Values:')
print(groupByCols[['Product_or_Service_Code','Description_of_Requirement','freq']][:10])
#groupByCols.to_csv (r'duplicates_group_count.csv', index = False, header=True)
#print(groupByCols)

