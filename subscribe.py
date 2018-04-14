import paho.mqtt.client as mqtt #import the client1


def on_connect(client, obj, flags, rc):
  print("rc: " + str(rc))


def on_message(client, obj, msg):
  print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(client, obj, mid):
  print("mid: " + str(mid))


def on_subscribe(client, obj, mid, granted_qos):
  print("Subscribed: " + str(mid) + " " + str(granted_qos))


broker_address="iot.eclipse.org"

client = mqtt.Client()

client.on_message=on_message
client.on_message = on_message
client.on_connect = on_connect
client.on_publish = on_publish
client.on_subscribe = on_subscribe

client.connect(broker_address) #connect to broker

client.subscribe("topic1")

client.loop_forever()