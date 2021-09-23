import csv
csv_file = csv.reader(open('demo.csv','r', encoding= 'UTF-8'))#demo - name, r - read only, encoding - 

for row in csv_file:
    print(row)
    print(row[0])

with open('dmo.csv', 'r', encoding = 'UTF-8') as csv_file:
    for row in csv_file:
        print(row)

def some_method(a,b,c,d):
    pass
some_method(1,2,3,5)
some_method(a = 1, b = 2, d = 3, c = 4)