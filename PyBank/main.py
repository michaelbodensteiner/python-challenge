import os
import csv

csv_path = os.path.join('.', 'python-challenge', 'PyBank', 'Resources', 'budget_data.csv')

with open(csv_path, "r") as file:
    budgetdata = csv.reader(file)
    header = next(budgetdata)
    row = list(budgetdata)

