# Factorial generator

def factorial_generator(num):
    i = 1
    product = 1
    while (i <= num) :
        product = product * i
        i += 1
    return product

print(factorial_generator(5))




