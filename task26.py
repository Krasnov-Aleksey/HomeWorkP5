'''
Напишите программу, которая на вход принимает
два числа A и B, и возводит число А в целую степень B с
помощью рекурсии.
A = 3; B = 5 -> 243 (3⁵)
A = 2; B = 3 -> 8
'''
def square_number(num,sq):
    if sq==1:
        return num
    return num*(square_number(num,sq-1))

num=int(input('Введите число '))
sq=int(input('Введите степень '))

print (square_number(num,sq))