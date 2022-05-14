import json

def parse_json(path):
    return json.load(open(path))

def generate_output_string(sign, key, value):
    result = f'  {sign} {key}: '
    if value == True:
        result += 'true'
    elif value == False:
        result += 'false'
    else:
        result += str(value)
    result += '\n'
    return result

def generate_diff(filepath1, filepath2, format):
    file1 = parse_json(filepath1)
    file2 = parse_json(filepath2)

    # Получаем массив отсортированных по алфавиту уникальных ключей
    keys1 = list(file1.keys())
    keys2 = list(file2.keys())
    keys = keys1 + keys2
    keys_uniq = list(set(keys))
    keys_uniq.sort()

    # Формируем выходной результат
    output = '{\n'

    # Проходим по ключам и смотрим их присутствие и значение в каждом файле
    for i in keys_uniq:
        # 1. Значение есть в обоих словарях
        if i in file1 and i in file2:
            if file1[i] == file2[i]:
                output += generate_output_string(' ', i, file1[i])
            else:
                output += generate_output_string('-', i, file1[i])
                output += generate_output_string('+', i, file2[i])
        # 2. Значение есть в первом, но отсутствует во втором
        elif i in file1:
            output += generate_output_string('-', i, file1[i])
        # 3. Значение есть во втором, но отсутствует в первом
        else:
            output += generate_output_string('+', i, file2[i])
    output += '}'
    return output
