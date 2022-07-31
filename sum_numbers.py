 #Write a Python function to sum all the numbers in a list

 #Function
def sum(numbers):
    total = 0

#For loop:
    for value in numbers:
        total +=value

#return
    return total

#print the sum of value
print(sum(((8,2,3,0,7))))
