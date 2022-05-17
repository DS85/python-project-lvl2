import json
import os.path as path
import yaml


def generate_diff(file1, file2):
    # Get file format and read files
    ext1, ext2 = path.splitext(file1)[1], path.splitext(file2)[1]
    with open(path.abspath(file1)) as f1, open(path.abspath(file2)) as f2:
        if ext1 == '.json' and ext2 == '.json':
            f1_data = json.load(f1)
            f2_data = json.load(f2)
        elif ext1 in ('.yml', '.yaml') and ext2 in ('.yml', '.yaml'):
            f1_data = yaml.full_load(f1)
            f2_data = yaml.full_load(f2)
        else:
            return 'File extension is not supported'

    # Form list of keys for searching in files and sorting:
    elements_list = list()
    for k in f1_data.keys():
        if k not in elements_list:
            elements_list.append(k)
    for k in f2_data.keys():
        if k not in elements_list:
            elements_list.append(k)
    elements_list.sort()

    # Form dictionary with files differences
    result_dict = {}
    for i in elements_list:
        if i in f1_data and i in f2_data:  # If elements in both files:
            if f1_data[i] == f2_data[i]:  # And values are equal:
                result_dict[f'  {i}'] = f1_data[i]
            else:  # And values are not equal:
                result_dict[f'- {i}'] = f1_data[i]
                result_dict[f'+ {i}'] = f2_data[i]
        else:  # If elements are not in both files:
            if i in f1_data:  # If element in file1 only:
                result_dict[f'- {i}'] = f1_data[i]
            else:  # If element in file2 only:
                result_dict[f'+ {i}'] = f2_data[i]

    return json.dumps(result_dict, indent=2)
