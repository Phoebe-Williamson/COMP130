##
# A file for lab 1
#
'''
#Q1
import math
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))
SA = 2*(length*width+width*height+height*length)
print(f"The surface area of the cuboid is: {SA:.2f}")

#Q2
radians = int(input("Enter an integer value in radians: "))
rad_to_deg = round(radians * 57.2958)
print(f"The equivalent value in degrees is: {rad_to_deg}")

#Q3
full_name = str(input("Enter your full name: "))
first, last = full_name.split(" ")
inital = first[0]
length = len(inital + ". " + last)
equal_signs = "=" * length
print(f"{equal_signs}\n{inital}. {last}\n{equal_signs}")

#Q4
import math
def get_largest_prime_factor(number):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    largest_prime = 0
    for numbers in primes:
        print(numbers)
        if number/numbers == round(number/numbers):
            largest_prime = number/numbers
    return largest_prime

print(get_largest_prime_factor(55))
print(get_largest_prime_factor(42))
'''
#Q5
def square_odds(numbers_list):
    for number in numbers_list:
        if number %2 != 0:
            numbers_list[number] = number^2

numbers_list = [1, 5, 12, 6, 7]
print(numbers_list)
square_odds(numbers_list)
print(numbers_list)































