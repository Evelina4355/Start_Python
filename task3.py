[1, 1.2, 'привет']
a = [1, 1.1, 'a', [1], (1, 1.1), {1, 2}, {'a': 1}, None, True]  # Список в котором целое; вещественное; строковое; другой список; кортеж; множество; словарь; пустой тип; булевый тип.
a = []  # Пустой список
b = list()  # Пустой список
a = (1, 2.1, 3)  # Раньше я был кортежем
list(a)  # [1, 2.1. 3], но 'a' остался кортежем
b = list('abc')  # ['a','b','c',]
a = [1, 1.1, 'a']
print(a)  # [1, 1.1, 'a']
print([1, 1.1, 'a'])  # [1, 1.1, 'a']
a = [1, 1.1, 'a']
a[0]  # 1
a[1]  # 1.1
a[2]  # 'a'
a[3]  # Ошибка, вышли за границы
a[-1]  # 'a'
a[-2]  # 1.1
a[-3]  # 1
a[-4]  # Ошибка, вышли за границы
a = [1, 2, 3]
a.index(3)  # 2.Возвращает индекс,где передаваемое значение стоит в списке.В примере вернется 2,так как значение 3 в списке стоит на 2-ом индексе.
a = [1, 1.1, 'a']
a[0] = 'а'  # Теперь'a'равно ['a', 1.1, 'a']
a[1] = 'б'  # Теперь'a' равно ['a', 'б', 'a']
a[-1] = 'в'  # Теперь'a' равно ['a', 'б', 'в']
a = [1, 2, 3]  # Теперь'a'равно [1, 2, 3]
a = [1, 2, 3]
a.append(4)  # Добавляет значение(объект) в конец списка. Добавляет только один объект или значение.Теперь "a" [1,2,3,4]
a.append(['a', 'b'])  # Теперь"a" [1,2,3,4,['a', 'b']]. Не забываем, что методы в списке изменяют значения и структуру в самом списке.
a = [1, 2, 3]
a.insert(0, 4)  # Добавляет значение (объект), что стоит на втором месте (4) на место под индексом, что стоит на первом месте (0). В конкретном примере добавит 4 на 0-ой индекс, т.е. вначало. Теперь "а" [4, 1, 2, 3]
a = [1, 2, 3]
a.insert(3, 4)  # В конкретном примере добавит 4 на 3-ий индекс, т.е вконец. Теперь "a" [1, 2, 3, 4]/
a = [1, 2, 3]
a.insert(-1, 4)  # Кажется, что здесь должно значение 4 добавить в конце, но на самом деле 4 встанет в предпоследнее место. Теперь "a" [1, 2, 4, 3]
a = [1, 2, 3]
a.extend([4, 5, 6])  # Добавляет данные в список поэлементно. Теперь "a" [1, 2, 3, 4, 5, 6]
a = [1, 1.1, 'a']
del a[0]  # Теперь'a' равно [1.1, 'a']
del a[-1]  # Теперь'a' равно [1.1]
del a[-1]  # Теперь'a' равно []
del a  # Полное удаление переменной"a"
a = [1, 2, 3]
a.clear()  # Полностью очмщает список, превращая его в пустой список. Теперь"a" []
a = [1, 2, 3]
a.pop(1)  # Возвращает последний элемент  и удаляет его из списка. В примере вернет 3 и удалит его из списка. Теперь"a" [1,2]
a = [1, 'ab', 3]
a.pop(1)  # Возвращает элемент по указанному ИНДЕКСУ и удаляет его из списка. В примере вернет 'ab' и удалит его из списка. Теперь "a" [1,3]. Если такого индекса нет, то возникает ошибка indexError: pop index out of range
a = [1, 2, 'ab']
a.remove('ab')  # Удаляет элемент по указанному ЗНАЧЕНИЮ из списка. Если данного значения нет, то появится ошибка. Теперь "а"[1,2]. Если такого значения нет, то возникнет ошибка ValueError: list.remove(x): x not in list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # '[1,2,3,4,5,6]'
a += b  # Теперь"a" равно '[1,2,3,4,5,6]'
a = [1, 2, 3]
b = 2
c = a * b
print(c)  # [1,2,3,1,2,3]
a *= b  # Теперь "a" равно [1,2,3,1,2,3]
a = [1, 2, 3]  # Это одновременый список
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Это двумерный (список в списке) список. Его можно представить как: [[1,2,3], [4,5,6], [7,8,9]]
b = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b[0]  # Получение 1-го списка [1,2,3]
b[0][0]  # Получение 1-го элеиента "1"из 1-го списка[ 1,2,3]
b[-1][-1]   # Получение последнего элеиента "9" из последнего списка [7, 8, 9]
help(list)  # Информация о списках
a = [1, 1, 3, 1]
a.count(1)  # 3. Возвращает сколько раз в списке встретилось предаваемое значение. В примере вернется 3, так как в списке три единицы.
a = [1, 2, 3]
a.copy()  # [1,2,3]. Возвращает копию списка. Это удобно, чтобы скопировать данные в новую переменную и изменять значение уже в новой переменной, чтобы значения в старой переменной не изменилось.
a = [1, 2, 3]
a.reverse()  # Полностью переворачивает список. Теперь "а" [3,2,1]
a = [2, 1, 3]
a.sort()  # Сортирует значения в списке в порядке ВОЗРАСТАНИЯ. Теперь "а" [1,2,3]
a = [2, 1, 3]
a.sort(reverse=True)  # Сортирует значения в списке в порядке УБЫВАНИЯ. Теперь  "а" [3,2,1
a = [1, 2 [1, 2, 3]]
b = a.copy()  # Скопировали значения из "а" в "b". Тепеь "b" [1, 2,[1,2,3]].
b[2][0] = 10  # Поменяли значение во вложенном списке списка "b". Теперь "b" [1, 2[10,2,3]]/
print(a)  # [1, 2,[10,2,3]]. Значение в "а" тоже поменялось.
b[0] = 10  # Поменяли значение в списке "b". Теперь "b" [10, 2, [10, 2,3]].
print(a)  # [1,2[10,2,3]]. Значение "a" в этот раз не поменялось.
from copy import deepcopy
a = [1, 2, [1, 2, 3]]
b = deepcopy(a)  # Теперь "b" [1,2,[1,2,3]].
b[2][0] = 10  # Теперь  "b" [1,2,[10,2,3]].
print(a)  # [1,2,[1,2,3]]. Значение в "а" не поменялось.
a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]  # Можно так
b = [[0] * 3]*3  # А можно так. Только в этом случае есть небольшая особенность.
a[0][0] = 1  # Здесь все будет как и планировалось. "а" [[1,0,0],[0,0,0],[0,0,0]]
b[0][0] = 1  # А здесь, не так как плани ровалось. "b" [[1,0,0],[0,0,0],[0,0,0]]

