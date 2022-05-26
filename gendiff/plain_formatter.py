def plain_formatter(diff, path=''):
    result = []
    for i in diff:
        key, value, status = i['key'], i['value'], i['status']
        if status == 'modified':
            old_value = i['old value']
            result.append(
                f'Property \'{path}{key}\' was updated. '
                f'From {stylish_value(old_value)} to {stylish_value(value)}')
        elif status == 'removed':
            result.append(
                f'Property \'{path}{key}\' was removed'
            )
        elif status == 'added':
            result.append(
                f'Property \'{path}{key}\' was added '
                f'with value: {stylish_value(value)}')
        elif status == 'parent modified':
            result.append(plain_formatter(value, f'{path}{key}.'))
    return '\n'.join(result)


def stylish_value(value):
    if type(value) == list:
        return '[complex value]'
    if type(value) == int:
        return value
    if value is True:
        result = 'true'
    elif value is False:
        result = 'false'
    elif value is None:
        result = 'null'
    else:
        result = f"\'{value}\'"
    return result
