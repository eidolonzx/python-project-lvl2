from gendiff.parsers import parse_json
from gendiff.parsers import parse_yaml
import os.path


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
        raise SystemExit("ERR 1: Can't compare files with different extensions")

    if file1_extension == '.json':
        file1 = parse_json(filepath1)
        file2 = parse_json(filepath2)
    elif file1_extension == '.yaml' or file1_extension == '.yml':
        file1 = parse_yaml(filepath1)
        file2 = parse_yaml(filepath2)
    else:
        raise SystemExit("ERR 2: Unknown file extensions")

    return make_diff_list(file1, file2)


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
