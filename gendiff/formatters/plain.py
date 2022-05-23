from gendiff.formatters.common import format_special_val


def format_plain(diff, level=0,  addr=[]):
    '''
    Format list of differences into "plain" view. Arguments:
    diff - list of differences
    level - level of nesting
    addr - path to element
    '''
    result = ''
    diff.sort()
    for i in diff:
        while level < len(addr):
            addr.pop()
        if level == len(addr):
            addr.append(i[0])

        if i[1] == 'added':
            result += f'Property \'{".".join(addr)}\' was added '
            result += f'with value: {format_plain_val(i[3])}\n'
        elif i[1] == 'removed':
            result += f'Property \'{".".join(addr)}\' was removed\n'
        elif i[1] == 'changed':
            result += f'Property \'{".".join(addr)}\' was updated. From '
            result += f'{format_plain_val(i[2])} to {format_plain_val(i[3])}\n'
        elif i[1] == 'have_children':
            result += format_plain(i[4], level+1, addr)
    return result


def format_plain_val(value):
    '''
    Format values for "plain" view.
    '''
    if type(value) is dict:
        result = '[complex value]'
    else:
        result = format_special_val(value)
        if result not in ('false', 'true', 'null') and type(result) != int:
            result = f"'{result}'"
    return result
