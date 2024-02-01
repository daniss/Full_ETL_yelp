import pandas as pd
from extractdata import scrape
from put_data import put_data
import re

# We will use the following function to clean the data:
def clean_data(data):
    data = data.replace("Ville : ", "")
    data = re.sub(r' et \d+\.', ',', data)
    data = data.replace("This is a placeholder +", "")
    data = re.sub(r'(\b\w+\b),\d+\.\s*', r'\1,', data)
    data = re.sub(r'(\b\w[\w\s]+\w)(\d+\.\d+)', r'\1,\2,', data) # ajoute , avec le (review)
    data = re.sub(r',\s*(\([^)]+\))', r',\1,', data)
    data = re.sub(r'€+', r',\g<0>,', data)
    return data

# We will use the following function to transform the data:
def transform_data(data):
    data = data.split("\n")
    data = [clean_data(d) for d in data if d != ""]
    return data

# We will use the following function to run the pipeline:
def run_pipeline():
    f = open("data.json", "r")
    data = f.read()
    data = transform_data(data)
    data = [line for line in data if len(line.split(',')) == 7]
    f.close()
    f = open("data.csv", "w")
    for d in data:
        f.write(d + "\n")
    f.close()

def transform():
    scrape()
    run_pipeline()
    put_data()

if __name__ == "__main__":
    transform()