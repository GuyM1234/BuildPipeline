# from kafka.admin import KafkaAdminClient, NewTopic
import pymongo.database
from pymongo.collection import Collection
from setup_configs import KAFKA_HOST, MONGO
from pymongo import MongoClient


def kafka(config: dict):
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_HOST,
        client_id=config.client_id
    )
    admin_client.create_topics([NewTopic(name=config.topic_name, num_partitions=config.num_partitions,
                                         replication_factor=config.replication_factor)])


def hive(config: dict):
    pass


class Mongo:
    @staticmethod
    def write_config(config: dict):
        client = MongoClient(MONGO['host'], MONGO['port'])
        db = client.get_database(MONGO['db_name'])
        collection = db.get_collection(MONGO['collection_name'])
        config = Mongo.combine_consumers_config(config, collection)
        added_doc = collection.insert_one(config)
        return added_doc.inserted_id

    @staticmethod
    def combine_consumers_config(config: dict, collection: dict):
        similar_pipelines = collection.find({"validations.scheme": config['validations']['scheme']})
        try:
            similar_pipeline_config = similar_pipelines.next()
            for consumer_type, consumer_config in similar_pipeline_config['consumers'].items():
                config['consumers'][consumer_type] = consumer_config
        except StopIteration:
            pass
        return config


configg = {
    'producer': {
        'name': "kafka",
        'config': {
            'topic': 'sagah',
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
Mongo.write_config(configg)
