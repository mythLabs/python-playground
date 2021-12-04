print("""hi this is
transferable to new line""")

print('hi \n yo')
print(r'hi \n yo')

# string are immutable thus function return new value unlist list where function manupulate original value

spam="low ow low"
print(spam.upper())
print(spam)

spam1= "     abc"
print(spam1)
print(spam1.strip())
print(spam1.lstrip())

print("{1} - {0}".format('f','s'))

print("Hello %s, how %s you ?" % ('amit','are'))