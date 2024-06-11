'''
Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
Change the last_name of the first student from 'Jordan' to 'Bryant'
In the sports_directory, change 'Messi' to 'Andres'
Change the value 20 in z to 30
'''
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
#Change the value 10 in x to 15
x [1][0]=15 
print(x) 

#Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]["last_name"] = "Bryant"

#In the sports_directory, change 'Messi' to 'Andres'
sports_directory["soccer"][0] = "Andres" 

#Change the value 20 in z to 30
z[0]["y"] = 30

'''
Create a function iterateDictionary(some_list) that, given a list of dictionaries, 
the function loops through each dictionary in the list and prints each key and the associated value.
'''
def iterateDictionary(list)
    for i in range(0,len(list))
    output = ""
    for key,val in list[i].items()
    output += f"{key} - {val},"
    print(output)

    iterateDictionary(students)

    '''
    Create a function printInfo(some_dict) that given a dictionary whose values are all lists,
    prints the name of each key along with the size of its list, and then prints the associated values within each key's list.
    '''

    

