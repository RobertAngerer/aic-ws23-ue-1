import json
import csv

from kafka import KafkaProducer
def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

def on_send_error(excp):
    print('I am an errback')
    print(excp)
    # handle exception

record = {}
producer = KafkaProducer(bootstrap_servers=['localhost:29092'], value_serializer=lambda m: json.dumps(m).encode('ascii'))
with open('taxi_data/taxi_log_2008_by_id/1.txt', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        record['key'] = row[0]
        record['datetime'] = row[1]
        record['long'] = row[2]
        record['lat'] = row[3]
        print(record)
        producer.send('taxis', record, bytes(row[0], 'utf-8')).add_callback(on_send_success).add_errback(on_send_error)
        record = {}


# # produce json messages
# producer.send('taxis', {'key': 'value'}, key=)