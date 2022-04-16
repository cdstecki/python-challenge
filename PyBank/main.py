import os
import csv

csvpath = os.path.join('C:\\Users\\User\\Desktop\\git-repos\\python-challenge\\PyBank\\Resources\\budget_data.csv')


total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_change = 0
profit_loss_change_list = []
month_change = []
greatest_increase = 0
greatest_decrease = 9999999999999999

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)

with open(csvpath) as csvfile:
   reader = csv.DictReader(csvfile)

   # loop through the data
   index=0
   for row in reader:
       if(index==0):
           total_months+=1
           total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
           previous_profit_loss = int(row["Profit/Losses"])
           month_change = month_change + [row["Date"]]
           index+=1
           continue

       # The total number of months 
       total_months = total_months + 1
       total_profit_loss = total_profit_loss + int(row["Profit/Losses"])
       profit_loss_change = int(row["Profit/Losses"]) - previous_profit_loss
       profit_loss_change_list.append(profit_loss_change)
       previous_profit_loss = int(row["Profit/Losses"])
       month_change = month_change + [row["Date"]]
      
   greatestDecrease=min(profit_loss_change_list)
   greatestIncrease=max(profit_loss_change_list)
   greatestDecrease_month=profit_loss_change_list.index(greatestDecrease)+1
   greatestIncrease_month=profit_loss_change_list.index(greatestIncrease)+1

# Print Financial Analysis
   print("Financial Analysis")
   print("--------------------------------")
   print(f"Total Months: {total_months}")
   print(f"Total Profit/Losess: ${total_profit_loss}")
   print(f"Average Change: ${round(sum(profit_loss_change_list)/len(profit_loss_change_list),2)}")
   print(f"Greatest increase in Profits: {month_change[greatestIncrease_month]} (${(str(greatestIncrease))})")
   print(f"Greatest decrease in Profits: {month_change[greatestDecrease_month]} (${(str(greatestDecrease))})")