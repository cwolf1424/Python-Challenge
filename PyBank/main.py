#modules
import csv

#get data file path
data_file_path = "PyBank/Resources/budget_data.csv"

#set variables
total_months = 0
total_amount = 0
average_change = 0
greatest_p_increase = 0
greatest_p_decrease = 0

#open results
with open (data_file_path,"r") as budget:
    #read results
    budget_reader=csv.reader(budget)
    for entry in budget_reader:
        print (entry)


#print results in terminal

#export results to text file


#Financial Analysis
#----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)