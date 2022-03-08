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
    # consumers_setup = consumers_setups[config['consumers']['name']]
    # consumers_setup(config['consumer']['config'])
    producer_setup = producers_setups[config['producer']['name']]
    producer_setup(config['producer']['config'])
    Mongo.write(config)
    return config

