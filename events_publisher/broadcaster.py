from kafka import KafkaProducer, KafkaClient


class EventBroadcaster(object):
    def __init__(self, topic="default"):
        self.topic = topic
        self.kafka_server = "localhost:9092"
        self.ensure_topic()

    def ensure_topic(self):
        cli = KafkaClient(bootstrap_servers=self.kafka_server)
        resp = cli.add_topic(self.topic)
        print(resp)

    def send_dummy_events(self, event_num):
        producer = KafkaProducer(bootstrap_servers=self.kafka_server)
        for i in range(event_num):
            msg = f"this is message number {i}"
            producer.send(self.topic, msg.encode(encoding="utf-8"))
            print(msg)
