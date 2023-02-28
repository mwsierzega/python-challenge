# open csv files

import os
import csv

#variables
total_ballots = 0
fullcandidate_list = []
candidate_list = []
percent_Charles = 0
total_Charles = 0
counter_Charles = []
percent_Diana = 0
total_Diana = 0
counter_Diana = []
percent_Raymon = 0
total_Raymon = 0
counter_Raymon = []
all_total_votes = []

#read csv file
csvpath = os.path.join('Resources', 'election_data.csv') 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

#skip header
    csv_header = next(csvreader)

# Note to self, possible options to open csv files: 
# csvpath = os.path.join(r"./Resources/election_data.csv",'rt')
# csvpath = os.path.join("./Resources/election_data.csv")
# with open("election_data.csv") as csvfile:
    #csvreader = csv.reader(csvfile)
    
    
    for row in csvreader:
            total_ballots = total_ballots + 1
            
            #candidate column into a list
            fullcandidate_list = [(row[2])]
            
            #look through candidate colum list
            for i in fullcandidate_list:
                if i not in candidate_list:
                    candidate_list.append(i)
            
            #track vote counts for each candidate
            for i in fullcandidate_list:
                if i == candidate_list[0]:
                    counter_Charles += [i]
                elif i == candidate_list[1]:
                    counter_Diana += [i]
                elif i == candidate_list[2]:
                    counter_Raymon += [i]
            
            #initialize total vote counts with len function for each candidate    
            total_Charles = len(counter_Charles)
            percent_Charles = round((total_Charles/total_ballots)*100, 3)
            
            total_Diana = len(counter_Diana)
            percent_Diana = round((total_Diana/total_ballots)*100, 3)
            
            total_Raymon = len(counter_Raymon)
            percent_Raymon = round((total_Raymon/total_ballots)*100, 3)

            # find winner of election
            all_total_votes = [total_Charles] + [total_Diana] + [total_Raymon]
            winner_value = max(total_Charles, total_Diana, total_Raymon)

            for i in range(len(all_total_votes)):
                if all_total_votes[i] == winner_value:
                    winner = candidate_list[i]
       
#print analysis
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_ballots}")
print("-------------------------")
print(f"{candidate_list[0]}: {percent_Charles}% ({total_Charles})")
print(f"{candidate_list[1]}: {percent_Diana}% ({total_Diana})")
print(f"{candidate_list[2]}: {percent_Raymon}% ({total_Raymon})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")