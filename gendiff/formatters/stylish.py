from gendiff.formatters.common import format_special_val


def format_stylish(diff, level=0):
    '''
    Formats list of differences into "stylish" view. Arguments:
    diff - list of differences
    level - level of nesting to count correct indent
    '''
    indent = '  '
    for _ in range(level):
        indent += '    '
    result = '{\n'
    for i in diff:
        if i[1] == 'added':
            result += f'{indent}+ {i[0]}: {format_stylish_val(i[3], indent)}\n'
        elif i[1] == 'removed':
            result += f'{indent}- {i[0]}: {format_stylish_val(i[2], indent)}\n'
        elif i[1] == 'not_changed':
            result += f'{indent}  {i[0]}: {format_stylish_val(i[2], indent)}\n'
        elif i[1] == 'changed':
            result += f'{indent}- {i[0]}: {format_stylish_val(i[2], indent)}\n'
            result += f'{indent}+ {i[0]}: {format_stylish_val(i[3], indent)}\n'
        elif i[1] == 'have_children':
            result += f'{indent}  {i[0]}: '
            result += format_stylish(i[4], level + 1)
    result += f'{indent[:-2]}}}\n'
    return result


def format_stylish_val(value, indent):
    '''
    Format values for "stylish" view. Arguments:
    value
    indent - indent for values with dict type
    '''
    result = ''
    indent += '    '
    if type(value) is dict:
        result = '{\n'
        for k, v in value.items():
            result += f'{indent}  {k}: {format_stylish_val(v, indent)}\n'
        result += f'{indent[:-2]}}}'
    else:
        result = format_special_val(value)
    return result
