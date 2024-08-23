import paho.mqtt.publish as publish

publish.single("ifn649", "Hello World", hostname="3.107.83.64")
print("Done")
