my_family = ['Раис', 'Эльвира', 'Эвелина', 'Кашиф', 'Фамия']
my_family_height = [
    ['Раис', 178],
    ['Эльвира', 162],
    ['Эвелина', 158],
    ['Кашиф', 182],
    ['Фамия', 154]
]
print(f'Рост отца -', my_family_height[0][1])
total_height = 0
for person in my_family_height:
    total_height += person[1]
print(f'Общий рост моей семьи -', total_height)