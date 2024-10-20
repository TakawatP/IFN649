import serial
import time
import string
import paho.mqtt.client as mqtt

# MQTT settings
MQTT_BROKER = "13.55.201.188"
MQTT_TOPIC = "home/lighting"
LOG_FILE = "mqtt_log.txt"  # Log file for MQTT messages

# Track control mode (default: automatic)
control_mode = "AUTO"  # Can be "AUTO" or "MANUAL"

# reading and writing data from and to Arduino serially.
# rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))

# MQTT on_connect callback
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(MQTT_TOPIC)

# MQTT on_message callback
def on_message(client, userdata, msg):
    global control_mode
    ser.write(msg.payload)
    # Log message to a text file
    with open(LOG_FILE, 'a') as f:
        f.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - Received message: {msg.payload.decode()} on topic: {msg.topic}\n")
    
    # Check if the message is a control command
    if msg.topic == "home/lighting":
        command = msg.payload.decode().upper()
        print(command)
        
        if command == "AUTO":
            control_mode = "AUTO"
            print("Switched to automatic mode.")
        elif command == "MANUAL":
            control_mode = "MANUAL"
            print("Switched to manual mode.")
        elif control_mode == "MANUAL" and command in ["Light ON", "Light OFF"]:
            # Manual control of lights
            client.publish(MQTT_TOPIC, command)
            print(f"Manual command: {command}")
        else:
            print("Invalid control command or mode.")
    else:
        print(f"Received message: {msg.payload.decode()} on topic: {msg.topic}")

# Setup MQTT client
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, 1883, 60)
client.loop_start()

while True:
    if control_mode == "AUTO":
        # Automatic mode - read from the LDR sensor
        if ser.in_waiting > 0:
            if control_mode == "AUTO":
                rawserial = ser.readline()
                cookedserial = rawserial.decode('utf-8').strip('\r\n')
                print(cookedserial)

                # Read the LDR sensor
                ldr_value = cookedserial

                # If it's dark, send "Light ON" message
                if ldr_value == "LOW":
                    client.publish(MQTT_TOPIC, "Light OFF")
                    print("Light OFF")
                # If it's bright, send "Light OFF" message
                else:
                    client.publish(MQTT_TOPIC, "Light ON")
                    print("Light ON")

                # Wait before checking again
                time.sleep(1)
                #print(control_mode)
            else:
                break
    else:
        # Manual mode - no automatic updates
        time.sleep(1)
