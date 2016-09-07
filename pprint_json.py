import json


def load_data(filepath):
    with open(filepath,'r') as json_file:
        return json.loads(json_file.read())


def pretty_print_json(data):
    print(json.dumps(data, indent = 4, ensure_ascii = False))


if __name__ == '__main__':
    data = load_data(input('Введите путь к файлу с json: '))
    pretty_print_json(data)
    pass
