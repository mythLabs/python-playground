spam = 42 # Global scope

def eggs():
    spam = 42 # Local scope
    spam = spam -1
    print('Inside function' + str(spam))

eggs()
print('Outside function' + str(spam))