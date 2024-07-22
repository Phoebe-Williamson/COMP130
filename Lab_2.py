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
'''
#Q6
def print_title():
    banner = "Average Rainfall, temperature and sunshine data for selected locations throughout NZ"
    print(f"{banner}\n" + "=" * len(banner))































    
