from csv import reader
from random import *
if __name__=="__main__":
 output = open('Bai3.txt','w')
 a=[]
 b = 0

with open('books-en.csv','r') as csvfile3:
    table = reader(csvfile3, delimiter=';')
    for row in table:
        a.append(f'{row[2]}.{row[1]} - {row[3]} \n')

for i in range(20):
    number = randint(1, 9410)
    b +=1
    output.write(f'{b}: {a[number]}')

output.close()