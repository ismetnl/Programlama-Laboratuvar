def max_of_two(a,b):
    if a>b:
        return a
    else:
        return b

def max_of_three(a,b,c):
    return max_of_two(a,max_of_two(b,c))

def atset(liste=[14,-3,5,-2,-1,2,6,-2]):
    n = len(liste)
    if(n==1):
        return liste[0]
    left_i = 0
    left_j=n//2
    right_i = n//2
    right_j=n
    left_sum = atset(liste[left_i:left_j])
    right_sum = atset(liste[right_i:right_j])
    temp_left_sum = 0
    t = 0

    for i in range(left_j-1,left_i-1,-1):
        t = t+liste[i]
        if(t>temp_left_sum):
            temp_left_sum = t

    t = 0
    temp_right_sum = 0

    for i in range (right_i,right_j):
        t = t+liste[i]
        if(t>temp_right_sum):
            temp_right_sum = t

    center_sum = temp_left_sum+temp_right_sum
    return max_of_three(left_sum,right_sum,center_sum)


print(atset())