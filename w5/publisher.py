import paho.mqtt.publish as publish

publish.single("ifn649", "LED_ON", hostname="3.107.83.64")
print("Done")
