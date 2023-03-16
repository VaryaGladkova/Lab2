import csv


def color(code):
    return f'\u001b[{code}m'


YELLOW = color(43)
BLUE = color(44)
WHITE = color(47)
GREEN = color(42)
RED = color(41)
END = color(0)


# Сгенерировать при помощи escape-символов в консоли изображение флага 3 варианта

for i in range(1, 3):
    print(RED + ' ' * 36 + END)

for i in range(1, 3):
    print(WHITE + ' ' * 36 + END)

for i in range(1, 3):
    print(BLUE + ' ' * 36 + END)

print()


for i in range(1):
    print(WHITE + ' ' * (1 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (20 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (20 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (1 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (3 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (15 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (2 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (15 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (3 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (5 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (8 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (5 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (8 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (4 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (14 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (4 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (8 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (10 - 2 * i) + YELLOW + '  ' * (4 + 2 * i)
          + WHITE + ' ' * (18 - 2 * i) + YELLOW + '  ' * (4 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (8 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (4 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (14 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (4 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (8 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (5 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (8 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (10 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (5 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (3 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (15 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (2 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (15 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (3 - 2 * i) + END)

for i in range(1):
    print(WHITE + ' ' * (1 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (20 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (20 - 2 * i) + YELLOW + '  ' * (2 + 2 * i)
          + WHITE + ' ' * (1 - 2 * i) + END)

print()

for i in range(9, 0, -1):
    print(WHITE + str(i) + WHITE + ' ' * 2 * i + GREEN + ' ' * (i // i)
          + WHITE + ' ' * (36 - 2 * i) + END)

print(WHITE + '0    1   2   3   4   5   6   7   8   9' + END, '\n')

print()

count_2016 = 0
count_before2016 = 0

with open('books.csv') as csvfile:
    books = csv.reader(csvfile, delimiter=';')
    title = csvfile.readline()
    for row in books:

        if  str(row[6])[6:10] >= "2016":
            count_before2016 += 1
        else:
            count_2016 += 1

books_before2016 = int((count_2016 / (count_2016 + count_before2016)) * 100)
books_after2016 = 100 - books_before2016

print(f'Книги до 2016 года:{GREEN + " " * books_before2016 + WHITE + str(books_before2016) + END} %', '\n')
print(f'Книги после 2016 года: {GREEN + " " * books_after2016 + WHITE + str(books_after2016) + END} %')
