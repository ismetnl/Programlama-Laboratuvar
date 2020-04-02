from week_1_lesson_1 import get_n_random_numbers

my_list = [1,2,5,7,12,51,21,-4,-8,10,-2]

def my_linear_search(my_list,item_search):

    found = (-1,-1)

    for indis in range(len(my_list)):

        if my_list[indis] == item_search:

            found = (my_list[indis],indis) # bulunan sayı ve indisi tuple olarak return ediyoruz
            #break Bu şekilde yaparsak listede istediğimiz sayıyı bulduğu zaman döngü sonlanır

    return found


print(my_linear_search(my_list,21))

my_list = get_n_random_numbers(10,-50,50)
print()
def my_mean(my_list):

    s,t=0,0

    for item in my_list:

        s +=1
        t +=item

    mean_ = t/s

    return mean_

print(my_list)
print(my_mean(my_list))

print()
def bubble_sort(my_list):

    n = len(my_list)
    print(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not (my_list[j]<my_list[j+1]):
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return my_list
my_list = bubble_sort(my_list)

print(my_list)



print()
def my_binary_search(my_list,item_search):

    found = (-1,-1)
    low = 0
    high = len(my_list)-1

    while low <= high:

        mid = (low+high) // 2

        if(my_list[mid] == item_search ):
            return item_search,mid
        elif( my_list[mid] > item_search):
            high -= 1
        else:
            low += 1

    return found

my_list = [1,2,5,7,12,51,21,-4,-8,10,-2]
print(bubble_sort(my_list))
print(my_binary_search(bubble_sort(my_list),7))


print()
def my_median(my_list):

    my_list_2 = bubble_sort(my_list)

    n = len(my_list_2)

    if n%2 ==1:
        middle = int(n/2)+1
        median = my_list_2[middle]
    else:
        middle_1 = my_list_2[int(n/2)]
        middle_2 = my_list_2[int(n/2)+1]
        median = (middle_1 + middle_2) / 2

    return median


print(my_list)
print(my_median(my_list))