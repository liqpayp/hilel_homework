#методы строки
str = 'Hello World'
print(str.capitalize())
print(str.upper())
print(str.lower())
print(str.swapcase())
print(str.title())
print(str.count('o'))
print(str.find('World'))
print(str.find('world'))
print(str.find('World', 5))
print(str.find('World', 5, 10))
# методы списка
list = [1, 2, 3, 4, 5]
print(list.append(6))
print(list.insert(0, 0))
print(list.pop())
print(list.pop(0))
print(list.remove(3))
print(list.reverse())
print(list.sort())
print(list.count(3))
print(list.extend([7, 8, 9]))
print(list.clear())
print(list.copy())
#методы словаря
dict = {'name': 'John', 'age': '35'}
print(dict.get('name'))
print(dict.get('surname', 'Unknown'))
print(dict.keys())
#методы кортежа
tuple = (1, 2, 3, 4, 5)
print(tuple.count(1))
print(tuple.index(1))
print(tuple.index(1, 1))
print(tuple.index(1, 1, 3))
print(tuple.count(1, 1, 3))
#примеры исмользования max() и min() для списка и словаря
print(max(list))
print(min(list))
print(max(dict))
print(min(dict))
print(max(tuple))
print(min(tuple))
#примеры in и not in для списка и словаря
print(1 in list)
print(1 not in list)
print(1 in dict)
print(1 not in dict)
print(1 in tuple)
print(1 not in tuple)
#примера условия if elif else для списка и словаря
if 1 in list:
    print('1 есть в списке')
elif 1 in dict:
    print('1 есть в словаре')
elif 1 in tuple:
    print('1 есть в кортеже')
else:
    print('1 нет в списке и нет в словаре и нет в кортеже')









