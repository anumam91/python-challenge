import csv
print ("Financial Analysis")
print ("---------------------------")

month_count = 0
value_list = []
diff_list = []
month_list = []

file_path = "C:/users/Anum Ali/Desktop/budget_data.csv"
with open(file_path) as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)
    
    #The number of months is equal to the number of rows in the dataset. 
    #To count the number of rows:
    for (row) in csvreader:
        if ((int(row[1])) > 1 or (int(row[1])<1)):
            month_count = month_count + 1 

    #To get the sum of all of the values in a column, use for loop . . .
    #. . . to add each value to a list, then take the sum of the list
            value_list.append(int(row[1]))
            month_list.append(str(row[0]))

#Avg change in "Profit/Losses" between months over the entire period
for x in range(len(value_list)):
    n = value_list[x]
    m = value_list [x-1]
    difference = (n-m)
    diff_list.append(difference)

diff_list.pop(0)
average = sum(diff_list) / len(diff_list)

great_dec = min(diff_list)
great_inc = max(diff_list)

#Figure out which month is associated with greatest dec using index 
dec_index = diff_list.index(min(diff_list))
dec_month = month_list[int(dec_index + 1)]

#Figure out which month is associated with greatest inc using index
inc_index = diff_list.index(max(diff_list))
inc_month = month_list[int(inc_index + 1)]

#Print everything!
print (f'Total number of months: {month_count}')
print (f'Total: ${sum(value_list)}')
print(f'Average Change: ${average}')
print(f'Greatest Increase in Profits: {inc_month} (${great_inc})')
print(f'Greatest Decrease in Profits: {dec_month} (${great_dec})')
    
