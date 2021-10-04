import os
import csv

# navigate to file
PyBank = os.path.join("data", "budget_data.csv")

months = []
net_total = []

with open (PyBank, newline = "") as csvfile:
    readcsv = csv.reader(csvfile, delimiter = ',')

    csv_header = next(csvfile)
    # put the data into lists
    for row in readcsv:
        months.append(row[0])
        net_total.append(int(row[1]))

    # calculate total months
    total_months = len(months)

    # set variables for loop
    x = 1
    y = 0

    # net total amount of "Profit/Losses" over the entire period 
    # net total amount of "Profit/Losses" over the entire period, then find the average of those changes
    average_change = (net_total[1] - net_total[0])
    
    changes = []

    # for loop to calculate month to month change
    for month in range(total_months - 1):
        average_change = (net_total[x] - net_total[y])
        changes.append(int(average_change))
        x+=1
        y+=1
    # average monthly change and round it
    av_mon_change_ = round(sum(changes)/(total_months -1),2)

    # greatest increase in profits (date and amount), find the max change, return the index to find position, and find the month of the max change
    max_change = max(changes)
    max_index = changes.index(max_change)
    max_change_month = months[max_index +1]
    # greatest decrease in profits (date and amount), find the min change, return the index to find position, and find the month of the min change
    min_change = min(changes)
    min_index = changes.index(min_change)
    min_change_month = months[min_index +1]

# print the values
print("Financial Analysis")
print("-----------------------")
print(f"Months: {len(months)}")
print(f"Total: ${sum(net_total)}")
print(f"Average Monthly Change: {av_mon_change_}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

# write the output to a text file
final_analysis = open("Financial_Analysis.txt", "w")
final_analysis.write("Financial Analysis/n")
final_analysis.write("-----------------------/n")
final_analysis.write(f"Months: {len(months)}/n")
final_analysis.write(f"Total: ${sum(net_total)}/n")
final_analysis.write(f"Average Monthly Change: {av_mon_change_}/n")
final_analysis.write(f"Greatest Increase in Profits: {max_change_month} (${max_change})/n")
final_analysis.write(f"Greatest Decrease in Profits: {min_change_month} (${min_change})/n")

final_analysis.close()