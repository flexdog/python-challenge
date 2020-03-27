# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 10:06:51 2020

@author: 212742984
"""

import os
import csv
import sys

path = os.path.join("Resources", "PyBank_budget_data.csv")


with open(path, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    min_value = sys.maxsize
    max_value = 0
    csv_header = next(csvreader)
    row_count = 0
    total = 0
    
    for item in csvreader:
        initial = int(item[1])
        break
    for row in csvreader:
        val = int(row[1])
        if val < min_value:
            min_value = val
            min_month = row[0]
        if val > max_value:
            max_value = val
            max_month = row[0]
        row_count = row_count + 1
        total = total + val

        final = int(row[1])
     
        average_change = (final - initial)/row_count
    
   
    print("")
    print("Financial Analysis")
    print("-----------------------------------------------------------------")
    print("")
    print(f"Total Months: {row_count}")
    print(f"Total: ${ total}")        
    print("Average Change: ${:.2f}".format(average_change))
    print(f"The Greatest Increase in Profits: {max_month}  ${max_value}")
    print(f"The Greatest Decrease in Profits: {min_month}  ${min_value}")


sys.stdout=open("Bank_Financial_Data.txt","w")
print("")
print("Financial Analysis")
print("-----------------------------------------------------------------")
print("")
print(f"Total Months: {row_count}")
print(f"Total: ${ total}")        
print("Average Change: ${:.2f}".format(average_change))
print(f"The Greatest Increase in Profits: {max_month}  ${max_value}")
print(f"The Greatest Decrease in Profits: {min_month}  ${min_value}")
sys.stdout.close()
