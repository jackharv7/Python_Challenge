import os
import csv

#identify variables
months = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
total_diff = 0
avg_diff = 0

os.chdir(os.path.dirname(os.path.abspath(__file__)))
#find the file
csvpath = os.path.join("..", "PyBank", "budget_data.csv")
#open the file
with open("budget_data.csv") as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile, None)
    #find header
    #create a list
    lst = []
    #add data to list/identify datatype
    for row in csvreader:
        lst.append([row[0], int(row[1])])  
        #account for number of months
        months += 1
        #total profit of all profit/loss
        total += int(row[1])

    #find the difference between profit and losses
    
    #make a new list for differences
    diff = [[lst[i + 1][0], lst[i+1][1] - lst[i][1]] for i in range(len(lst)-1)]
    for r in diff:
        total_diff += (r[1])
    #find the average difference of the differences(one less month due to difference between months)
    avg_diff = total_diff/(months-1)
    #sort by proft, not date
    diff.sort(key = lambda x: x[1])
    #last input in sorted list
    greatest_increase = diff[-1]
    #first input in sorted list
    greatest_decrease = diff[0]

text_summary = """
    Financial Analysis
-----------------------------
Total Months: {months}
Total: ${total}
Average Change = ${avg_diff:.2f}
Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})
Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})
""".format(months=months, greatest_increase=greatest_increase, greatest_decrease=greatest_decrease, avg_diff=avg_diff, total=total)

# write results to output line
print(text_summary)
#write results to a new file
with open('summary.txt', 'w') as outfile:
    outfile.write(text_summary)