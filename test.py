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

# configg = {
#     'producer': {
#         'name': "kafka",
#         'config': {
#             'topic_name': 'sagah',
#             'num_partitions': 1,
#             'replication_factor': 1,
#             'client_id': '123pijhsdfl;jakN'
#         }
#     },
#     'consumers': {
#         'hive': {
#             'path': '/usr/home/ma29',
#             'table': 'random',
#         },
#     },
#     'validations': {
#         'scheme': {
#             'id': 'string',
#             'age': 'int',
#         },
#         'file_type': 'json'
#     }
# }

