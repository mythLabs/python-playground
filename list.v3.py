food = ['Bread', 'Milk', 'Butter', 'Butter', 'Eggs', 'Chicken']

print(food.index('Butter'))

food.append('end')

food.insert(2, 'mid')

food.remove('Butter')

food.sort(key=str.lower)

print(food)