import os
import csv

csv_path = os.path.join('.', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')
with open(csv_path, "r") as file:
   
    data = csv.reader(file)
    
    header = next(data)
    row = list(data)

lists = list(zip(*row))
months = lists[0]
profit = [int(x) for x in lists[1]]
net_change = [int(profit[k] - profit[k - 1]) for k in range(1, len(profit))]
num_month = len(row)
total = sum(profit)
avg_change = sum(net_change) / len(net_change) 
max_increase = row[net_change.index(max(net_change))]
max_decrease = row[net_change.index(min(net_change))] 

output = ("Financial Analysis: \n" +
        "========================== \n"
        f"Total Months: {num_month}\n" +
        f"Total: ${total}\n" +
        f"Average Change: ${round(avg_change, 2)}\n" +
        f"Greatest Increase in Profits: {max_increase[0]} (${max(net_change)})\n" +
        f"Greatest Decrease in Profits: {max_decrease[0]} (${min(net_change)})")

print(output)

with open("results.txt", "w", newline = "") as results:
    results.write(output)