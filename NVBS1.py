from csv import reader 
if __name__ == '__main__':
    publick = []

with open('books-en.csv','r') as csvfile:
    a = reader(csvfile, delimiter = ';')
    for raw in a:
        publick.append(raw[4])

publick = set(publick)
sx = list(publick)
Rejuntat = sorted(sx)


print(Rejuntat)