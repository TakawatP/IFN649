import paho.mqtt.publish as publish

publish.single("home/lighting", "MANUAL", hostname="13.55.201.188")
print("Done")
