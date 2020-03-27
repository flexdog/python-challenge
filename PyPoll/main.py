# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 13:38:26 2020

@author: 212742984
"""


import os
import csv
import sys
csvPath = os.path.join("Resources", "PyPoll_election_data.csv")

with open(csvPath, newline='') as csvFile:
    khan_count = 0
    correy_count = 0
    li_count = 0
    oTooley_count = 0
    csvReader = csv.reader(csvFile, delimiter=",")
    csvHeader = next(csvReader)
    
    for row in csvReader:
        khan = row[2]
        if khan == 'Khan':
            khan_count = khan_count +1
        correy = row[2]
        if correy == 'Correy':
            correy_count = correy_count + 1
        li = row[2]
        if li == 'Li':
            li_count = li_count + 1
        oTooley = row[2]
        if oTooley == "O'Tooley":
            oTooley_count = oTooley_count + 1
            
total_votes = csvReader.line_num -1
print(f"File reports: {total_votes}")

if (khan_count + correy_count + li_count + oTooley_count) == total_votes:
    print(f"{total_votes} votes are accounted.")
else:
    print("Not all votes are accounted.")

khan_percent = float(khan_count / total_votes)
correy_percent = float(correy_count / total_votes)
li_percent = float(li_count / total_votes)
oTooley_percent = float(oTooley_count / total_votes)


if khan_count > 0:
    winner = "Khan"
if correy_count > khan_count:
    winner = "Correy"
if li_count > correy_count:
    winner = "Li"
if oTooley_count > li_count:
    winner = "O'Tooley"  

print("")
print("")
print("Election Results")
print("--------------------------------------")
print(f"Total Votes:  {total_votes}")
print("--------------------------------------")
print(f"Khan: " + "{0:.3%}".format(khan_percent) + " (" + str(khan_count) + ")")
print(f"Correy: " + "{0:.3%}".format(correy_percent) + " (" + str(correy_count) + ")")
print(f"Li: " + "{0:.3%}".format(li_percent) + " (" + str(li_count) + ")")
print(f"O'Tooley: " + "{0:.3%}".format(oTooley_percent) + " (" + str(oTooley_count) + ")")
print("--------------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------------")         

sys.stdout=open("Election_Data.txt","w")
print("Election Results")
print("--------------------------------------")
print(f"Total Votes:  {total_votes}")
print("--------------------------------------")
print(f"Khan: " + "{0:.3%}".format(khan_percent) + " (" + str(khan_count) + ")")
print(f"Correy: " + "{0:.3%}".format(correy_percent) + " (" + str(correy_count) + ")")
print(f"Li: " + "{0:.3%}".format(li_percent) + " (" + str(li_count) + ")")
print(f"O'Tooley: " + "{0:.3%}".format(oTooley_percent) + " (" + str(oTooley_count) + ")")
print("--------------------------------------")
print(f"Winner:  {winner}")
print("--------------------------------------")
sys.stdout.close() 
       
        