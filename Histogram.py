
def my_h(list_1):

    my_d = dict()

    for i in list_1:

        if i in my_d:
            my_d[i] += 1

        else:
            my_d[i] = 1


    return my_d

List_1 = [0,5,25,100,5,5,0,100]

print(my_h(List_1))
