import requests

x = requests.post("http://localhost:5000/", data=config)
print(x)

configg = {
    'producer': {
        'name': "kafka",
        'config': {
            'topic_name': 'sagah',
            'num_partitions': 1,
            'replication_factor': 1,
            'client_id': '123pijhsdfl;jakN'
        }
    },
    'consumers': {
        'hive': {
            'path': '/usr/home/ma29',
            'table': 'random',
        },
    },
    'validations': {
        'scheme': {
            'id': 'string',
            'age': 'int',
        },
        'file_type': 'json'
    }
}
MINIMAL_CONFIG = {
    'sagah': '',
    'username': '',
    'producer': {
        'name': '',
    },
    'consumers': {
        # 'hive': None,
    },
    'validations': {
        'scheme': {
            '': '',
        },
        'file_type': ''
    }
}
print(MINIMAL_CONFIG['consumers'])
