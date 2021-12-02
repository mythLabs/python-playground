cat1 = {'name': 'zoey','age': 4}

cat2 = {'age': 4, 'name': 'zoey'}

if cat1== cat2:
    print('same')

if 'name' in cat1:
    print(cat1['name'])

print(cat1.keys())
print(cat1.values())
print(cat1.items())

print(list(cat1.keys()))
print(list(cat1.values()))
print(list(cat1.items()))

print(cat1.get('nn',0))