from heimdell.core.utils.exceptions import ProducerNotSupported, ConsumerNotSupported

keys = ['sagah', 'username', 'producer', 'consumers', 'validations']
producer_names = ['kafka']
consumer_names = ['hive', 'elastic', 'oracle']


def get_missing_keys(config):
    missing_keys = [key for key in keys if not is_key_exists(key, config)]
    if 'producer' not in missing_keys and not is_key_exists('name', config['producer']):
        missing_keys.append('producer/name')
    if 'consumers' not in missing_keys and \
            not any(consumer_name in config['consumers'].keys() for consumer_name in consumer_names):
        missing_keys.append('consumers/name')
    return missing_keys


def validate_values(config: dict):
    if not config['producer']['name'] in consumer_names:
        raise ProducerNotSupported()
    for consumer_name in config['consumers'].keys():
        if consumer_name not in consumer_names:
            raise ConsumerNotSupported()


def enrich(config: dict):
    pass


def is_key_exists(key: str, config: dict):
    return config.get(key) is not None
