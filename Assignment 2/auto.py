import paho.mqtt.publish as publish

publish.single("home/lighting", "AUTO", hostname="13.55.201.188")
print("Done")
