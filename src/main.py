from kafka import KafkaProducer

from src.config.logger import logger
from src.config.core import Config
from src.sinks import KafkaSink
from src.twitter.core import TwitterApi, TwitterStream
from src.twitter.filters import filters


def main():
    config = Config.build()

    api = TwitterApi.build(auth_config=config.auth)
    kafka_producer = KafkaProducer(bootstrap_servers=config.sink.kafka.url)
    kafka_sink = KafkaSink(topic=config.sink.kafka.topic, producer=kafka_producer)

    logger.info('Running...')
    stream = TwitterStream.build(api=api, filters=filters, sink=kafka_sink)
    stream.run()


if __name__ == '__main__':
    main()
