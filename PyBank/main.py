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
header_line = []

#open results
with open (data_file_path,"r") as budget:
    #read results
    budget_reader=csv.reader(budget)
    for entry in budget_reader:
        if (budget_reader.line_num ==1):
            header_line = entry
        else:
            #set categores for vote based on header_line
            date = entry [0]
            profit_losses = entry [1]

            total_months +=1
            total_amount += float(profit_losses)

#print results in terminal
print ("")
print ("Financial Analysis")
print ("----------------------------")
print ("")
print (f'Total Months: {total_months}')
print ("")
print (f'Total: ${total_amount}')
print ("")

#export results to text file



#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)