import math
# Digits practice 

def num_to_list(num):
    num_as_list = []

    i = 10
    while num >= 1:
        result = math.floor(num%i) 
        num_as_list.insert(0, result)
        num /= 10

    return num_as_list

def list_to_num(l):
    list_as_num = 0
    temp = []

    i = 1
    for digit in l:
        temp.insert(0, digit)
    for j in temp:
        list_as_num += i * j
        i *= 10
    return list_as_num

def at_most_one(last_item, current): #returns an affected value of last_item if it can be made smaller than at_most_one
    l = num_to_list(last_item)
    last_digit = 0
    i = 0
    for digit in l:
        if(digit<last_digit):
            # check if the swap lowers the value
            temp = l
            temp[i] = last_digit
            temp[i-1] = digit
            demo = list_to_num(temp)
            if demo < current:
                return demo
        last_digit = digit
        i += 1
    return last_item

def strictly_increasing(inlist):
    i = 1 
    while(i<len(inlist)):
        if inlist[i]<=inlist[i-1]:
            demo = at_most_one(inlist[i-1], inlist[i])
            if demo < inlist[i]:
                inlist[i-1] = demo
            else:
                print(inlist)
                return False
        i += 1
    print(inlist)
    return True

print(strictly_increasing([1,2,3,109,50,353,333]))

