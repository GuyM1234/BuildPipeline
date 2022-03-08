from kafka.admin import KafkaAdminClient, NewTopic
import pymongo.database

from pymongo.collection import Collection
from configuration import KAFKA_HOST, MONGO
from pymongo import MongoClient


def kafka(config: dict):
    admin_client = KafkaAdminClient(
        bootstrap_servers=KAFKA_HOST,
        client_id=config['client_id']
    )
    admin_client.create_topics([NewTopic(name=config['topic_name'], num_partitions=config['num_partitions'],
                                         replication_factor=config['replication_factor'])])


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
