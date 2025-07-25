#Task 1: Read a File and Handle Errors

try:
    k='Sample.txt' #change the file name to check file does not found
    k=open('Sample.txt', 'r')
    reading_file=k.readlines()
    print(reading_file)
    k.close()
except FileNotFoundError:
    print(f'File {k} not found.')
finally:
    print()
