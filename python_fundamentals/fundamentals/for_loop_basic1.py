#Print all integers from 0 to 150.
for x in range(1,51)
print (x)

#Print all the multiples of 5 from 5 to 1,000
for i in range(5,1001)
if((i %= 5) == 0):
    mult_of_five.append(i)
    print(mult_of_five)

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"
for y in range(1,101)
if y %= 5 == 0:
print("coding")
elif y %=10 == 0:
print("coding dojo")
else:
continue

#Add odd integers from 0 to 500,000, and print the final sum
sum=0
for x in range(0,500001)
if x %= 2 !=0:
sum=sum+x
print(sum)

#Print positive numbers starting at 2018, counting down by fours
num = 2018
while num > 0:
    print(num)
    num -= 4

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example,
# if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lownum=2
highnum=20
mult=5
for i in range(lownum , highnum)
    if i %= mult == 0:
    print(i)

#output full_name function
def full_name(f_name,l_name)
    full_name = f_name + l_name
    return full_name
    name=full_name("anis","ben selma")
    print(name)








