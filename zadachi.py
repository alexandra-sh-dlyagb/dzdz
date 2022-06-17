# 1. Найдите НОК двух чисел
# я рещила использовать алгоритм евклида, чтобы найти НОД, а потом через НОД - НОК
A = int(input('Введите число А => '))
B = int(input('Введите число B => '))
mult = A*B
while A!=0 and B!=0:
    if A>B:
        A = A%B
    else:
        B = B%A
NOD = A+B
#НОД через НОК можно найти по формуле a*b/НОД(a, b)
#произведение мы нашли заранее. это у нас mult
NOK = mult/NOD
print (int (NOK))



# 2. Найти число Пи с заданной точностью d
import math
length_pi = int(input('Введите количество знаков после запятой => '))
pi = math.pi #радостно нашла число пи)))))
value_answer = round(pi, length_pi) #округлила
print (value_answer)



# 3. Составить список простых множителей натурального числа N
N = int (input("Введите число N => "))
answer_array = []
delitel = 2
while N!=1:
    if N%delitel ==0 :
        answer_array.append(delitel)
        N = N/delitel
    else:
        delitel = delitel+1
print (answer_array)



# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
#нашла козырный вариант. реально ооочень удобно
input_array = [2, 1, 24, 2, 56, 2, 24]
new_array = set(input_array)
print (new_array)



# 5. Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа
path = 'file.txt'
data = open(path, 'w')
for line in data:
    if int(line)%2==0:
        data.writelines (line)