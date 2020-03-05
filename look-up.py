
#d = dictianory
#V = value

def lookup(d,V):

    for key in d:
        if d[key]== V:
            return key

    return -1

my_d = dict()

my_d ={1:3,2:5,6:8}


print(lookup(my_d,100))
