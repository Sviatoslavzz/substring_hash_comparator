option = int(input("Введите 1 для ввода данных из консоли / Введите 2 для ввода данных из файла\n"))
array = []
if option == 1:
    s = input("Введите строку: ")
    q = int(input())

    for i in range(q):
        array.append([int(i) for i in input().split()])
else:
    path = input("Введите путь к файлу: ")
    with open(path, "r") as file:
        s = file.readline().strip()
        q = int(file.readline().strip())
        for i in range(q):
            array.append([int(i) for i in file.readline().strip().split()])

x = 257
p = 10 ** 9 + 7
h = [0]
x_list = [0]
res = 0
mul_x = 1
n = len(s)
for i in range(n):
    res = ((res * x) + ord(s[i])) % p
    h.append(res)
    mul_x = (mul_x * x) % p
    x_list.append(mul_x)


def string_compare(len_sub, start_1, start_2):
    return (h[start_1 + len_sub] + h[start_2] * x_list[len_sub]) % p == (
            h[start_2 + len_sub] + h[start_1] * x_list[len_sub]) % p


for i in range(q):
    if string_compare(array[i][0], array[i][1], array[i][2]):
        print("yes")
    else:
        print("no")
