# python msg.py --user pnijhara

import paho.mqtt.client as mqtt
import argparse

# Create the parser
parser = argparse.ArgumentParser(prog='AMU-OSS-MESSAGING',
                                    description='cli based group messaging for amu-oss sessions',
                                    epilog='Happy learning !')

# Add the arguments
parser.add_argument('--user', action='store', type=str, required=True)
parser.add_argument('--server', action='store', type=str)

args = parser.parse_args()

MQTT_TOPIC = "amu"
BROKER_ENDPOINT = args.server
BROKER_PORT = 1883


mqtt_client = mqtt.Client()
current_user = args.user

def on_message(client, userdata, message):
    current_msg = message.payload.decode("utf-8")
    user = current_msg.partition('[')[-1].rpartition(']')[0]  # to get the username between []
    if user != current_user:
        print(current_msg)

def main():
    try:
        mqtt_client.on_message = on_message
        mqtt_client.connect(BROKER_ENDPOINT, BROKER_PORT)
        mqtt_client.subscribe(MQTT_TOPIC)
        mqtt_client.loop_start()
        while True:
            raw_msg = str(input())
            pub_msg = '[' + current_user + '] ' + raw_msg
            if raw_msg != '':
                mqtt_client.publish(MQTT_TOPIC, pub_msg)
            else:
                print("can't send empty message", end='')
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        print('\ngoodbye !')


if __name__ == '__main__':
    main()
