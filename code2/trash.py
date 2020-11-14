# is_user = True
# is_friend = True
# if is_friend and is_user:
#     print("best frends forever")



''' #ternary operation

#print("If is printed") if False else print("else is printed")
is_friend = True
message = "message is allowed" if is_friend else "message is NOT allowed"
print(message)
'''




'''
#about Falsy and Truthy

All values are considered "truthy" except for the following, which are "falsy":

None
False
0
0.0
0j
Decimal(0)
Fraction(0, 1)
[] - an empty list
{} - an empty dict
() - an empty tuple
'' - an empty str
b'' - an empty bytes
set() - an empty set
an empty range, like range(0)
objects for which
obj.__bool__() returns False
obj.__len__() returns 0
'''


#is vs ==
# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([1,2,3] == [1,2,3])
# print('\n')

#now using is

# print(True is 1)
# print(True is True)
# print('' is 1)
# print('' is '')
# print([] is [])
# print(10 is 10.0)
# print([1,2,3] is [1,2,3])

#is more strict


'''
for item in {1,2,3,4,5}:
    for x in ['a', 'b', 'c']:
        print(item, x)
'''


# user = {
#     'name': 'Bek',
#     'age': 21,
#     'can_swim': True 
# }

# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for key, value in user.items():
#     print(key, value)

# #the name like d, s doesn't matter
# for d, s in user.items():
#     print(d, s)

# #this will give an error
# #for item in 50:
# #    print(item)


''' global inside function
#but this method is inefficient

table = 0

def confusion():
    global table
    table += 1
    return table

confusion()
confusion()
print(confusion())
'''



'''
#another method
table = 0

def confusion(table):
    table += 1
    return table

print(confusion(confusion(confusion(table))))
'''

# my_list = []
# for i in range(1, 11):
#     my_list.append(i)
# print(my_list)

# counter = 0

# for item in my_list:
#     counter += item 
# print(counter)

# for _ in range(0, 10, 2):
#     print()

#print(list(range(1, 11))) #output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''
for char in enumerate('man'):
    print(char)
'''

value = 0.0
output = int(value >= 0)
print(output)