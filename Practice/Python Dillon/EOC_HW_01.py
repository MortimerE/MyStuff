# importing the math package
import math

my_name = "Mort"
my_age = 23 
mybase = 420
mypow = 69

print(my_name, my_age)

def print_my_info(name,age):
    print(name, age)

def raise_to_the_power(base, exponent):
    return base**exponent

def raise_to_the_pow(base, exponent):
    print(pow(base, exponent))

def raise_to_the_mathdotpow(base, exponent): 
    print(math.pow(base, exponent))

def raise_to_the_loop_power(base, exponent):
    result = base
    i = 1
    while i<exponent:
        result *= base
        i += 1
    print(result)

print_my_info("Andre", 3000)
print_my_info("Nice", 69)
print_my_info("Blazeit", 420)
print("Base = 420 power = 69")
print(raise_to_the_power(mybase,mypow))
raise_to_the_pow(mybase,mypow)
raise_to_the_mathdotpow(mybase,mypow)
raise_to_the_loop_power(mybase,mypow)

