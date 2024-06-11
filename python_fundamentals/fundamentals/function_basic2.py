# 1-countdown: Create a function that accepts a number as an input. 
#Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
#Example: countdown(5) should return [5,4,3,2,1,0]

def countdown(begin):
    list = []
    return list(range(begin,-1,-1))
'''
def countdown(num):
output = []
for i in range(num,-1,-1)
output.append(i)
return output

print (countdown(5))
'''

#2-Print and return Create a function that will receive a list with two numbers. Print the first value and return the second.
#Example: print_and_return([1,2]) should print 1 and return 2

def print_and_return(x,y):
    print(x)
    return(y)
'''
def print_and_return(list)
print (list[0])
return list[1]

print (print_and_return(1,2))
'''

#3-first_plus_length : Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
#Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
sum=0
def first_plus_length(list):
    sum = list[0] + len(list)
    return sum

#Values Greater than Second : Write a function that accepts a list 
#and creates a new list containing only the values from the original list that are greater than its 2nd value. 
#Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
#Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
#Example: values_greater_than_second([3]) should return False
def greater_than_second(list_1,list_2):
    while list_1[i]>list_1[1] :
        list_2.append(list_1(i))
        if len(list_2) > 2 :
            print(len(list_2))
            print(list_2)
        else
        return false
    
    '''
    def values_greater_than_second(list):
    if len(list) < 2:
        return False
    output = []
    for i in range(0,len(list)):
        if list[i] > list[1]:
            output.append(list[i])
    print(len(output))
    return output

    print(values_greater_than_second([5,2,3,2,1,4]))
    print(values_greater_than_second([3]))
    '''

#length_and_value : Write a function that accepts two integers as parameters: size and value. 
#The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
#Example: length_and_value(4,7) should return [7,7,7,7]
#Example: length_and_value(6,2) should return [2,2,2,2,2,2]

def length_and_value(int(size),int(val)):
        return [val] * size 

'''
def length_and_value(size,value):
    output = []
    for i in range(0, size):
        output.append(value)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
'''

capitals = {"Washington":"Olympia","California":"Sacramento",
            "Idaho":"Boise","Illinois":"Springfield",
            "Texas":"Austin","Oklahoma":"Oklahoma City",
            "Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc