#Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(num):
    new_list = []
    for i in range(num,-1,-1):
        new_list.append(i)
    return(new_list)

new_list = countdown(12)
print(new_list)

#Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(arg):
    print(list[0])
    return(list[1])
list = [1,4]
r = print_and_return(list)
print(r)

#First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

def first_plus_length(arg):
    return(arg[0] + len(arg))

list = [4,6,78,5,9,3]
r = first_plus_length(list)
print(r)

#Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False

def values_grater_than_second(arg):
    greater_than_second = []
    if len(arg)<2:
        return("False")
    else:
        for i in range(len(arg)):
            if arg[i]>arg[1]:
                greater_than_second.append(arg[i])
    print(len(greater_than_second))
    return(greater_than_second)

greater_than_second = values_grater_than_second([6,3,78,9,7,2,1,22,11,1,1,1])
print(greater_than_second)

#This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(l,v):
    lv_list=[]
    for i in range(l):
        lv_list.append(v)
    return(lv_list)

length_value_list = length_and_value(4,8)
print(length_value_list)