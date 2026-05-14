zoo = ['lion', 'kangaroo', 'elephant', 'monkey',]
zoo.insert(1, 'bear')
print(zoo)

birds = ['rooster', 'ostrich', 'lark', ]
zoo.extend(birds)
print(zoo)

zoo.remove('elephant')
print(zoo)

lion = zoo.index('lion') + 1
lark = zoo.index('lark') + 1
print(f'Лев сидит в {lion} клетке')
print(f'Жаворонок сидит в {lark} клетке')