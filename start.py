import eel
import telethon

eel.init("web")


@eel.expose
def save_api_config(api_id, api_hash):
    client = telethon.TelegramClient('anon', api_id, api_hash)
    with open('api_config.txt', 'w') as config_file:
        config_file.write('\n'.join([api_id, api_hash]))
    client.disconnect()
    return True


eel.start('main.html', size=(400, 700))
