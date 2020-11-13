# last updated: Nov12, 2020
# Akhrorbek Abdukhamitov
print(bin(5)) #output: 0b101 show the binary value.
print(int('0b101', 2)) #output 5
print(int('0b1100100', 2)) #output 100

PI = 3.14 #capital letter is saying the variable is cons

#naming variables is a skill

wealther = "It\'s \"kind of\" sunny"

long_string = '''
\t eiorhf
\n wsfor
wefjiow
wiejfoi
'''
name = "Bek"
age = 21

#both formatting works fine. First formatting is the PREFFERED
print(f'Hey {name}, you\'re already {age}')
print('Hey {}, you\'re already {}'.format(name, age))

#if you want to give new values then
print('Hi {name}, you\'re {age}'.format(name='Azizbek', age=18))

my_str = '0123456789'
#formatting is [start:stop:stepover]
print(my_str[0:10:2]) #output is 02468

#can be used for reversing too
my_str = my_str[::-1]

#strings are immutable
selfish = "12345"
'''
selfish[0] = "9" #this will give an error
''' 

basket = [1,2,3,4,5]
new_list = basket.append(100)

print(new_list) #output: None because append is inplace. doesn't assign the actual value
print(basket) #this will output [1,2,3,4,5,100]

## insert(position, value)
basket.insert(4,200) #output [1,2,3,4,200,100] adds 200 to position 4


basket.pop() #removes whatever is at the end of the list
#output os [1,2,3,4,200]
basket.pop(0) #can remove the indexed values too.
#output: [2,3,4,200]
#pop can assign a value. this one is an exception.
my_list = [2,3,4,5,6]

extended = my_list.pop(4)
print(extended)
#output: 6

basket.remove(200) #removes the value
	#output [2,3,4]

#list methods doesn't assign a new value *except for pop()

#index('b') will show the index number
my_list = ['a', 'b', 'c', 'd']

print(my_list.index('b'))

a_list = ['a', 'c', 'x', 'b']
a_list.sort() #will sort the list for us

#sorted(a_list) is a function
sorted(a_list) #and can be used same as a_list.sort() method

a_list.reverse() #reverses the indexes in the opposite
#------------------------------
print(list(range(1, 100, 2)))
#output is a list of numbers from 1-100 with a step of 2

#join method
sentence = ' '
print(sentence.join(['hi', 'my', 'name', 'is', 'JoJo']))
#output is: hi my name is JoJo

#list unpacking
a,b,c = [1,2,3]
print(a)
print(b)
print(c)
''' output is 
1
2
3
'''
a,b,c, *hyu = [1,2,3,4,5,6,7,8,9,10]
#when you print hyu the output is [4,5,6,7,8,9,10]

a,b,c, *hyu, d = [1,2,3,4,5,6,7,8,9,10]
#when you print hyu the output is [4,5,6,7,8,9]
#and print(d) is 10



my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

check = 'a'

if check in my_list:
    print(check + ' is in basket')
else: print(check + ' is not in basket')