#Your analysis should align with the following results:

#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)

# starting code generation

# import csv files

import os
import csv


file_read = os.path.join('Resources', 'budget_data.csv')

# results file name
file_write = os.path.join('Analysis', 'budget_analysis.txt')

#variable for total number of months included in the dataset

total_months = 0

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
profit_loss = 0
month_change = []
list_change = []
average_change = 0

#The net total amount of "Profit/Losses" over the entire period
total_net = 0

#The greatest increase in profits (date and amount) over the entire period
greatest_increase = ['',0]

#The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = ['',999999999999999999999]

# open the csv file

with open(file_read, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csvheader = next(csvreader)
    
    first_row = next(csvreader)
    total_months += 1
    total_net = int(first_row[1])
    previous_month = int(first_row[1])
    
#read file header, read rows

for row in csvreader:
    total_months += 1
    total_net += int(row[1])
    
#calculate profit/loss changes over the entire period

list_change = int(row[1])-profit_loss
profit_loss = int(row[1])
list_change = list_change/total_months
month_change += list_change

# use if statement to calculate greatest increase in profits

if list_change > greatest_increase[1]:
    greatest_increase[1] = list_change
    
# use if statement to calculate greatest decrease in profits
if list_change < greatest_decrease[1]:
    greatest_decrease[1] = list_change
    
# use if statement to calculate average change
average_change = sum(month_change)/len(month_change)

#create output file
output_file = open(file_write, 'w')

print(output_file)

with open(file_write, 'a') as output_file:
    output_file.write('output')
