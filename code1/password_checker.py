username = input("username: ")
password = input("password: ")

len = len(password)
len_minus = len - 3

hidden_password = str('*' * len_minus) + str(password[len_minus:len-1]) + '*'

print(f'your username is {username} and password is {hidden_password}')
