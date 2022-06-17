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