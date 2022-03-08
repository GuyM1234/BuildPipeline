import requests

config = {
    'producer': {
        'name': "kafka",
        'config': {
            'topic': 'sagah',
            'num_partitions': 1,
            'replication_factor': 1,
            'client_id': '123pijhsdfl;jakN'
        }
    },
    'consumers': [{
        'name': 'hive',
        'config': {
            'tables': [{
                'table_name': 'new_guy'
            }]
        }
    }],
    'validations': {
        'scheme': {
            'id': str,
            'age': int,
        },
        'file_type': 'json'
    }
}

x = requests.post("http://localhost:5000/", data=config)
print(x)