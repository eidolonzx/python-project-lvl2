def plain_formatter(diff, path=''):
    result = []
    for i in diff:
        key, value, status = i['key'], i['value'], i['status']
        if status == 'modified':
            result.append(
                f'Property \'{path}{key}\' was updated. '
                f'From {stylish_value(i["old value"])} to {stylish_value(value)}')
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
    if value == True:
        result = 'true'
    elif value == False:
        result = 'false'
    elif value == None:
        result = 'null'
    else:
        result = f"\'{value}\'"
    return result
