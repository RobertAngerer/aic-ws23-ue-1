from kafka import KafkaAdminClient
from kafka.admin import NewTopic

admin_client = KafkaAdminClient(
    bootstrap_servers="broker:9092",
    client_id='test'
)

taxis = NewTopic('taxis', 3, 3)

admin_client.create_topics(taxis)











