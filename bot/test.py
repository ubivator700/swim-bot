import os
import db
import worker
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

UPSKILLS_TOKEN = os.environ.get('UPSKILLS_TOKEN')
GROUP_ID = os.environ.get('GROUP_ID')
vk_session = vk_api.VkApi(token=UPSKILLS_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
        id = event.message['peer_id']
        worker.send_form(id)
