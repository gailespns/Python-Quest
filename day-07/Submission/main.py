file = open('user_info.txt','w')

user_info = input("Enter your name: ")

file.write(user_info)

file.close()
