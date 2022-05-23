from gendiff.stylish_formatter import stylish_formatter

def render_diff_result(diff_result, format='stylish'):
    if format == 'stylish':
        return stylish_formatter(diff_result)
    elif format == 'plain':
        return # plain_render(diff_result)
