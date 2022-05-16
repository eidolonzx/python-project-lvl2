def render_prefix(key, sign, step):
    return f'{" " * step} {sign} {key}: '


def fix_bool_values(value):
    if isinstance(value, bool):
        if value == True:
            return 'true'
        elif value == False:
            return 'false'
    if value is None:
        return 'null'    
    return value

def render_diff_result(diff_result):
    output = '{\n'
    def iter(dict, step):
        nonlocal output
        for i in dict:
            if i['parent'] == True:
                if i['type'] == 'unchanged' or i['type'] == 'changed':
                    sign = ' '
                    # TODO: лишняя проверка, исправить в engine.py и здесь
                elif i['type'] == 'added':
                    sign = '+'
                else:
                    sign = '-'

                output += render_prefix(i['key'], sign, step)
                step += 4
                output += '{\n'
                iter(i['children'], step)
                output += ' ' * (step - 1)
                output += '}\n'
                step -= 4
            else:
                if i['type'] == 'unchanged':
                    output += render_prefix(i['key'], ' ', step)
                    output += str(fix_bool_values(i['value']))
                elif i['type'] == 'changed':
                    output += render_prefix(i['key'], '-', step)
                    output += str(fix_bool_values(i['old_value']))
                    output += '\n'
                    output += render_prefix(i['key'], '+', step)
                    output += str(fix_bool_values(i['new_value']))
                elif i['type'] == 'deleted':
                    output += render_prefix(i['key'], '-', step)
                    output += str(fix_bool_values(i['value']))
                elif i['type'] == 'added':
                    output += render_prefix(i['key'], '+', step)
                    output += str(fix_bool_values(i['value']))
                output += '\n'
        return


    iter(diff_result, 1)
    output += '}'
    return output
