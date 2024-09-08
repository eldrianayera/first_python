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
    return abs(num1 - num2)

print(subs(100,43))


def mul(num1,num2) :
    return num1 * num2

print(mul(100,43))


def div(num1,num2) :
    return num1 / num2

print(div(100,43))



def odd_even(num) :
    if num % 2 == 0 :
        return 'even'
    else :
        return 'odd'
    
print(odd_even(212))
print(odd_even(92738))
print(odd_even(433))
print(odd_even(23735))
