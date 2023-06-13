import os
import vk_api
from vk_api import exceptions
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import threading
import time
from multiprocessing import Process
import db

import proccess

UPSKILLS_TOKEN = 'vk1.a.JviNokvKmaOO0CUhFFSLUWIEszm2IGfTEcHBee1Sd_co-bGHkrrMu6N-DsIQZzignvMjX95vWquwatGdhR0CZMMBdFA3G-CoTJO_cgoKezjbeFjd39x2NgM3O7s4cxbi0n9fe9THcFXHyJUa_BT4FXRCKb05Mnc8oH7bbXDpUePRO2v7dpCr6gb34UftQ2tx'
GROUP_ID = '201905325'
vk_session = vk_api.VkApi(token=UPSKILLS_TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

def bot():
    time.sleep(30)
    db.make_db()
    db.make_table()
    while True:
        for event in longpoll.listen():

            if event.type == VkBotEventType.GROUP_JOIN:
                e_id = str(event.object['user_id'])
                print('\n\n'+e_id+' joined the group\n\n')
                event_data = event.object 
                threading.Thread(target=proccess.p_join, args=(event_data,)).start()

            if event.type == VkBotEventType.MESSAGE_ALLOW:
                event_data = event.object 
                threading.Thread(target=proccess.p_allow, args=(event_data,)).start()

            if event.type == VkBotEventType.GROUP_LEAVE:
                e_id = str(event.object['user_id'])
                print('\n\n'+e_id+' left the group\n\n')
                event_data = event.object 
                threading.Thread(target=proccess.p_leave, args=(event_data,)).start() 

            if event.type == VkBotEventType.MESSAGE_NEW and event.from_user:
                event_data = event.message
                threading.Thread(target=proccess.p_message, args=(event_data,)).start()

if __name__ == '__main__':
    # Exception = exceptions.ApiError
    arr = [1,2]
    for i in arr:
        try:
            bot()
        except Exception as e:
            print('\n\n---BOT EXEPTION---\n\n')
            print(e)
            print('\n\n---END OF EXEPTION---\n\n')
            continue
        arr.append(1)
        print(arr)

