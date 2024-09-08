# Factorial generator

def factorial_generator(num):
    i = 1
    product = 1
    while (i <= num) :
        product = product * i
        i += 1
    return product

print(factorial_generator(5))


def add(num1,num2) :
    return num1 + num2

print(add(100,43))


def subs(num1,num2) :
    return num1 - num2

print(subs(100,43))

