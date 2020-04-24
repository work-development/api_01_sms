import time

import requests
from twilio.rest import Client
import os

from dotenv import load_dotenv
load_dotenv()

def get_status(user_id):

    params = {
        'user_ids': user_id,
        'v': '5.92',
        'access_token': os.getenv("access_token"),
        'fields': 'online'
    }
    ProfileInfo = requests.post('https://api.vk.com/method/users.get', params=params)

    return ProfileInfo.json()['response'][0]['online'] # Верните статус пользователя в ВК 1-online

#print(get_status(os.getenv("vk_id")))



def sms_sender(sms_text):
    account_sid = os.getenv("account_sid")
    auth_token = os.getenv("auth_token")
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
         to = os.getenv("NUMBER_TO"),
         from_ = os.getenv("NUMBER_FROM"),
         body= sms_text
     )
    return message.sid  # Верните sid отправленного сообщения из Twilio


if __name__ == "__main__":
    vk_id = input("Введите id ")
    while True:
        if get_status(vk_id) == 1:
            sms_sender(f'{vk_id} сейчас онлайн!')
            break
        time.sleep(5)

