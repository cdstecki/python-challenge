import os
import csv

csvpath = os.path.join('C:\\Users\\User\\Desktop\\git-repos\\python-challenge\\PyBank\\Resources\\budget_data.csv')
txtpath = os.path.join('C:\\Users\\User\\Desktop\\git-repos\\python-challenge\\PyBank\\Analysis\\Analysis.txt')

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
      
   greatest_decrease=min(profit_loss_change_list)
   greatest_increase=max(profit_loss_change_list)
   greatest_decrease_month=profit_loss_change_list.index(greatest_decrease)+1
   greatest_increase_month=profit_loss_change_list.index(greatest_increase)+1

# Financial Analysis Summary
summary = (
   f"\nFinancial Analysis\n"
   f"--------------------------------\n"
   f"Total Months: {total_months}\n"
   f"Total Profit/Losess: ${total_profit_loss}\n"
   f"Average Change: ${round(sum(profit_loss_change_list)/len(profit_loss_change_list),2)}\n"
   f"Greatest increase in Profits: {month_change[greatest_increase_month]} (${(str(greatest_increase))})\n"
   f"Greatest decrease in Profits: {month_change[greatest_decrease_month]} (${(str(greatest_decrease))})\n"
)

# Print Financial Analysis Summary
print(summary)

# Export Analysis to text file
with open(txtpath, "w") as txt_file:
    txt_file.write(summary)
