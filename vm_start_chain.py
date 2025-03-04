"""EE 250L Lab 04 Starter Code
Run vm_pub.py in a separate terminal on your VM."""

import paho.mqtt.client as mqtt
import time

"""This function (or "callback") will be executed when this client receives 
a connection acknowledgement packet response from the server. """

def on_connect(client, userdata, flags, rc):
    """Once our client has successfully connected, it makes sense to subscribe to
    all the topics of interest. Also, subscribing in on_connect() means that, 
    if we lose the connection and the library reconnects for us, this callback
    will be called again thus renewing the subscriptions"""

    print("Connected to server (i.e., broker) with result code "+str(rc))
    #replace user with your USC username in all subscriptions
    client.subscribe("ralasadi/pong")

    
    #Add the custom callbacks by indicating the topic and the name of the callback handle
    client.message_callback_add("ralasadi/pong", on_message_from_ping)


"""This object (functions are objects!) serves as the default callback for 
messages received when another node publishes a message this client is 
subscribed to. By "default,"" we mean that this callback is called if a custom 
callback has not been registered using paho-mqtt's message_callback_add()."""
def on_message(client, userdata, msg):
    print("Default callback - topic: " + msg.topic + "   msg: " + str(msg.payload, "utf-8"))

#Custom message callback.
def on_message_from_ping(client, userdata, message):
   num = int(message.payload.decode()) + 1
   client.publish("ralasadi/ping", num)
   print("Publishing ping")
   time.sleep(1)
   print("Custom callback  - Ping Message: ",num)
   


if __name__ == '__main__':
    
    #create a client object
    client = mqtt.Client()
    #attach a default callback which we defined above for incoming mqtt messages
    client.on_message = on_message
    #attach the on_connect() callback function defined above to the mqtt client
    client.on_connect = on_connect

    client.connect(host="172.20.10.2", port=1883, keepalive=60)

    client.loop_start()
    num = 0

    time.sleep(1)

    #while True:
        #replace user with your USC username in all subscriptions

    client.publish("ralasadi/ping", num)
        #print("Publishing ping")
    time.sleep(1)
    #num = num + 1
    while True:
        pass
