import telethon
import time

DELAY = 2
API_CONFIG_FILE = 'api_config.txt'
UNVERIFIED_USERS_FILE = 'list_for_users_to_check.txt'


def load_api_config():
    with open(API_CONFIG_FILE, 'r') as config_file:
        return config_file.read().split('\n')


def load_unverified_users():
    with open(UNVERIFIED_USERS_FILE, 'r') as file:
        return file.read().split('\n')


api_id, api_hash = load_api_config()
unverified_users = load_unverified_users()

for unverified_user in unverified_users:
    with telethon.TelegramClient('anon', api_id, api_hash) as client:
        time.sleep(3)
        try:
            user = client.loop.run_until_complete(client.get_entity(unverified_user))
        except ValueError:
            print(f'{unverified_user} имя свободно')
            continue
        print(f'{unverified_user} имя занято')

# if __name__ == '__main__':
#     print(load_api_config())
