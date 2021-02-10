userfile = input("Which file do you want us to read? : ")

file = open(userfile, 'r')
#print(file.read())

words = 0

for line in file:
    linesplit = line.split()
    words = words + len(linesplit) 
print(words)            
