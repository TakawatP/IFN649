import paho.mqtt.publish as publish

publish.single("home/lighting", "Light OFF", hostname="3.107.83.64")
print("Done")
