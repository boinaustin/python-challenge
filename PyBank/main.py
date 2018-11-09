import csv
import os
budget_data = '/Users/bokim/UTAUS201810DATA2/Python/Homework/Instructions/PyBank/Resources/budget_data.csv'

with open(budget_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    rows = []
    pl =[]
    total_amount_pl = 0
    
    for i, row in enumerate(csvreader):
        if i == 0:
            header = row
        else:
            rows.append(row)
            pl.append(int(row[1]))
            
            total_amount_pl = total_amount_pl + int(row[1])
    

                          
                        
total_months = len(rows)  
avg_change = total_amount_pl / total_months
                          
print("Total months: " + str(total_months))
print("Total amount of pl: " + str(total_amount_pl))
print("Average Change: " + str(avg_change))

greatest_increase = max(pl)
greatest_decrease = min(pl)


date1 = rows[0][0]
date2 = rows[0][0]
for x in rows:
    if x[1] == str(greatest_increase):
        date1 = x[0]
    elif x[1] == str(greatest_decrease):
        date2 = x[0]
print("Date: " + str(date1) + " The greatest increase: " + str(greatest_increase))
print("Date: " + str(date2) + " The greatest decrease: " + str(greatest_decrease))


with open("budgetAssign.txt", 'w') as csvfile:
     csvwriter = csv.writer(csvfile, delimiter=',')
     csvwriter.writerow(['Total Month', 'Total P/L', 'Average Change', 'Greatest Increase Date & Value', 'Greastest Decrease Date & Value' ])
     csvwriter.writerow([total_months, total_amount_pl, avg_change, str(greatest_increase) + date1 , str(greatest_decrease) + date2])