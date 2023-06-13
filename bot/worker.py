import os
import random
import main 
import db

MANAGER_ID = '240345909'

def send_msg(peer_id, botmessage=None, keyboard=None, photo=None):
    rnd = random.randint(1, 100000)
    post = {
        'peer_id': peer_id,
        'message': botmessage,
        'random_id': rnd,
        }

    if keyboard is not None:
        post['keyboard'] = keyboard.get_keyboard()

    if photo is not None:
        post["attachment"] = photo

    main.vk_session.method('messages.send', post)

def send_form(peer_id):
    rnd = random.randint(1, 100000)
    form = db.get_form(peer_id)
    botmessage = 'Новая заявка из группы ВК!\n\nИмя: '+str(form['name'])+'\nВозраст: Ребёнок\nБассейн: '+str(form['pool'])+'\nНаправление: '+str(form['type'])+'\nГруппа: '+str(form['age'])+'\nТренер: '+str(form['trainer'])+'\nТелефон: '+str(form['phone'])
    if form['adult'] == 'adult':
        botmessage = 'Новая заявка из группы ВК!\n\nИмя: '+str(form['name'])+'\nВозраст: Взрослый\nБассейн: '+str(form['pool'])+'\nНаправление: '+str(form['type'])+'\nГруппа: '+str(form['age'])+'\nТренер: '+str(form['trainer'])+'\nТелефон: '+str(form['phone'])
    post = {
        'peer_id': MANAGER_ID,
        'message': botmessage,
        'random_id': rnd,
        }
    
    main.vk_session.method('messages.send', post)
