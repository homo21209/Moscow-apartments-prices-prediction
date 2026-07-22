import kagglehub
import os
import csv

from fontTools.t1Lib import writeOther

# Download latest version
path = kagglehub.dataset_download("egorkainov/moscow-housing-price-dataset")
outfile =  r"C:\Users\user\moscow_apartments\data\raw\moscow_apartments.csv"

print("Path to dataset files:", path)

file_path = os.path.join(path,'data.csv')

with open(file_path,newline='',mode='r',encoding='utf-8') as f:
    with open(outfile,mode='w',encoding='utf-8',newline='') as of:
        reader = csv.reader(f)
        writer = csv.writer(of)
        for row in reader:
            writer.writerow(row)

