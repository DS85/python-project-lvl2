import json


def format_json(diff):
    result = convert_list_to_dict(diff)
    return json.dumps(result, indent=4)


def convert_list_to_dict(list):
    result = []
    for i in list:
        element = {}
        element['name'] = i[0]
        element['status'] = i[1]
        element['value'] = i[2]
        element['new_value'] = i[3]
        element['children'] = i[4]
        if i[1] == 'have_children':
            element['children'] = convert_list_to_dict(i[4])
        result.append(element)
    return result
