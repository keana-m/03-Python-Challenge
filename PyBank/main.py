import os
import csv

os.chdir(os.path.dirname(os.path.abspath(__file__)))
pybank_csv = os.path.join(".", "Resources", "budget_data.csv")

date = []
profit_loss = []

with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:

        date.append(row[0])
        profit_loss.append(int(row[1]))

    profit_change = []
    for x in range(1, len(profit_loss)):

        profit_change.append(int(profit_loss[x] - int(profit_loss[x-1])))
    
    avg_profit_loss = round(sum(profit_change)/len(profit_change),2)            
        
    max_profit = max(profit_change)
    min_profit = min(profit_change)

    max_index = profit_change.index(max_profit)
    min_index = profit_change.index(min_profit)
    
    max_month = date[max_index + 1]
    min_month = date[min_index + 1]

    print(f"Total Months: {len(date)}")
    print(f"Total: ${sum(profit_loss)}")
    print(f"Average Change: ${avg_profit_loss}")
    print(f"Greatest Increase in Profits: {max_month} {max_profit}")
    print(f"Greatest Decrease in Profits: {min_month} {min_profit}")

output_path = os.path.join(".", "Analysis", "financial_analysis.txt")
with open(output_path, 'w') as csvwriter:

    csvwriter.write("```text\n")
    csvwriter.write("Financial Analysis\n")
    csvwriter.write("----------------------------\n")
    csvwriter.write(f"Total Months: {len(date)}\n")
    csvwriter.write(f"Total: ${sum(profit_loss)}\n")
    csvwriter.write(f"Average Change: ${avg_profit_loss}\n")
    csvwriter.write(f"Greatest Increase in Profits: {max_month} {max_profit}\n")
    csvwriter.write(f"Greatest Decrease in Profits: {min_month} {min_profit}\n")
    csvwriter.write("```\n")