import paho.mqtt.publish as publish

publish.single("home/lighting", "Light ON", hostname="13.55.201.188")
print("Done")
