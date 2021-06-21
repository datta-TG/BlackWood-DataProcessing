#           Probate Script for transforming CSVs to only one table
import os
import pandas as pd

def read_clean_csv(path):
    main_columns = ['Case Number Probate','County','Filing Date']
    df = pd.read_csv(path)
    columns = df.columns.tolist()
    #Validation Case Number
    other_case_number_names = ['Case Number','Case number','Case Nnumber']
    matches = list(set(columns) & set(other_case_number_names))
    if(len(matches)==1):
        df.rename(columns={matches[0]:'Case Number Probate'}, inplace=True)
    # County integration"""
    df['County'] = 'Miami Dade'
    return df[main_columns]

path_to_files = "./data/input/Probate/"
path_output = "./data/output/Probate.csv"
list_of_files = os.listdir(path_to_files)
if(len(list_of_files)>0):
    df = read_clean_csv(os.path.join(path_to_files,list_of_files[0]))
    for i in range(1,len(list_of_files)):
        df = pd.concat([df,read_clean_csv(os.path.join(path_to_files,list_of_files[i]))])
    print(df.info())
df.to_csv(path_output,index=False)