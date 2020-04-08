import sys

def ay_listesi():
    months_of_list = []
    with open(sys.argv[1]+"/input_hw_2.csv", mode="r") as dosya:
        for satir in dosya:
            i=0
            for sutun in satir.split(";"):
                if(i==3):
                    ay = sutun[5]+sutun[6]
                    months_of_list.append(ay)
                i = i+1
    return months_of_list

def my_frequency_with_dict(list):

    frequency_dict = {}

    for item in list:
        if (item in frequency_dict):
            frequency_dict[item] = frequency_dict[item]+1
        else:
            frequency_dict[item] = 1

    return frequency_dict

def bubble_sort(my_list):

    n = len(my_list)
    for i in range(n-1,-1,-1):
        for j in range(0,i):
            if not (my_list[j] < my_list[j+1]):
                temp = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = temp

    return my_list

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

def ortalama(my_list):

    s,t=0,0

    for item in my_list:

        s +=1
        t +=item

    ortalama = t/s

    return ortalama

def list_of_hist(hist_m):
    list_h =[]
    for item in hist_m:
        list_h.append(hist_m[item])
    return list_h


list_m = ay_listesi()
hist_m = my_frequency_with_dict(list_m)
list_h = list_of_hist(hist_m)
mean = int(ortalama(list_h))
median = my_median(list_h)

with open(sys.argv[2]+"/180401056_hw_2_output.txt",mode="w") as output:
    output.writelines("Median : {}".format(median)+"\n")
    output.writelines("Ortalama : {}".format(mean))
print("işlem basarili")











