import json


def json_encode(func_list):
    return json.dumps({"func_list": func_list})

def json_decode(func_string):
    return json.loads(func_string)

def get_json_from_list(func_list):
    return json_encode(func_list)


def get_list_from_json(func_string):
    return json_decode(func_string)

