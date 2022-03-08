# from kafka.admin import KafkaAdminClient, NewTopic
from config import KAFKA_HOST


def kafka(config: dict):
    # admin_client = KafkaAdminClient(
    #     bootstrap_servers=KAFKA_HOST,
    #     client_id=config.client_id
    # )
    # admin_client.create_topics([NewTopic(name=config.topic_name, num_partitions=config.num_partitions,
    #                                      replication_factor=config.replication_factor)])
    return config


def hive(config: dict):
    pass
