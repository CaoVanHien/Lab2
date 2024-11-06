from csv import reader 
import operator

if __name__ == "__main__" :
    a=0
    Books = []

with open('books-en.csv','r') as csvfile:
    table = list(reader(csvfile, delimiter = ';'))
    data = table[1:]
    table = sorted(data, key = lambda row: int(row[5]), reverse = True) 


    for row in table:
        if a < 20:
            Books.append(f' {a+1} : {row[2]} : {row[1]} : {row[5]}')
        a +=1

    print("\n".join(Books))