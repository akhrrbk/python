#dictionaries
user1 = {
	'student_number': 721384,
	'name': 'Bek'
}

user2 = dict(name='John', student_number = 23740)
print(user2)
print(user1['name'] + '\'s age is ' + str(user1.get('age', 21)))
print(user1)


print('Bek' in user1.keys())
print('Bek' in user1.values())
print('Bek' in user1.items())

user2 = user1.copy()
print(user1.clear()) #output: None
print(user1)
print(user2)
print(user2.pop('student_number'))
print(user2)
# user2.popitem()
user2.update({'name': 55})
print(user2)

#sets
my_set = {1,2,3,4,5,5}
print(my_set) #prints only one 5 since 5 is already there

my_set.add(100) #adds 100 
print(my_set)

my_set.add(2) #nothing happens since 2 is already in the list
print(my_set)

new_set = my_set.copy()
my_set.clear()
print(new_set)
print(my_set) #output: set() which is empty

#set methods
'''
.difference()
.discard()
.difference_update()
.intersection()
.isdisjoint()
.issubset()
issuperset()
union()
'''