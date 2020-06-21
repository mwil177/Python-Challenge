import os
import csv 

#Path
csvpath = os.path.join('pybank.csv')


#Open & Read
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    
    #Variables
    month = []
    revenue = []
    revenue_change = []
    monthly_change = []
    
    #Print Header
    print(f"Header: {csv_header}")

   
    #Read Thru Data Following Header
    for row in csvreader:
    
    #Total Months in DataSet
       revenue.append(row[1])
       month.append(row[0])
    print(len(month))
    
    #Rev
    revenue_int = map(int,revenue)
    total_revenue = (sum(revenue_int))
    print(total_revenue)

    #Delta
    t = 0
    for t in range(len(revenue) - 1):
        profit_loss = int(revenue[t +1]) - int(revenue[t])
        revenue_change.append(profit_loss)
    Total = sum(revenue_change)
    monthly_change = Total / len(revenue_change)
    print(monthly_change)

    #Greatest Profits Inc.
    profit_increase = max(revenue_change)
    print(profit_increase)
    p = revenue_change.index(profit_increase)
    month_increase = month[p+1]

    #Greatest Losses Decr.
    profit_decrease = min(revenue_change)
    print(profit_decrease)
    l = revenue_change.index(profit_decrease)
    month_decrease = month[l+1]


#Print Commands
print(f'Banking Analysis')
print(f'-----------------------')
print("Total Months: " + str(len(month)))
print(f"Greatest Increase in Profits: {month_increase} (${profit_increase})")
print(f"Greatest Decrease in Profits: {month_decrease} (${profit_decrease})")
