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


def generate_diff(filepath1, filepath2):
    file1_extension = os.path.splitext(filepath1)[1]
    file2_extension = os.path.splitext(filepath2)[1]

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
    # keys_uniq = get_uniq_keys(file1, file2)

    return make_diff_list(file1, file2)


def make_diff_list(file1, file2):
    keys_uniq = get_uniq_keys(file1, file2)
    result = []
    for i in keys_uniq:
        if i not in file1:
            # Если нет в старом, но появилось в новом
            if type(file2[i]) == dict:
                result.append({
                    'key': i,
                    'status': 'added',
                    'value': make_diff_list(file2[i], file2[i])
                })
            else:
                result.append({
                    'key': i,
                    'status': 'added',
                    'value': file2[i]
                })
        elif i not in file2:
            # result[i] = ('deleted', file1[i])
            if type(file1[i]) == dict:
                result.append({
                    'key': i,
                    'status': 'removed',
                    'value': make_diff_list(file1[i], file1[i])
                })
            else:
                result.append({
                    'key': i,
                    'status': 'removed',
                    'value': file1[i]
                })
        elif file1[i] == file2[i]:
            # result[i] = ('not modified', file1[i])
            if type(file1[i]) == dict:
                result.append({
                    'key': i,
                    'status': 'not modified',
                    'value': make_diff_list(file1[i], file2[i])
                })
            else:
                result.append({
                    'key': i,
                    'status': 'not modified',
                    'value': file1[i]
                })
        elif type(file1[i]) == dict and type(file2[i]) == dict:
            # result[i] = ('nested modified', make_diff_list(file1[i], file2[i]))
            result.append({
                'key': i,
                'status': 'parent modified',
                'value': make_diff_list(file1[i], file2[i])
            })
        else:
            # result[i] = ('modified', file1[i], file2[i])
            if type(file1[i]) == dict:
                result.append({
                    'key': i,
                    'status': 'modified',
                    'value': file2[i],
                    'old value': make_diff_list(file1[i], file1[i])
                })
            elif type(file2[i]) == dict:
                result.append({
                    'key': i,
                    'status': 'modified',
                    'value': make_diff_list(file2[i], file2[i]),
                    'old value': file1[i]
                })
            else:
                result.append({
                    'key': i,
                    'status': 'modified',
                    'value': file2[i],
                    'old value': file1[i]
                })
    return result
