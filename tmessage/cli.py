import paho.mqtt.client as mqtt
import argparse
from colorama import init, deinit, Fore, Back, Style
from datetime import datetime
import os
import json
import tmessage.auth as auth  # auth.py

# Initialize colorama
init()

# Create the parser
parser = argparse.ArgumentParser(prog='AMU-OSS-MESSAGING',
                                 description='cli based group messaging\
                                 for amu-oss sessions',
                                 epilog='Happy learning !')

# Add the arguments
parser.add_argument('--user', action='store', type=str, required=True)
parser.add_argument('--server', action='store', type=str)
parser.add_argument('--port', action='store', type=int)
parser.add_argument('--store',
                    action='store_true',
                    help='Store messages in JSON format.')

args = parser.parse_args()

IS_STORE = args.store
MQTT_TOPIC = "amu"
BROKER_ENDPOINT = args.server or "test.mosquitto.org"
BROKER_PORT = args.port or 1883


mqtt_client = mqtt.Client()
current_user = args.user


def on_message(client, userdata, message):
    current_msg = message.payload.decode("utf-8")

    # to get the username between []
    user = current_msg.partition('[')[-1].rpartition(']')[0]
    if user != current_user:
        print(Back.GREEN + Fore.BLACK + current_msg +
              Back.RESET + Fore.RESET + "")
        _, _, message = current_msg.partition('] ')
        if IS_STORE:
            store_messages(user, message)


folder_name = 'messages'
session_start_date = datetime.now().strftime('%Y-%m-%d_%H:%M')

data = {}


def store_messages(user, raw_msg):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    data['time'] = datetime.now().strftime('%Y-%m-%d %H:%M')
    data['content'] = raw_msg
    data['from'] = user

    with open('messages/{}.json'.format(session_start_date), 'a', encoding='utf-8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)


def main():
    try:
        if auth.checkExisted(current_user):
            password = input(f'User {current_user} found\nEnter password: ')
            payload = auth.authenticate(current_user, password)
        else:
            print(f'Welcome {current_user} to tmessage!\nPlease register...')
            displayed_name = input(f'Enter your name used for display: ')
            password = input(f'Enter password: ')
            password_confirm = input(f'Re-enter password: ')
            while password != password_confirm:
                print('Passwords do not match, please try again...')
                password = input(f'Enter password: ')
                password_confirm = input(f'Re-enter password: ')
            payload = auth.register(current_user, displayed_name,
                                    password, password_confirm)
        print('User Authorized')
        user_name = payload["user_name"]
        displayed_name = payload["displayed_name"]

        mqtt_client.on_message = on_message
        mqtt_client.connect(BROKER_ENDPOINT, BROKER_PORT)
        mqtt_client.subscribe(MQTT_TOPIC)
        mqtt_client.loop_start()
        while True:
            raw_msg = str(input(Back.RESET + Fore.RESET))
            pub_msg = f'[{user_name}] {displayed_name}: {raw_msg}'
            if raw_msg != '':
                mqtt_client.publish(MQTT_TOPIC, pub_msg)
                if IS_STORE:
                    store_messages(current_user, raw_msg)
            else:
                print(Back.WHITE + Fore.RED +
                      "Can't send empty message", end='\n')
    except KeyboardInterrupt:
        mqtt_client.disconnect()
        Style.RESET_ALL
        deinit()
        print('\ngoodbye !')
    except ConnectionRefusedError:
        Style.RESET_ALL
        deinit()
        print("\nCan't connect please check your network connection")
    except Exception as err:
        Style.RESET_ALL
        deinit()
        print(f'\n{err}')


if __name__ == "__main__":
    main()
