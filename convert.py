import pandas as pd
from jinja2 import Template
import argparse

# Specify command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--spreadsheet", help="Excel file from MS forms")
parser.add_argument("-m", "--map", help="Column mapping")
parser.add_argument("-t", "--template", help="Jinja template")
args = parser.parse_args()

# Import the column mapping in file named in parameter -m
headers = [i.strip().split("\t")[1] for i in open(args.map,'r').readlines()]

# Read in the Microsoft forms data from the Excel spreadsheet in file named in parameter -s
data = pd.read_excel(args.spreadsheet)
data.columns = headers
print(data.head())

# Import the template in file named in parameter -t
with open(args.template) as f:
    tmpl = Template(f.read())

for index,row in data.iterrows():
    with open(f"{row['id']}.html", 'w') as outputfile:
        # try:
        outputpage = tmpl.render(data=row)
        outputfile.write(outputpage)
        # except:
        #     print(f"Row ID {row['id']} has an error")
