import setups

producers_setups = {
    'kafka': setups.kafka
}

consumers_setups = {
    'hive': setups.hive
}


def build_pipeline(config: dict):
    # write(config)
    consumers_setup = producers[config['producer']['name']]
    consumers_setup(config['consumer']['config'])
    producers_setup = producers[config['producer']['name']]
    producer_settings = producers_setup(producer['config'])
    return producer_settings
