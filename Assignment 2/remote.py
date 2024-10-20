import paho.mqtt.publish as publish

MQTT_TOPIC = "home/lighting"
MQTT_HOSTNAME = "13.55.201.188"

def control_lighting(topic, hostname):
    while True:
        mode = input("Enter mode (AUTO, MANUAL, Light ON, Light OFF) or type 'EXIT' to quit: ").strip().upper()

        if mode == "EXIT":
            print("Exiting the program.")
            break
        elif mode == "AUTO":
            publish.single(topic, "AUTO", hostname=hostname)
        elif mode == "MANUAL":
            publish.single(topic, "MANUAL", hostname=hostname)
        elif mode == "LIGHT ON":
            publish.single(topic, "Light ON", hostname=hostname)
        elif mode == "LIGHT OFF":
            publish.single(topic, "Light OFF", hostname=hostname)
        else:
            print("Invalid mode selected.")
            continue
        
        print(f"Mode '{mode}' selected. Command sent successfully.")

control_lighting(MQTT_TOPIC, MQTT_HOSTNAME)
