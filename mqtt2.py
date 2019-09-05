import paho.mqtt.client as mqtt

MQTT_TOPIC = "amu"
BROKER_ENDPOINT = "192.168.43.235"
BROKER_PORT = 1883

mqtt_client = mqtt.Client()

def on_message(client, userdata, message):
   print("Message Recieved from broker: " + message.payload.decode("utf-8"))

def main():
    try:
        mqtt_client.on_message = on_message
        mqtt_client.connect(BROKER_ENDPOINT, BROKER_PORT)
        mqtt_client.subscribe(MQTT_TOPIC)
        mqtt_client.loop_forever()
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        print('\ngoodbye !')
    

if __name__ == '__main__':
    main()