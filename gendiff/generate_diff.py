import json
import os.path as path
import yaml
from gendiff.formatters.json import format_json
from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish


def generate_diff(file1, file2, format='stylish'):
    '''
    Finds differences in two files. Arguments:
    file1 - path to file1
    file2 - path to file2
    '''
    # Get file format and read files
    with open(path.abspath(file1)) as f1, open(path.abspath(file2)) as f2:
        ext1, ext2 = path.splitext(file1)[1], path.splitext(file2)[1]
        if ext1 == '.json' and ext2 == '.json':
            f1_data = json.load(f1)
            f2_data = json.load(f2)
        elif ext1 in ('.yml', '.yaml') and ext2 in ('.yml', '.yaml'):
            f1_data = yaml.full_load(f1)
            f2_data = yaml.full_load(f2)
        else:
            return 'File extension is not supported'
    # Get differences
    diff = compare_dicts(f1_data, f2_data)
    # Format differences
    if format == 'stylish':
        result = format_stylish(diff)
    elif format == 'plain':
        result = format_plain(diff)
    elif format == 'json':
        result = format_json(diff)
    else:
        result = f'{format} - is unsupported format'
    print(result)
    return result


def compare_dicts(dict1, dict2):
    '''
    Compares two dictionaries and returns list of diferences. Arguments:
    dict1 - dictionary1
    dict2 - dictionary2
    '''
    diff = []
    all_keys = list(dict1.keys() | dict2.keys())

    for i in sorted(all_keys):
        name = i  # Element name
        status = ''  # not_changed, added, removed, changed, have_children
        value = ''  # Element value if is not dict
        new_value = ''  # Element new value if value is not dict
        children = []  # List of children
        # Added
        if i not in dict1:
            status = 'added'
            new_value = dict2[i]
        # Removed
        elif i not in dict2:
            status = 'removed'
            value = dict1[i]
        # Have children
        elif type(dict1[i]) is dict and type(dict2[i]) is dict:
            status = 'have_children'
            children = compare_dicts(dict1[i], dict2[i])
        # Not changed
        elif (i in dict1 and i in dict2) and (dict1[i] == dict2[i]):
            status = 'not_changed'
            value = dict1[i]
        # Changed
        else:
            status = 'changed'
            value = dict1[i]
            new_value = dict2[i]

        element = []
        element.append(name)
        element.append(status)
        element.append(value)
        element.append(new_value)
        element.append(children)
        diff.append(element)

    return diff
