def format_special_val(value):
    '''
    Format special values.
    '''
    if value is False:
        result = 'false'
    elif value is True:
        result = 'true'
    elif value is None:
        result = 'null'
    else:
        result = value
    return result
