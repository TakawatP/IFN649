import serial
import time
import string
import paho.mqtt.client as mqtt

#MQTT settings
MQTT_BROKER = "3.107.83.64"
MQTT_TOPIC = "home/lighting"

#reading and writing data from and to arduino serially.
#rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

#MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
	print("Connect with result code" + str(rc))
	client.subscribe(MQTT_TOPIC)

#MQTT on_message callabck
def on_message(client, userdata, msg):
	print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

#Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_start()

while True:
  if ser.in_waiting > 0:
    rawserial = ser.readline()
    cookedserial = rawserial.decode('utf-8').strip('\r\n')
    print(cookedserial)

	#Read the LDR sensor
	ldr_value = cookedserial
		
		
	#If it's dark, send "Light ON" message
	if ldr_value == "LOW":
		client.publish(MQTT_TOPIC, "Light ON")
		print("Light ON")
	#If it's bright, send "Light OFF" message
	else:
		client.publish(MQTT_TOPIC, "Light OFF")
		print("Light OFF")
		
	#wait before checking again
	time.sleep(5)
