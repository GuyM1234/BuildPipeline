def build_kafka(config: dict):
    pass


def write_to_db(config):
    mongo.write()


producers_setups = {
    'kafka': setup_kafka
}

consumers_setups = {
    'hive': setup_hive
}


def build_pipeline(config: dict):
    write(config)
    consumers_setup = producers[config['producer']['name']]
    consumers_setup(config['consumer']['config'])
    producers_setup = producers[config['producer']['name']]
    producer_settings = producers_setup(producer['config'])
    return producer_settings

