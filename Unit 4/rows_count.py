#Program to count number of rown in a csv file
import csv 
rowc = 0
filen="count.csv"
with open(filen,"r") as file:
    r=csv.reader(file)
    for row in r:
        rowc+=1
print("Number of rows = ",rowc) 

