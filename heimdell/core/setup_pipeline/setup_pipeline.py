from heimdell.core.pipelinebuilder.setups import kafka, Mongo, hive

producers_setups = {
    'kafka': kafka
}

consumers_setups = {
    'hive': hive
}


def setup_pipeline(config: dict):
    # consumers_setup = consumers_setups[config['consumers']['name']]
    # consumers_setup(config['consumer']['config'])
    producer_setup = producers_setups[config['producer']['name']]
    producer_settings = producer_setup(config['producer']['config'])
    Mongo.write(config)
    return producer_settings

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