#Write a Python program to reverse a string

#function:
def str_reverse(string1):
    reverse1 = ''
    index = len(string1)
#while loop:
    while index > 0:
        reverse1 += string1[index-1] 
        index = index - 1
#return:
    return reverse1
    
#print string reverse:
print(str_reverse(("1234abcd")))

    