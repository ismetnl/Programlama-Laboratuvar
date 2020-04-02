from week_1_lesson_1 import get_n_random_numbers
from week_1_lesson_1 import my_frequency_with_list_of_tuples
from week_1_lesson_1 import my_frequency_with_dict


my_list_1 = get_n_random_numbers(10)
my_hist_d = my_frequency_with_dict(my_list_1)
my_hist_t = my_frequency_with_list_of_tuples(my_list_1)


def my_mode_with_dict(my_hist_d): #sözlükte bulunan en büyük frekans değerini ve ona ait key'i döndürür

    frequency_max =-1
    mode =-1

    for key in my_hist_d:
        #print(key,my_hist_d[key])
        if my_hist_d[key] > frequency_max:
            frequency_max = my_hist_d[key]
            mode = key

    return mode,frequency_max

print("dict: {}".format(my_hist_d))
print("mode dict : {}".format(my_mode_with_dict(my_hist_d)))


def my_mode_with_list_of_tuples(my_hist_t):

    frequency_max = -1
    mode = -1

    for item,frequency in my_hist_t:
        #print(mode,frequency_max)
        if(frequency > frequency_max):
            frequency_max = frequency
            mode = item

    return mode,frequency_max

print("mode tuple list : {}".format(my_mode_with_list_of_tuples(my_hist_t)))