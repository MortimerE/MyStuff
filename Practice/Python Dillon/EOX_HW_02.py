def replace_dub_quote(temp):
    index = 0
    while temp.find('"', index) != -1 and index < len(temp):
        temp = temp[0:index] + "'" + temp[index+1:] 
        index = temp.find('"', index)
    return temp

def exists_in(temp, target):
    str_index = temp.find(target)
    if str_index != -1:
        return("the sweet cheeks are located at : " + str(str_index))
    else:
        return("the princess is in another castle!")

def bool_in(temp, target):
    return temp.find(target) != -1

def is_bool_in(temp, target):
    str_index = temp.find(target)
    if(bool_in(temp,target)):
        return("Oh, we boolin! " + str(str_index))
    else:
        return("Unfortunately, it would appear that we are not boolin")

def is_greater_than_fifty(num, be_loud):
    output = ""
    if type(num) is not int:
        output = "Silly rabbit, this function is for numbers…"
    elif num>50:
        output = "That's a pretty big number!"
    else:
        output = "Not too big of a number…"
    if type(be_loud) is bool() and be_loud:
        output = output.upper()
    elif type(be_loud) is not bool:
        output += "\n...and 'be_loud' needs to be a bool!"
    return output

quote_string = '"Theese"' + " hoes are " + '"lit"'
mystring = "peepeepoopoo"
print(exists_in(mystring, "eepo"))
print(bool_in(mystring, "eepo"))
print(is_bool_in(mystring, "eepo"))
print(quote_string)
print(replace_dub_quote(quote_string))