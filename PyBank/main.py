# import csv files

import os
import csv


file_read = os.path.join('Resources', 'budget_data.csv')
file_write = os.path.join('Analysis', 'budget_analysis.txt')

# variables
    # total number of months included in the dataset
total_months = 0

    # changes in "Profit/Losses" over the entire period, average of those changes
profit_loss = 0
month_change = []
list_change = []
average_change = 0

    # net total amount of "Profit/Losses" over the entire period
total_net = 0

    # greatest increase in profits (date and amount) over the entire period
greatest_increase = ['',0]

    # greatest decrease in profits (date and amount) over the entire period
greatest_decrease = ['',999999999999999999999]

# open the csv file

with open(file_read, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)
    
    first_row = next(csvreader)
    total_months += 1
    total_net = int(first_row[1])
    previous_month = int(first_row[1])

for row in csvreader:
    total_months += 1
    total_net += int(row[1])
    
#calculate profit/loss changes over the entire period

list_change = int(row[1])-profit_loss
profit_loss = int(row[1])
list_change = list_change/total_months
month_change += list_change

# use if statement to calculate greatest increase in profits,  greatest decrease in profits

if list_change > greatest_increase[1]:
    greatest_increase[1] = list_change
if list_change < greatest_decrease[1]:
    greatest_decrease[1] = list_change
    
# use if statement to calculate average change
average_change = sum(month_change)/len(month_change)

#create output file
output_file = open(file_write, 'w')

print(output_file)

with open(file_write, 'a') as output_file:
    output_file.write('output') 