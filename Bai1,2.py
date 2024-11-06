from csv import reader

if __name__ == "__main__":
    count = 0


    with open('books-en.csv', 'r') as csvfile1:
        table = reader(csvfile1, delimiter=';')
        for row in table:
            if len(row[1]) >= 30:
                count+=1 

    print(count)





from csv import reader

if __name__ == "__main__":
    author = input("Введите автора ")
    storage = []

    with open('books-en.csv', 'r') as csvfile2:
        table = reader(csvfile2, delimiter=';')
        for row in table:
            if author in row[2] and  int(row[6]) >=200:
                    storage.append(f'ID:{row[0]};Название: {row[1]};Дата поступления: {row[3]};Price:{row[6]} \n')

    if len(storage)!=0:
        print('У этого автора для выдачи доступны: \n', *storage)
    else:
        print('Для выдачи недоступны книги этого автора')



