goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}
store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')

table_code = goods['Стол']
table_item1 = store[table_code][0]
table_item2 = store[table_code][1]
table_quantity = table_item1['quantity'] + table_item2['quantity']
table_price1 = table_item1['price']
table_price2 = table_item2['price']
table_cost = table_item1['quantity'] * table_price1 + table_item2['quantity'] * table_price2
print('Стол -', table_quantity, 'шт, стоимость', table_cost, 'руб')

sofa_code = goods['Диван']
sofa_item1 = store[sofa_code][0]
sofa_item2 = store[sofa_code][1]
sofa_quantity = sofa_item1['quantity'] + sofa_item2['quantity']
sofa_price1 = sofa_item1['price']
sofa_price2 = sofa_item2['price']
sofa_cost = sofa_item1['quantity'] * sofa_price1 + sofa_price2 * sofa_item2['quantity']
print('Диван -', sofa_quantity, 'шт, стоимость', sofa_cost, 'руб')

chair_code = goods['Стул']
chair_item1 = store[chair_code][0]
chair_item2 = store[chair_code][1]
chair_item3 = store[chair_code][2]
chair_quantity = chair_item1['quantity'] + chair_item2['quantity'] + chair_item3['quantity']
chair_price1 = chair_item1['price']
chair_price2 = chair_item2['price']
chair_price3 = chair_item3['price']
chair_cost = chair_item1['quantity'] * chair_price1 + chair_item2['quantity'] * chair_price2 + chair_item3['quantity'] * chair_price3
print('Стул -', chair_quantity, 'шт, стоимость', chair_cost, 'руб')