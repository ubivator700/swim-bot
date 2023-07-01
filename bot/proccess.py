import worker
import db
import blocks
import keyboards
import blocks
import texts

def p_leave(data):
    user_id = data['user_id']
    worker.send_msg(user_id, 'Возвращайся)')
    db.delete_user(user_id)
    return

def p_join(data):
    user_id = data['user_id']
    db.add_user(user_id)
    worker.send_msg(user_id, 'Спасибо за подписку')
    worker.send_msg(user_id, keyboard=keyboards.start_keyboard, botmessage='Привет! \nЯ искусственный интеллект от Школы плавания Swim Shot🐬\n\nЯ знаю актуальное расписание и стоимость занятий, могу познакомить с Тренерским составом, помочь выбрать подходящий бассейн и записаться на пробную тренировку. \nДавай общаться📲')
    return
    
def p_allow(data):
    user_id = data['user_id']
    worker.send_msg(user_id, 'Спасибо за подписку')
    worker.send_msg(user_id, keyboard=keyboards.start_keyboard, botmessage='Привет! \nЯ искусственный интеллект от Школы плавания Swim Shot🐬\n\nЯ знаю актуальное расписание и стоимость занятий, могу познакомить с Тренерским составом, помочь выбрать подходящий бассейн и записаться на пробную тренировку. \nДавай общаться📲')
    return

def p_message(event_data):
    user_id = event_data['peer_id']
    msg_text = event_data['text']
    position = db.get_position(user_id)
    user_name = db.get_name(user_id)
    user_pool = db.get_pool(user_id)
    adult = db.get_adult(user_id)
    kid_type = db.get_type(user_id)
    user_phone = db.get_phone(user_id)
    user_age = db.get_age(user_id)
    user_data = {
        'user_id': user_id,
        'msg_text': msg_text,
        'position': position,
        'user_name': user_name,
        'user_pool': user_pool,
        'adult': adult,
        'kid_type': kid_type,
        'user_phone': user_phone,
        'user_age': user_age
    }

    if position == 'nachat' and event_data['text'] == 'Начать':
        worker.send_msg(user_id, texts.meet)
        db.set_position(user_id, 'name')

    if position == 'name':
        db.set_name(user_id, msg_text)
        db.set_position(user_id, 'info')
        uname = db.get_name(user_id)
        worker.send_msg(user_id, keyboard=keyboards.info_keyboard, botmessage='Отлично! \n\n' + uname + ', для начала немного расскажу о Swim Shot. \n\nЖми кнопку «Что такое Swim Shot?». Но если хочешь пропустить этот шаг, нажми на «Давай сразу к делу»', )
                    
    if position == 'info' and msg_text == 'Что такое Swim Shot? 🤔' or msg_text == 'Давай сразу к делу':
        if msg_text == 'Что такое Swim Shot? 🤔':
            worker.send_msg(user_id, botmessage = 'Swim Shot – крупнейшая Школа плавания в Зеленограде по количеству довольных учеников!\n\n👉🏻Самое главное для нас: наслаждение от того, что делаешь, поэтому мы обучаем плавать только в кайф\n\nМы:\n💧обучаем плаванию с нуля\n💧подготавливаем к соревнованиям\n💧улучшаем технику\n\n🔹 Групповые занятия для детей с 2 лет и взрослых любого возраста и уровня подготовки\n🔹 Самостоятельное плавание без Тренера как с разовой оплатой, так и по абонементам разной длительности\n\n✔️ Ежедневно нас посещают более 200 человек\n✔️ У нас более 1000 довольных пловцов в Зеленограде\n✔️ Наши Тренеры – Мастера спорта, участники Олимпийских игр, Чемпионатов мира и Европы\n\nКстати, пробная тренировка в Swim Shot по цене чашки кофе☕️')
        worker.send_msg(user_id, keyboard=keyboards.adult_keyboard, botmessage = user_name + ', теперь задам пару вопросов, чтобы предложить именно то, что для тебя будет полезно. Для кого интересуешься занятиями?')
        db.set_position(user_id, 'kid/adult')

    if position == 'kid/adult':
        blocks.kid_adult(user_data)

    if adult == 'kid':
        if user_data['position'] == 'kid-pool':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid/adult')
                worker.send_msg(user_id, keyboard=keyboards.adult_keyboard, botmessage = user_name + ', теперь задам пару вопросов, чтобы предложить именно то, что для тебя будет полезно. Для кого интересуешься занятиями?')
                blocks.kid_adult(user_data)
            else:
                blocks.kid_pool(user_data)

        if user_data['position'] == 'kid-type':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid-pool')
                worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_pool_keyboard, botmessage='Выбери бассейн:\n\n👉Бассейн Swim Shot: с 3 лет персонально, с 6 лет – в группу (Зеленоград, к1801)\n\n👉СК «Орбита» для детей 2-6 лет (Зеленоград, Озёрная аллея, 6)')
                blocks.kid_pool(user_data)
            else:
                blocks.kid_type(user_data)

        if user_data['position'] == 'kid-age':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid-type')
                worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
                blocks.kid_type(user_data)
            else:
                blocks.kid_age(user_data)
            
        if user_data['position'] == 'trainer':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid/adult')
                worker.send_msg(user_id, keyboard=keyboards.adult_keyboard, botmessage = 'Для кого интересуешься занятиями?')
                blocks.kid_adult(user_data)
            else:
                blocks.kid_group_trainer(user_data)

        if user_data['position'] == 'price':
            if msg_text == 'Назад':
                if user_data['kid_type'] == 'Групповые':
                    db.set_position(user_data['user_id'], 'trainer')
                    blocks.kid_age(user_data)
                elif user_data['kid_type'] == 'Персональные':
                    db.set_position(user_data['user_id'], 'kid-type')
                    worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
                    blocks.kid_type(user_data)
                elif user_data['kid_type'] == 'Свободное плавание':
                    db.set_position(user_data['user_id'], 'kid-type')
                    worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
                    blocks.kid_type(user_data)
            else:
                blocks.kid_price(user_data)

        if user_data['position'] == 'phone':
            if msg_text == 'Назад':
                if user_data['kid_type'] == 'Групповые':
                    db.set_position(user_data['user_id'], 'trainer')
                    blocks.kid_age(user_data)
                elif user_data['kid_type'] == 'Персональные':
                    db.set_position(user_data['user_id'], 'kid-type')
                    worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
                    blocks.kid_type(user_data)
                elif user_data['kid_type'] == 'Свободное плавание':
                    db.set_position(user_data['user_id'], 'kid-type')
                    worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
                    blocks.kid_type(user_data)
            else: 
                blocks.kid_phone(user_data)


    if adult == 'adult':
        if user_data['position'] == 'adult-pool':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid/adult')
                worker.send_msg(user_id, keyboard=keyboards.adult_keyboard, botmessage = user_name + ', теперь задам пару вопросов, чтобы предложить именно то, что для тебя будет полезно. Для кого интересуешься занятиями?')
                blocks.kid_adult(user_data)
            else:
                blocks.adult_pool(user_data)

        if user_data['position'] == 'adult-type':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'adult-pool')
                worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_pool_keyboard, botmessage='Выбери бассейн:\n\n\n👉Бассейн Swim Shot (Зеленоград, к1801)')
                blocks.adult_pool
            else:
                blocks.adult_types(user_data)

        if user_data['position'] == 'schedule':
            if msg_text == 'Назад':
                worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
                db.set_position(user_data['user_id'], 'adult-type')
                blocks.adult_types(user_data)
            else:
                blocks.adult_sched(user_data)

        if user_data['position'] == 'adult-daytime':
            if msg_text == 'Назад':
                worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
                db.set_position(user_data['user_id'], 'adult-type')
                blocks.adult_types(user_data)
            else:
                blocks.adult_day(user_data)

        if user_data['position'] == 'adult-trainer':
            if msg_text == 'Назад':
                db.set_position(user_data['user_id'], 'kid/adult')
                worker.send_msg(user_id, keyboard=keyboards.adult_keyboard, botmessage = 'Для кого интересуешься занятиями?')
                blocks.kid_adult(user_data)
            else:
                blocks.adult_trainer(user_data)

        if user_data['position'] == 'price':
            if msg_text == 'Назад':
                worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
                db.set_position(user_data['user_id'], 'adult-type')
                blocks.adult_types(user_data)
            else:
                blocks.adult_price(user_data)

        if user_data['position'] == 'phone':
            if msg_text == 'Назад':
                worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
                db.set_position(user_data['user_id'], 'adult-type')
                blocks.adult_types(user_data)
            else:
                blocks.adult_phone(user_data)

    if user_data['position'] == 'deal':
        if msg_text == 'Назад':
            worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
            db.set_position(user_data['user_id'], 'adult-type')
            blocks.adult_types(user_data)
    
    if user_data['position'] == 'fin':
            if msg_text == 'Новая заявка':
                db.delete_user(user_id)
                db.add_user(user_id)
                worker.send_msg(user_id, keyboard=keyboards.start_keyboard, botmessage=texts.start)
