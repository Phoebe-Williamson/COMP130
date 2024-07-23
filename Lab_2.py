##
# A file for lab 2
# Author: Phoebe Williamson
# Date (22/7/24)
#
'''
#Q1
def read_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.read().split("\n")
    input_file.close()
    return lines


data = read_file("regions.txt")
print(data)
print(type(data))
print(type(data[0]))
print(type(data[0][0]), type(data[0][1]), type(data[0][1][0]))

#Q2
def get_numbers_list(data):
    return [float(num) for num in data.split(",")]

line1 = '73.3,66.1, 87.3, 99.4, 112.6, 126.4, 145.1, 118.4, 105.1, 100.2, 85.8, 92.8'
line2 = '76.3, 68.7, 79.4, 80.3, 99.7, 113.2, 118.2, 103.4, 91.5, 91.9, 85.0, 100.7'
list1 = get_numbers_list(line1)
print(list1)
print(get_numbers_list(line2))
print(type(list1[0]))

#Q3
def read_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.read().split("\n")
    input_file.close()
    return lines
    
def get_numbers_list(data):
    return [float(num) for num in data.split(",")]
    
def create_dictionary(filename):
    lines = read_file(filename)
    dictionary = {}
    for line in lines:
        region, numbers = line.split(":")
        dictionary[region] = get_numbers_list(numbers)
    return dictionary

data_dict = create_dictionary('rainfall.txt')
for key in sorted(data_dict):
    print(key, data_dict [key])

#Q4
def create_regions_dictionary(regions_list):
    new_dict = {}
    for region in regions_list:
        new_dict[region] = []
    return new_dict

data = ['Auckland', 'Hamilton']
a_dict = create_regions_dictionary(data)
for key in sorted(a_dict):
    print(key, a_dict[key])

#Q5
def merge_data(regions_dict, data_dict):
    for region in regions_dict:
        if region in data_dict:
            average = sum(data_dict[region])/len(data_dict[region])
            regions_dict[region].append(round(average, 2))
    return regions_dict

regions_dict = {'Auckland':[93.24], 'Hamilton':[] }
data_dict = {'Auckland': [16.2, 16.6, 14.2, 12.2, 10.8, 8.2, 7.2, 8.2, 9.2, 11]}
merge_data(regions_dict, data_dict)
for key in sorted(regions_dict):
    print(key, regions_dict[key])

#Q6
def print_title():
    banner = "Average Rainfall, temperature and sunshine data for selected locations throughout NZ"
    print(f"{banner}\n" + "=" * len(banner))
 
#Q7
def print_table(regions_dict, column_names):
    text = "Name"
    print(f"{text:>16}", end="|")
    for column in column_names:
        print(f"{column:>16}", end="|")
    print()
    for key in sorted(regions_dict):
        print(f"{key:>16}", end="|")
        numbers = regions_dict[key]
        rain = round(numbers[0], 2)
        temp = round(numbers[1], 2)
        print(f"{rain:>16}", end="|")
        print(f"{temp:>16}", end="|")
        print()

regions_dict = {'Kaitaia': [110.0, 11.766666666666666], 'Auckland': [93.24166666666667, 12.058333333333335], 'Tauranga': [100.125, 10.841666666666667]}
print_table(regions_dict, ['Rainfall(mm)', 'Min.Temperature'])
'''
def main():
    #Complete the main() function 
    print_title()
    regions_filename = input("Enter a filename for reading regions: ")
    regions_list = read_file(regions_filename)
    regions_dict = create_regions_dictionary(regions_list)
    rainfall_filename = input("Enter a filename for reading rainfall data: ")
    rainfall_dict = create_dictionary(rainfall_filename)
    merge_data(regions_dict, rainfall_dict)
    min_temp_filename = input("Enter a filename for reading minimum temperature data: ")
    min_temp_dict = create_dictionary(min_temp_filename)
    merge_data(regions_dict, min_temp_dict)
    max_temp_filename = input("Enter a filename for reading maximum temperature data: ")
    max_temp_dict = create_dictionary(max_temp_filename)
    merge_data(regions_dict, max_temp_dict)
    sunshine_filename = input("Enter a filename for reading sunshine data: ")
    sunshine_dict = create_dictionary(sunshine_filename)
    merge_data(regions_dict, sunshine_dict)
    print_table(regions_dict, ['Rainfall(mm)', 'Min.Temperature', 'Max.Temperature', 'Sunshine(hr)'])
        
#Copy all your functions in here
def print_title():
    banner = "Average Rainfall, temperature and sunshine data for selected locations throughout NZ"
    print(f"{banner}\n" + "=" * len(banner))

def read_file(filename):
    input_file = open(filename, 'r')
    lines = input_file.read().split("\n")
    input_file.close()
    return lines

def create_regions_dictionary(regions_list):
    new_dict = {}
    for region in regions_list:
        new_dict[region] = []
    return new_dict

def create_dictionary(filename):
    f = open(filename, 'r')
    d = {}
    content = f.read().split('\n')
    for line in content:
        name, num = line.split(":")
        numbers = num.split(',')
        d[name] = [float(x) for x in numbers]
    return d

def merge_data(regions_dict, data_dict):
    for region in data_dict:
        average = sum(data_dict[region])/len(data_dict[region])
        regions_dict[region].append(round(average, 2))
    
    
def print_table(regions_dict, column_names):
    text = "Name"
    print(f"{text:>16}", end="|")
    for column in column_names:
        print(f"{column:>16}", end="|")
    print()
    for region, columns in sorted(regions_dict.items()):
        print(f"{region:>16}", end="|")
        for column_name in columns:
            print(f"{column_name:>16.2f}", end="|")
        print()

















    
