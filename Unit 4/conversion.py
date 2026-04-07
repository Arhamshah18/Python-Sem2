import json 
import csv 

filename="data.json"

try:
    #open json file & read data
    with open(filename,'r') as jsonf:
        data=json.load(jsonf)   

    #open csv file & write data
    with open('output.csv','w',newline='') as csvf:
        headers=data[0].keys()
        writer=csv.DictWriter(csvf,fieldnames=headers) 
        writer.writeheader()
        writer.writerow(data)
    print("Conversion Successful")

except FileNotFoundError:
    print("File not found") 

    