# Python function that accepts a string and calculate the number of upper case letters and lower case letters.

#function:
def string_case(string):
    case = {"UPPER_CASE":0,"LOWER_CASE":0}

#for loop:
    for char in string:
        if char.isupper():
            case["UPPER_CASE"]+=1
        elif char.islower():
            case["LOWER_CASE"]+=1
        else:
            pass
#print the  count of upper and lower case characters:
    print("Original string :",string)
    print("number of upper case characters : ",case["UPPER_CASE"])
    print("number of lower case characters : ",case["LOWER_CASE"])
string_case('The quick Brow Fox')
