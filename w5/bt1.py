import paho.mqtt.client as mqtt
import serial

def on_connect(client, userdata, flags, rc): # func for making connection
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    client.subscribe("ifn649")
def on_message(client, userdata, msg): # Func for Sending msg
    print(msg.topic+" "+str(msg.payload))
    ser = serial.Serial("/dev/rfcomm0", 9600)
    ser.write(msg.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("3.107.83.64", 1883, 60)

client.loop_forever()

