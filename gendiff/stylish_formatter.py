def stylish_formatter(diff, step=2):
    result = ['{']
    for i in diff:
        key = i['key']
        value = i['value']
        status = i['status']
        if status == 'added':
            add_added(result, key, value, step)
        elif status == 'removed':
            add_removed(result, key, value, step)
        elif status == 'not modified':
            add_not_modified(result, key, value, step)
        elif status == 'modified':
            add_modified(result, key, value, i['old value'], step)
        else:
            add_nested_modified(result, key, value, step)
    result.append(' ' * (step - 2) + '}')
    return '\n'.join(result)


def stylish_value(value):
    if value is True:
        return 'true'
    elif value is False:
        return 'false'
    elif value is None:
        return 'null'
    else:
        return value


def stylish_dict(dict_, step):
    result = ['{']
    str_intent = ' ' * step
    for i in dict_:
        value = i['value']
        key = i['key']
        if type(value) == list:
            result.append(
                f'{str_intent}  {key}: {stylish_dict(value, step + 4)}')
        else:
            result.append(f'{str_intent}  {key}: {stylish_value(value)}')
    result.append(' ' * (step - 2) + '}')
    return '\n'.join(result)


def add_added(result, key, value, step):
    str_step = ' ' * step
    if type(value) == list:
        result.append(
            f'{str_step}+ {key}: {stylish_dict(value, step + 4)}')
    else:
        result.append(f'{str_step}+ {key}: {stylish_value(value)}')
    return result


def add_removed(result, key, value, step):
    str_step = ' ' * step
    if type(value) == list:
        result.append(
            f'{str_step}- {key}: {stylish_dict(value, step + 4)}')
    else:
        result.append(f'{str_step}- {key}: {stylish_value(value)}')
    return result


def add_not_modified(result, key, value, step):
    str_step = ' ' * step
    if type(value) == list:
        result.append(
            f'{str_step}  {key}: {stylish_dict(value, step + 4)}')
    else:
        result.append(f'{str_step}  {key}: {stylish_value(value)}')
    return result


def add_modified(result, key, value, old_value, step):
    str_step = ' ' * step
    if type(old_value) == list:
        result.append(
            f'{str_step}- {key}: {stylish_dict(old_value, step + 4)}')
    else:
        result.append(f'{str_step}- {key}: {stylish_value(old_value)}')
    if type(value) == list:
        result.append(
            f'{str_step}+ {key}: {stylish_dict(value, step + 4)}')
    else:
        result.append(f'{str_step}+ {key}: {stylish_value(value)}')
    return result


def add_nested_modified(result, key, value, step):
    str_step = ' ' * step
    result.append(
        f'{str_step}  {key}: {stylish_formatter(value, step + 4)}')
    return result
