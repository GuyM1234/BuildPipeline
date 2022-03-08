from heimdell.core.pipeline.setup.setups import kafka, Mongo, hive
from heimdell.core.pipeline.setup.setup_config import setup_config

producers_setups = {
    'kafka': kafka
}

consumers_setups = {
    'hive': hive
}


def setup(config: dict):
    config = setup_config(config)
    producer_setup = producers_setups[config['producer']['name']]
    producer_setup(config['producer']['config'])
    for consumer_type, consumer_config in config['consumers'].items():
        consumers_setup = consumers_setups[consumer_type]
        consumers_setup(consumer_config)
    Mongo.write(config)
    return config
