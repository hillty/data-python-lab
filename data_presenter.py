#step 2:
open_file = open('CupcakeInvoices.csv')

#step 3:
# for row in open_file:
#     print(row)
#step 4:
# for row in open_file:
#   values = row.split(',')
#   print(values[2])
#step 5:
# for row in open_file:
#     values = row.split(',')
#     total = int(values[3]) * float(values[4])
#     print(total)
#step 6:
total = 0

for row in open_file:
    values = row.split(',')
    total = total + (int(values[3]) * float(values[4]))

print(total)
#step 7
open_file.close()