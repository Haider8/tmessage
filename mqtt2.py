import paho.mqtt.client as mqtt

MQTT_TOPIC = "amu"
BROKER_ENDPOINT = "192.168.43.235"
BROKER_PORT = 1883


mqtt_client = mqtt.Client()
current_msg = ""
current_user = "Haider8"

def on_message(client, userdata, message):
    current_msg = message.payload.decode("utf-8")
    user = current_msg.partition('[')[-1].rpartition(']')[0]  # to get the username between []
    if current_msg != message.payload.decode("utf-8"):
        print(user + current_msg)
    
    if user != current_user:
        print(current_msg)

def main():
    try:
        mqtt_client.on_message = on_message
        mqtt_client.connect(BROKER_ENDPOINT, BROKER_PORT)
        mqtt_client.subscribe(MQTT_TOPIC)
        mqtt_client.loop_start()
        while True:
            temperature = str(input())
            current_msg = temperature
            mqtt_client.publish(MQTT_TOPIC, temperature)
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        print('\ngoodbye !')


if __name__ == '__main__':
    main()