from gendiff.parsers import parse_json
from gendiff.parsers import parse_yaml
import os.path


# Получить список уникальных ключей, входящих в оба словаря
def get_uniq_keys(dict1, dict2):
    keys1 = list(dict1.keys())
    keys2 = list(dict2.keys())
    keys = keys1 + keys2
    keys_uniq = list(set(keys))
    keys_uniq.sort()
    return keys_uniq


def generate_diff(filepath1, filepath2, format):
    file1_extension = os.path.splitext(filepath1)[1]
    file2_extension = os.path.splitext(filepath2)[1]
    print('-*-*-*-*-*-*-*-*-*-')
    print(file1_extension)
    if file1_extension != file2_extension:
        raise SystemExit("ERROR 1: Can't compare files with different extensions")
    # Конвертим содержимое файлов в словарь
    if file1_extension == '.json':
        file1 = parse_json(filepath1)
        file2 = parse_json(filepath2)
    elif file1_extension == '.yaml' or file1_extension == '.yml':
        file1 = parse_yaml(filepath1)
        file2 = parse_yaml(filepath2)
    else:
        raise SystemExit("ERROR 2: Unknown file extensions")

    # Получаем массив отсортированных по алфавиту уникальных ключей
    keys_uniq = get_uniq_keys(file1, file2)

    # Формируем результирующий список, в котором каждый элемент
    #  - словарь свойств каждого ключа
    return make_diff_list(file1, file2, keys_uniq, [])


def make_diff_list(dict1, dict2, keys_uniq, acc):

    for i in keys_uniq:
        # 1. Если одинаковые ключи есть в обоих файлах
        if i in dict1 and i in dict2:
            # 1.1 Если в обоих ключах словари
            if type(dict1[i]) is dict and type(dict2[i]) is dict:

                child1 = dict1[i]
                child2 = dict2[i]
                if child1 == child2:
                    type_of_element = 'unchanged'
                else:
                    type_of_element = 'changed'

                uniq_keys = get_uniq_keys(child1, child2)
                children = make_diff_list(child1, child2, uniq_keys, [])
                acc.append({
                    'key': i,
                    'parent': True,
                    'type': type_of_element,
                    'children': children
                })
            # 1.2 Если в первом ключе словарь, а во втором значение
            elif type(dict1[i]) is dict:
                child1 = dict1[i]
                children = make_diff_list(child1, child1, child1.keys(), [])
                acc.append({
                    'key': i,
                    'parent': True,
                    'type': 'deleted',
                    'children': children
                })
                acc.append({
                    'key': i,
                    'value': dict2[i],
                    'type': 'added',
                    'parent': False
                })
            # 1.3 Если в первом ключе значение, а во втором словарь
            elif type(dict2[i]) is dict:
                child2 = dict2[i]
                children = make_diff_list(child2, child2, child2.keys(), [])
                acc.append({
                    'key': i,
                    'value': dict1[i],
                    'type': 'deleted',
                    'parent': False
                })
                acc.append({
                    'key': i,
                    'parent': True,
                    'type': 'added',
                    'children': children
                })
            # 1.4 Если в обоих ключах значения, и они одинаковые
            elif dict1[i] == dict2[i]:
                acc.append({
                    'key': i,
                    'value': dict1[i],
                    'type': 'unchanged',
                    'parent': False
                })
            # 1.5 Если в обоих ключах значения, и они разные
            else:
                # type = 'changed'
                acc.append({
                    'key': i,
                    'old_value': dict1[i],
                    'new_value': dict2[i],
                    'type': 'changed',
                    'parent': False
                })
        # 2. Если ключ есть в первом словаре, но отсутствует во втором
        elif i in dict1:
            # 2.1 Если в ключе словарь
            if type(dict1[i]) is dict:
                child1 = dict1[i]
                children = make_diff_list(child1, child1, child1.keys(), [])
                acc.append({
                    'key': i,
                    'parent': True,
                    'type': 'deleted',
                    'children': children
                })
            # 2.2 Если в ключе значение
            else:
                acc.append({
                    'key': i,
                    'value': dict1[i],
                    'type': 'deleted',
                    'parent': False
                })
        # 3. Если ключ есть во втором словаре, но отсутствует в первом
        else:
            # 3.1 Если в ключе словарь
            if type(dict2[i]) is dict:
                child2 = dict2[i]
                children = make_diff_list(child2, child2, child2.keys(), [])
                acc.append({
                    'key': i,
                    'parent': True,
                    'type': 'added',
                    'children': children
                })
            # 3.2 Если в ключе значение
            else:
                acc.append({
                    'key': i,
                    'value': dict2[i],
                    'type': 'added',
                    'parent': False
                })
    return acc
