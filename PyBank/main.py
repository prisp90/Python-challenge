import os
import csv

filepath = os.path.join('..', "Resources", "budget_data.csv")
bank_output_path = os.path.join('..',"Analysis","bank_output.txt")

with open(filepath, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    print(f'"Header: {csv_header}')
    
    total_month = 0
    total_amount = 0
    change_month_profit_loss = 0.0
    previous_month_profit_loss = 0.0
    diff_of_each_month_revenue = []
    dictionary_new_profit_loss = {}

    for month_row in reader:
        total_month += 1
        total_amount += (float(month_row[1]))

        change_month_profit_loss = float(month_row[1]) - previous_month_profit_loss
        
        diff_of_each_month_revenue.append(change_month_profit_loss)

        previous_month_profit_loss = float(month_row[1])

        dictionary_new_profit_loss[change_month_profit_loss] = month_row[0]

           
greatest_incr_profit = 0.0
greatest_decr_losses = 0.0
new_total_profit_loss = 0.0

average_change_profit_loss = 0.0

for i in range(len(diff_of_each_month_revenue)):
    if i==0:
        greatest_incr_profit=diff_of_each_month_revenue[i]
        greatest_decr_losses=diff_of_each_month_revenue[i]            
        continue

    if diff_of_each_month_revenue[i] >= greatest_incr_profit:
        greatest_incr_profit = diff_of_each_month_revenue[i]

    if diff_of_each_month_revenue[i] <= greatest_decr_losses:
        greatest_decr_losses = diff_of_each_month_revenue[i]


    new_total_profit_loss += diff_of_each_month_revenue[i]

average_change_profit_loss = new_total_profit_loss/(total_month-1)
avg_change = round(average_change_profit_loss,2)

x = dictionary_new_profit_loss[greatest_incr_profit]

y = dictionary_new_profit_loss[greatest_decr_losses]



print('==================================================')
    
print(" Financial Analysis")

print('==================================================')

print("Total months : ", total_month)

print("Total amount : "+"$"+ str(total_amount))

print("Avgrage change : "+"$"+ str(avg_change))

print("greatest increase in profit : "+ str(x) + " " +"("+"$"+ str(greatest_incr_profit)+")")

print("greatest decrese in losses : "+ str(y) + " " +"("+ "$"+str(greatest_decr_losses)+")")



with open(bank_output_path, 'w', newline= '') as txt_output_file:

    txt_output_file.write('\n==================================================\n')

    txt_output_file.write("\n Financial Analysis \n")

    txt_output_file.write('\n==================================================\n')



    txt_output_file.write("\n"+"Total months : "+ str(total_month)+"\n")

    txt_output_file.write("\n"+"Total amount : "+"$"+ str(total_amount)+ "\n")    

    txt_output_file.write("\nAvgrage change : "+"$"+ str(avg_change)+"\n")

    txt_output_file.write("\ngreatest increase in profit : "+ str(x) + " " +"("+"$"+ str(greatest_incr_profit)+")\n")

    txt_output_file.write("\ngreatest decrese in losses : "+ str(y) + " " +"("+ "$"+str(greatest_decr_losses)+")\n")

    txt_output_file.write('\n==================================================\n')
    