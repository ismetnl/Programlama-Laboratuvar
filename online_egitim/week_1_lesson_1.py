import random


def get_n_random_numbers(n=10,min_=-5,max_=5):

    numbers = []

    for i in range(n):
        numbers.append(random.randint(min_,max_))
    return numbers


list = sorted(get_n_random_numbers())


def my_frequency_with_dict(list):

    frequency_dict = {}    # dict() = {}

    for item in list:
        if (item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1

    return frequency_dict



def my_frequency_with_list_of_tuples(list):

    frequency_list = []

    for i in range(len(list)):

        s = False

        for j in range(len(frequency_list)):

            if (list[i] == frequency_list[j][0]):
                frequency_list[j][1] +=1
                s = True
                break

        if(s == False):
            frequency_list.append([list[i],1])

    return frequency_list
"""
print("list : {}".format(list))
print("Dictionary histogram: {}".format(my_frequency_with_dict(list)))
print("Tuple histogram: {}".format(my_frequency_with_list_of_tuples(list)))
"""


