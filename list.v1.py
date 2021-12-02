data = [1,'st', 3, 6]

print(data)

print(data[2])

print(data[1:3])

print(data[1:])

print(data[:2])

del data[3]

print(data)

if 3 in data:
    print('present')

if 5 not in data:
    print('absent')
