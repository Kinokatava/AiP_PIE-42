print("Задание 1")
dict_1 = {1: 'a', 2: 'b'}
dict_2 = {2: 'c', 4: 'd'}
result1 = dict_1 | dict_2
result2 = {**dict_1, **dict_2}
print(f"Первый результат выполнения: {result1}")
print(f"Второй результат выполнения: {result2}\n")

print("Задание 2")
# Функция для нахождения максимального значения для каждого ключа
def max_dct(*dicts):
    result = {}
    all_keys = set()
    for i in dicts:
        all_keys.update(i.keys())  # Собираем все уникальные ключи

    for key in all_keys:
        max_value = float('-inf')  # Инициализация макс
        for i in dicts:
            max_value = max(max_value, i.get(key, float('-inf')))  # Находим максимум
        result[key] = max_value  # Сохраняем результат
    return result

# Функция для нахождения суммы значений для каждого ключа
def sum_dct(*dicts):
    result = {}
    all_keys = set()
    for i in dicts:
        all_keys.update(i.keys())  # Собираем все уникальные ключи

    for key in all_keys:
        total_sum = 0  # Инициализация суммы
        for i in dicts:
            total_sum += i.get(key, 0)  # Суммируем значения
        result[key] = total_sum  # Сохраняем результат
    return result

dict_1 = {1: 12, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
dict_2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
dict_3 = {2: 3, 3: 3, 4: 60, 6: 8, 7: 25, 8: 71}
dict_4 = {3: 1, 4: 13, 5: 31, 9: 9, 10: 556}

print("Максимум для dict_1 и dict_2:\n", max_dct(dict_1, dict_2))
print("Сумма для dict_1, dict_4 и dict_3:\n", sum_dct(dict_1, dict_4, dict_3))
print("Максимум для всех словарей:\n", max_dct(dict_1, dict_2, dict_3, dict_4))
print("Сумма для всех словарей:\n", sum_dct(dict_1, dict_2, dict_3, dict_4), "\n")

print("Задание 3")
def set_gen(numbers):
    res = set()
    counts = {}

    for i in numbers:
        if i not in counts:
            counts[i] = 1
            res.add(i)
        else:
            counts[i] += 1
            k = str(i) * counts[i]
            res.add(k)
    return res

list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]
print(set_gen(list_1))
print(set_gen(list_2))
print(set_gen(list_3), "\n")

print("Задание 4")
def superset(set_1, set_2):
    if set_1 == set_2:
        print("Множества равны")
    elif set_1.issuperset(set_2) and set_1 != set_2:
        print(f"Объект {set_1} является чистым супермножеством")
    elif set_2.issuperset(set_1) and set_2 != set_1:
        print(f"Объект {set_2} является чистым супермножеством")
    else:
        print("Супермножество не обнаружено")

set_1 = {1, 8, 3, 5}
set_2 = {3, 5}
set_3 = {5, 3, 8, 1}
set_4 = {90, 100}

superset(set_1, set_2)
superset(set_1, set_3)
superset(set_2, set_3)
superset(set_4, set_2)