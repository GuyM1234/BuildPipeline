import requests
MINIMAL_CONFIG = {
    # 'sagah': '',
    'username': '',
    'producer': {
        'name': 'd',
    },
    'consumers': {
        'hive': None,
    },
    'validations': {
        'scheme': {
            '': '',
        },
        'file_type': ''
    }
}
print(MINIMAL_CONFIG)
x = requests.post("http://localhost:5000/", data=MINIMAL_CONFIG)
print(x.json())



