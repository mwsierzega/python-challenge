# open csv files

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

#read csv file

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    #skip the header
    csv_header = next(csvreader)
    
    #print analysis
    print("Election Results")
    print("-------------------------")
    
    #variables
    totalballots = 0
    fullcandidate_list = []
    candidate_list = []
    percent_Charlies = 0
    total_Charlies = 0
    counter_Charlies = []
    
    for row in csvreader:
        totalballots = totalballots + 1
        
        #makes candidate column into a list
        fullcandidate_list = [(row[2])]
        
        #look through candidate colun list to get list of candidates
        for i in fullcandidate_list:
            if i not in candidate_list:
                candidate_list.append(i)
                
        for i in fullcandidate_list:
            if i == candidate_list[0]:
                counter_Charlies += [i]
                
        total_Charlies = len(counter_Charlies)
        percent_Charlies = round((total_Charlies/totalballots)*100, 3)
        
print(f"Total Votes: {totalballots}")
print("-------------------------")
print(f"{candidate_list[0]}: {percent_Charlies}% ({total_Charlies})")
print(f"{candidate_list[1]}: ")
print(f"{candidate_list[2]}: ")
print("-------------------------")
print(f"Winner: ")
print("-------------------------")