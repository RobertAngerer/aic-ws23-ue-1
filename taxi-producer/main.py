from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="localhost:29092",
    security_protocol='PLAINTEXT',
    client_id='test'
)

topic_list = []
topic_list.append(NewTopic(name="taxis", num_partitions=1, replication_factor=1))
admin_client.create_topics(new_topics=topic_list, validate_only=False)












