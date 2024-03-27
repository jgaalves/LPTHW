from sys import argv

script = argv
filename = input("Type the filename \n > ")
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

#print("Type the filename again: ")
#file_again = input("> ")
#
#txt_again = open(file_again)
#
#print(txt_again.read()) 