import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import numpy as np
from config import TOKEN, id_сообщества

def main():
    vk_session = vk_api.VkApi(
        token=TOKEN)

    longpoll = VkBotLongPoll(vk_session, id_сообщества)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj.message['from_id'])
            print('Текст:', event.obj.message['text'])
            vk = vk_session.get_api()
            try:
                vk.messages.send(user_id=event.obj.message['from_id'],
                             message=f"Спасибо, что написали нам <{event.obj.message['text']}>. Мы обязательно ответим",
                             random_id=random.randint(2 ** 33, 2 ** 64))
            except Exception as e:
                print(f'ошибка: {e.__str__()}')

if __name__ == '__main__':
    main()