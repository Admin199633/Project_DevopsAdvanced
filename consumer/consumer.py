import pika
import time
import random
from prometheus_client import start_http_server, Summary, Counter, Gauge

#PROGRESS = Gauge('server_requests_inprogress', 'Number of requests in progress')

def on_message_received(ch, method, properties, body):
    processing_time = random.randint(1, 6)
    print(f'received: "{body}", will take {processing_time} to process')
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(f'finished processing and acknowledged message')
    print("Massages left in the queue")
    print(ch.queue_declare(queue='pc', exclusive=False, auto_delete=False).method.message_count)



def consumer():
    credentials = pika.PlainCredentials('user', 'Lior12345')
    connection_parameters = pika.ConnectionParameters('127.0.0.1',
                                                      5672,
                                                      '/',
                                                      credentials)
    # connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()
    channel.queue_declare(queue='pc')

    channel.basic_qos(prefetch_count=1)

    channel.basic_consume(queue='pc', on_message_callback=on_message_received)
    print("Massages left in the queue")
    # show number of massages left in the queue
    q=(channel.queue_declare(queue='pc', exclusive=False, auto_delete=False).method.message_count)
    print (q)
    #### prometheus

    #### prometheus


    print('Starting Consuming')
    channel.start_consuming()


# --connection_parameters = pika.ConnectionParameters('user:Yahel123@localhost')

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

c = Counter('my_failures', 'Description of Yahel counter')
c.inc()  # Increment by 1
c.inc(1.6)  # Increment by given value


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    #    time.sleep(t)
    consumer()



if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(9422)
    # Generate some requests.
    while True:
        process_request(random.random())
