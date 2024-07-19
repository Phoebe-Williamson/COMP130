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
def get_largest_prime_factor(number):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    #largest_prime = 0
    for i in range(len(primes) -1, -1, -1):
        if number%primes[i] == 0:
            largest_prime = primes[i]
            return largest_prime

print(get_largest_prime_factor(55))
print(get_largest_prime_factor(42))

#Q5
def square_odds(numbers_list):
    for i in range(len(numbers_list) -1, -1, -1):
        if numbers_list[i] %2 != 0:
            new_value = numbers_list[i]**2
            numbers_list[i] = new_value

numbers_list = [1, 5, 12, 6, 7]
print(numbers_list)
square_odds(numbers_list)
print(numbers_list)

#Q7
def read_school_census_data(filename):
    input_file = open(filename, 'r')
    lines = input_file.read().split("\n")
    input_file.close()
    tuple_list = []
    for line in lines:
        values = line.split(",")
        eye = values[0]
        height = int(values[1])
        left = int(values[2])
        right = int(values[3])
        new_tuple = eye, height, left, right
        tuple_list.append(new_tuple)
    return tuple_list
    
data = read_school_census_data('data.txt')
print(data)
print(type(data))
print(type(data[0][0]), type(data[0][1]), type(data[0][2]), type(data[0][3]))

#Q8
def create_dictionary(numbers):
    new_dict = {}
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for number in numbers:
        smallest_prime = get_smallest_prime_factor(number)
        if smallest_prime in new_dict:
            new_dict[smallest_prime].append(number)
        else:
            new_dict[smallest_prime] = [number]
    return new_dict

def get_smallest_prime_factor(number):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
    for prime_number in prime_numbers:
        if number % prime_number == 0:
            return prime_number
    return -1

numbers_dictionary = create_dictionary([76, 237, 20, 560, 924])
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])
values = [76, 237, 20, 560, 924, 351, 561, 133, 102, 147, 415, 126, 121, 780, 17, 1273, 64, 12]
numbers_dictionary = create_dictionary(values)
for key in sorted(numbers_dictionary.keys()):
    print(key, numbers_dictionary[key])

#Q9
def print_table(days_per_month, column_width=15):
    print(f"{'Month Days':>{column_width + 5}}")
    print("-" * column_width + "-----")
    for month, days in days_per_month.items():
        print(f"{month:>{column_width}} {days}")

days_per_month = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}
print_table(days_per_month)	
print_table(days_per_month, 20)

#Q10

#Q11
integer = int(input("Enter an integer between 1 and 9: "))
while (integer < 1) or (integer > 9):
    integer = int(input("Enter an integer between 1 and 9: "))
print("EVEN" if integer %2 == 0 else "ODD")
'''
#Q12
def create_words_list(word):
    return[word[i:] for i in range(len(word))]

word = create_words_list('case')
print(word)
print(create_words_list('cat'))
'''
#Q13
def get_sum_last_digits(usernames):
    x=0
    for name in usernames:
        x += int(name[-1])
    return x

names = ['abal412', 'oabc399', 'oyi001']
print(get_sum_last_digits(names))
data = ['Akim161', 'mgra734', 'dng004', 'bcar035']
print(get_sum_last_digits(data))
'''












