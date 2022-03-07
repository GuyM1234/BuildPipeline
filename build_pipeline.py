def build_kafka(config: dict):
    pass


def write(config):
    mongo.write()


producers = {
    'kafka': buildkakfa
}

consumers = {
    'hive': buildkakfa
}


def build(config: dict):
    producers[config['producer']['name']](config['producer']['config'])
    consumers[config['consumer']['name']](config['consumer']['config'])
    write(config)


config = {
    producer: {
        name: "kafka",
        config: {
            topic:
            part: 1
        }
    },
    consumer: [{
        name: 'hive',
        tables: [{

        }]
    }]
}