file = open('story.txt','r')

lines = file.readlines()
num_lines = len(lines)

print("The number of lines in this story is: ", num_lines)

file.close()
