from gendiff.parsers import parse_json
from gendiff.parsers import parse_yaml
from gendiff.stylish_formatter import stylish_formatter
from gendiff.plain_formatter import plain_formatter
from gendiff.json_formatter import json_formatter
import os.path


def generate_diff(filepath1, filepath2, format='stylish'):
    file1_extension = os.path.splitext(filepath1)[1]

    if file1_extension == '.json':
        file1 = parse_json(filepath1)
        file2 = parse_json(filepath2)
    else:
        file1 = parse_yaml(filepath1)
        file2 = parse_yaml(filepath2)

    diff_result = make_diff_list(file1, file2)

    if format == 'stylish':
        return stylish_formatter(diff_result)
    elif format == 'plain':
        return plain_formatter(diff_result)
    else:
        return json_formatter(diff_result)


def get_uniq_keys(dict1, dict2):
    keys_uniq = sorted(dict1.keys() | dict2.keys())
    return keys_uniq


def make_diff_list(file1, file2):  # noqa: C901
    keys_uniq = get_uniq_keys(file1, file2)
    result = []
    for i in keys_uniq:
        result_item = {
            'key': i
        }
        if i not in file1:
            result_item['status'] = 'added'
            if type(file2[i]) == dict:
                result_item['value'] = make_diff_list(file2[i], file2[i])
            else:
                result_item['value'] = file2[i]
        elif i not in file2:
            result_item['status'] = 'removed'
            if type(file1[i]) == dict:
                result_item['value'] = make_diff_list(file1[i], file1[i])
            else:
                result_item['value'] = file1[i]
        elif file1[i] == file2[i]:
            result_item['status'] = 'not modified'
            if type(file1[i]) == dict:
                result_item['value'] = make_diff_list(file1[i], file2[i])
            else:
                result_item['value'] = file1[i]
        elif type(file1[i]) == dict and type(file2[i]) == dict:
            result_item['status'] = 'parent modified'
            result_item['value'] = make_diff_list(file1[i], file2[i])
        else:
            result_item['status'] = 'modified'
            if type(file1[i]) == dict:
                result_item['value'] = file2[i]
                result_item['old value'] = make_diff_list(file1[i], file1[i])
            elif type(file2[i]) == dict:
                result_item['value'] = make_diff_list(file2[i], file2[i])
                result_item['old value'] = file1[i]
            else:
                result_item['value'] = file2[i]
                result_item['old value'] = file1[i]
        result.append(result_item)
    return result
