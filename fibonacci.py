known = {0:0,1:1}

def fiborec(num):
    """
    #sözlük kullanılmadan yazılmış hali

    if(num<2):
        return num

    else:
        return fiborec(num-1)+fiborec(num-2)

    """

    if num in known:

        return known[num]
    else:
        result = fiborec(num-1)+fiborec(num-2)
        known[num] = result
        return known[num]

print(fiborec(8))


