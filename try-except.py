def divby(dividedBy):
    try:
        return 42 / dividedBy
    except ZeroDivisionError:
        print('Error: dividing by zero')

print(divby(2))
print(divby(12))
print(divby(0))
print(divby(6))