#Task 2: Write and Append Data to a File

user_input = input('Enter text to write to the file: ')
file = open('output1.txt', 'w')
file.write(user_input + '\n')
file.close()

file = open('output1.txt', 'a')
file.write('Learning File handling in Python\n')
file.close()

file = open('output1.txt', 'r')
file_1 = file.read()
print(file_1)
file.close()
