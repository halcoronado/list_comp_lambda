#numbers 1 through 9
x = [i for i in range(10)]
print(x)
#adding an expression - sq of each number

squares = [i**2 for i in range(10)]

print(squares)

##multiply each element by 3, can be item or i any varuable
list1 = [3,4,5]
multiplied = [item*3 for item in list1]

print (multiplied)


##word manipulaion

listofwords =['this', 'is', 'a', 'list', 'of' ,'words']

items = [word[0] for word in listofwords]

print(items)


list1 = ['A','B','C']
list2 = [x.lower() for x in list1]
print (list2)
list3 = [x.upper() for x in list1]
print (list3)


##adding an IF condition
#akk even numbers from 0-4 (square)
new_range = [i*i for i in range(5) if i%2 ==0]
print(new_range)

string = 'Hello 12345 world'

just_numbs = [i for i in string if i.isdigit()]
just_letters = [x for x in string if x.isalpha()]

print(just_letters)
print(just_numbs)


##Using file

my_file = open('test.txt','r')

result =[x.rstrip('\n') for x in my_file if 'line3' in x]

print(result)


### using functions

def double(x):
    return x*2

print(double(10))


mynumbers = [double(x) for x in range(10)]
print(mynumbers)

#for even numbers only
mynumbers = [double(x) for x in range(10) if x%2==0]
print(mynumbers)

result = [x+y for x in [10,30,50] for y in [20,40,60]]
print (result)