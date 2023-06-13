import worker
import db
import keyboards
# photo-165657041_457239456
photos = {
    'Илья': 'photo-165657041_457239459',
    'Александра': 'photo-165657041_457239462',
    'Дарья': 'photo-165657041_457239458',
    'Сергей': 'photo-165657041_457239464',
    'Любовь': 'photo-165657041_457239460',
    'Александр А.': 'photo-165657041_457239456',
    'Александр Д.': 'photo-165657041_457239463'
}


#Д Е Т И
def kid_adult(user_data):
    if user_data['msg_text'] == 'Для ребёнка':
        db.set_adult(user_data['user_id'], 'kid')
        db.set_position(user_data['user_id'], 'kid-pool')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_pool_keyboard, botmessage='Выбери бассейн:\n\n\n👉Бассейн Swim Shot с 3 лет персонально, с 6 – в группу (Зеленоград, к1801)\n\n👉Бассейн в премиум клубе Анкор с 4 лет (Зеленоград, к305)\n\n👉СК «Орбита» для детей 2-6 лет (Зеленоград, Озёрная аллея, 6)')
    elif user_data['msg_text'] == 'Для взрослого':
        db.set_adult(user_data['user_id'], 'adult')
        db.set_position(user_data['user_id'], 'adult-pool')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_pool_keyboard, botmessage='Выбери бассейн:\n\n\n👉Бассейн Swim Shot с 3 лет персонально, с 6 – в группу (Зеленоград, к1801)\n\n👉Бассейн в премиум клубе Анкор с 4 лет (Зеленоград, к305)')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_keyboard, botmessage = user_data['user_name'] + ', теперь задам пару вопросов, чтобы предложить именно то, что для тебя будет полезно. Для кого интересуешься занятиями?')

def kid_pool(user_data):
    if user_data['msg_text'] == 'Бассейн Swim Shot' or user_data['msg_text'] == 'Бассейн Анкор' or user_data['msg_text'] == 'СК «Орбита»':
        db.set_pool(user_data['user_id'], user_data['msg_text'])
        db.set_position(user_data['user_id'], 'kid-type')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО восьми человек на одного тренера, в среднем 5-7)\n\n👉Персональные тренировки (один на один с тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет самостоятельно)')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_type(user_data):
    if user_data['msg_text'] == 'Групповые':
        db.set_type(user_data['user_id'], 'Групповые')
        age_keyboard = []
    
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            age_keyboard = keyboards.kid_age_k18_keyboard
        elif user_data['user_pool'] == 'Бассейн Анкор':
            age_keyboard = keyboards.kid_age_ankor_keyboard
        elif user_data['user_pool'] == 'СК «Орбита»':
            age_keyboard = keyboards.kid_age_orbita_keyboard
        else:
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

        db.set_position(user_data['user_id'], 'kid-age')
        worker.send_msg(user_data['user_id'], keyboard=age_keyboard, botmessage = user_data['user_name'] + ', выбери возрастную категорию ребенка')
    elif user_data['msg_text'] == 'Персональные':
        db.set_position(user_data['user_id'], 'trainer')
        worker.send_msg(user_data['user_id'], 'Персональные тренировки для тех, кто хочет быстрый, мощный и, главное, кайфовый результат 🔥\nЗанятия проходят под руководством тренера, который покажет (да, прямо в воде) технику и расскажет, как правильно пускать пузырики в воду 😁 Самое главное, что возраст и уровень плавания ученика не важны – хочешь ты подготовиться к соревнованиям или только знакомишься с водной стихией. Длительность тренировок – 45 минут.Персонально с тренером можно заниматься в любое время в рамках работы бассейна, записавшись заранее. \n\nРежим работы бассейна Swim Shot к1801: будни с 6:45 до 23:00, выходные и праздники с 8:15 до 22:15; \nбассейна Анкор к305: ежедневно с 9:00 до 22:00')       
        worker.send_msg(user_data['user_id'], keyboard=keyboards.trainer_keyboard_kid_personal, botmessage='Предлагаю познакомиться с тренерским составом. Скорее всего, это будет «любовь» с первого взгляда 🥰 Осталась определить, с кем')
        db.set_type(user_data['user_id'], 'Персональные')
    elif user_data['msg_text'] == 'Свободное плавание':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], 'Свободное плавание для тех, кто любит свободу и полный чилл в своё удовольствие 😇\nСвободное плавание могут посещать дети с 5 лет:\nдо 14 лет в сопровождении представителя и по письменному заявлению об его ответственности за ребенка;\nс 14 лет до 17  – самостоятельно, но с письменным заявлением представителя.\nРежим работы бассейна Swim Shot к1801: будни с 6:45 до 23:00, выходные и праздники с 8:15 до 22:15. \nС понедельника по субботу с 16:00 до 19:00 свободного плавания нет, поскольку тренируются спортгруппы. \n\nЗаниматься можно разово или по абонементу')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
        db.set_type(user_data['user_id'], 'Свободное плавание')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_age(user_data):
    worker.send_msg(user_data['user_id'], 'Смотри, какие группы я нашел 🔎 Можно комбинировать любые дни и любых тренеров из списка ниже. Можно заниматься разово или по абонементу. Можно заниматься 1 р/нед, 2 р/нед, 3 р/нед, да и вообще сколько угодно раз, все зависит от твоей цели')
    db.set_position(user_data['user_id'], 'trainer')

    if user_data['user_pool'] == 'Бассейн Swim Shot':
        if user_data['msg_text'] == '6-8' or user_data['user_age'] == '6-8':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801)\n\nпонедельник\n13:45 тренер Дарья\n14:30, 15:15, 16:45 тренер Любовь\n19:00, 19:45 тренер Илья\n\nвторник\n13:45, 14:30, 15:15, 16:00, 16:45, 19:45 тренер Александра\n14:30, 19:00 тренер Любовь\n16:00, 17:30 тренер Сергей\n\nсреда\n13:45 тренер Дарья\n14:30, 15:15, 16:45 тренер Любовь\n19:00 тренер Сергей\n\nчетверг\n13:45, 14:30, 15:15, 16:00, 16:45, 19:45 тренер Александра\n14:30, 19:00 тренер Любовь\n16:00, 17:30 тренер Сергей\n\nпятница\n13:45 тренер Дарья\n14:30, 15:15, 16:45 тренер Любовь\n19:00, 19:45 тренер Илья\n\nсуббота\n10:45, 11:30, 12:15, 14:30, 16:45 тренер Александра\n13:00, 13:45, 16:00 тренер Илья\n16:00, 17:30, 19:00 тренер Сергей\n\nвоскресенье\n10:45, 11:30, 12:15, 14:30, 16:45 тренер Александра\n13:00, 13:45, 16:00 тренер Илья')
        elif user_data['msg_text'] == '9-12' or user_data['user_age'] == '9-12':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801)\n\nпонедельник\n14:30, 15:15, 16:00, 17:30 тренер Ильяn\n16:00, 19:00 тренер Любовь\n\nвторник\n15:15, 17:30 тренер Любовь\n16:45, 18:15 тренер Сергей\n19:00 тренер Александра\n\nсреда\n14:30, 15:15, 17:30 тренер Сергей\n16:00, 19:00 тренер Любовь\n\nчетверг\n15:15, 17:30 тренер Любовь\n16:45, 18:15 тренер Сергей\n19:00 тренер Александра\n\nпятница\n14:30, 15:15, 16:00, 17:30 тренер Илья\n16:00, 19:00 тренер Любовь\n\nсуббота\n11:30, 14:30, 15:15, 18:15 тренер Сергей\n12:15, 16:45 тренер Илья\n13:00, 13:45, 19:00 тренер Александра\n18:15 тренер Сергей\n\nвоскресенье\n11:30 тренер Сергей\n12:15, 14:30, 15:15, 17:30, 18:15 тренер Илья\n13:00, 13:45, 16:00 тренер Александра')
        elif user_data['msg_text'] == '13-17' or user_data['user_age'] == '13-17':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801)\n\nпонедельник\n18:15 тренер Илья\n19:45 тренер Любовь\n\nвторник\n18:15 тренер Любовь\n\nсреда\n18:15 тренер Сергей\n19:45 тренер Любовь\n\nчетверг\n18:15 тренер Любовь\n\nпятница\n18:15 тренер Илья\n19:45 тренер Любовь\n\nсуббота\n17:30, 18:15 тренер Александра\n\nвоскресенье\n17:30, 18:15, 19:00 тренер Александра')
        else:
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    if user_data['user_pool'] == 'Бассейн Анкор':
        if user_data['msg_text'] == '4-5' or user_data['user_age'] == '4-5':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], '\nБассейн в премиум клубе Анкор (Зеленоград, к305)\n\nС понедельника по пятницу с 16:00 до 19:00. \nВыходные с 12:00 до 15:00. \nГруппы по возрасту компонуем, исходя из заявок. Старт локации 14 февраля 2023.\nТренер Сергей\nТренеры Дарья и Владимир')
        elif user_data['msg_text'] == '6-8' or user_data['user_age'] == '6-8':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], '\nБассейн в премиум клубе Анкор (Зеленоград, к305)\n\nС понедельника по пятницу с 16:00 до 19:00. \nВыходные с 12:00 до 15:00. \nГруппы по возврату компонуем, исходя из заявок. Старт локации 14 февраля 2023.\nТренер Сергей')
        elif user_data['msg_text'] == '9-12' or user_data['user_age'] == '9-12':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], '\nБассейн в премиум клубе Анкор (Зеленоград, к305)\n\nС понедельника по пятницу с 16:00 до 19:00. \nВыходные с 12:00 до 15:00. \nГруппы по возврату компонуем, исходя из заявок. Старт локации 14 февраля 2023.\nТренер Сергей')
        elif user_data['msg_text'] == '13-17' or user_data['user_age'] == '13-17':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], '\nБассейн в премиум клубе Анкор (Зеленоград, к305)\n\nС понедельника по пятницу с 16:00 до 19:00. \nВыходные с 12:00 до 15:00. \nГруппы по возврату компонуем, исходя из заявок. Старт локации 14 февраля 2023.\nТренер Сергей')
        else:
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    if user_data['user_pool'] == 'СК «Орбита»':
        if user_data['msg_text'] == '2-3' or user_data['msg_text'] == '4-6' or user_data['user_age'] == '2-3' or user_data['user_age'] == '4-6':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'СК «Орбита» (Зеленоград, Озёрная аллея, 6)\n\nСуббота 11:15, 12:00\n\nВоскресенье 12:45, 13:30\n\nТренеры Дарья и Владимир')
    worker.send_msg(user_data['user_id'], keyboard=keyboards.trainer_keyboard_kid_group, botmessage='Какие дни и время для тебя удобны, '+user_data['user_name']+'? Отправь мне в сообщении имя тренера, группы которого тебе подходят. Я познакомлю тебя с ним 🤝🏻')


def kid_group_trainer(user_data):
    ph = None
    if user_data['msg_text'] == 'Илья' or user_data['msg_text'] == 'Александра' or user_data['msg_text'] == 'Дарья' or user_data['msg_text'] == 'Сергей' or user_data['msg_text'] == 'Любовь' or user_data['msg_text'] == 'Владимир' or user_data['msg_text'] == 'Александр Д.' or user_data['msg_text'] == 'Александр А.':
        ph = photos[user_data['msg_text']]
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=keyboards.trainer_keyboard_kid_group)
        db.set_trainer(user_data['user_id'], user_data['msg_text'])
    elif user_data['msg_text'] == 'Выбрать тренера':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.confirm_keyb, botmessage='Хочешь выбрать тренера '+db.get_trainer(user_data['user_id'])+'?')
    elif user_data['msg_text'] == 'Подтвердить':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
    # elif user_data['msg_text'] == 'Отправь цены 💳':
    #     pass
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_price(user_data):
    if user_data['msg_text'] != 'Отправь цены 💳':
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    db.set_position(user_data['user_id'], 'phone')
    if user_data['kid_type'] == 'Групповые':
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц) в бассейне Swim Shot:\n\nРаз в неделю – от 4 500 до 4 900\nДва раза в неделю – от 7 500 до 8 500\nТри раза в неделю – от 9 900 до 10 900\n\n* стоимость варьируется в зависимости от выбранного времени')
            worker.send_msg(user_data['user_id'], user_data['user_name']+', пора тренироваться. Приглашаю тебя на пробную тренировку в школу плавания Swim Shot. Она стоит всего 500₽.')
        if user_data['user_pool'] == 'Бассейн Анкор':
            worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц) в СК «Орбита»:\n\nРаз в неделю – 5 500\nДва раза в неделю – 9 900')
            worker.send_msg(user_data['user_id'], user_data['user_name']+', пора тренироваться. Приглашаю тебя на пробную тренировку в школу плавания Swim Shot. Она стоит всего 500₽.')
        if user_data['user_pool'] == 'СК «Орбита»':
            worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц) в бассейне в премиум клубе Анкор:\n\nРаз в неделю – 14 900\nДва раза в неделю – 24 900\nТри раза в неделю – 34 900')
            worker.send_msg(user_data['user_id'], user_data['user_name']+', пора тренироваться. Приглашаю тебя на пробную тренировку в школу плавания Swim Shot. Она стоит всего 900₽.')
    
    if user_data['kid_type'] == 'Персональные':
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            worker.send_msg(user_data['user_id'], 'Персональные тренировки (покупаются блоком) в бассейне Swim Shot:\n\nОдна тренировка – 2 700\nТри тренировки – 7 800\nПять тренировок – 12 500\nДесять тренировок – 23 900')
            worker.send_msg(user_data['user_id'], user_data['user_name'] + ', давай попробуем. Приглашаю тебя на первую тренировку в школу плавания Swim Shot.')
    
    if user_data['kid_type'] == 'Свободное плавание':
        worker.send_msg(user_data['user_id'], 'Свободное плавание безлимит (нет ограничений по частоте и длительности посещений):\n\nМесяц – 4 900\nТри месяца – 12 900\nПолгода – 20 900\nГод – 29 900\nРазовое посещение без ограничений по времени – 1 000')
        worker.send_msg(user_data['user_id'], user_data['user_name'] + ', давай попробуем. Приглашаю тебя на первую тренировку в школу плавания Swim Shot.')
    worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage='Готов записаться?')


def kid_phone(user_data):
    if user_data['msg_text'] == 'Хочу записаться 🤩' or user_data['msg_text'] == 'Ввести заново':
        worker.send_msg(user_data['user_id'], 'Пришли свой номер телефона, чтобы наш менеджер с тобой связался')
    elif user_data['msg_text'] == 'Подтвердить':
        worker.send_form(user_data['user_id'])
        db.set_position(user_data['user_id'], 'fin')
        worker.send_msg(user_data['user_id'], 'Отлично 🎉 Заявка отправлена. Менеджер отдела продаж скоро свяжется с тобой. Ожидай, пожалуйста. А пока подпишись на наши страницы в соцсетях, чтобы не пропустить акции, изменения в расписании и прочую важную инфу о Swim Shot')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.end_keyb, botmessage='Стать чуть ближе к Swim Shot:\n\n🔗 ВКонтакте: https://vk.com/swim_shot\n🔗 Телеграм: https://t.me/swimshot\n🔗 Розовая соц сеть (запрещенная в РФ): https://www.instagram.com/swim_shot\n🔗 Яндекс.Дзен: https://zen.yandex.ru/id/61f02212765d8f1266d725a4/\n🔗 Сайт: https://swimshot.ru/')
    else:
        db.set_phone(user_data['user_id'], user_data['msg_text'])
        worker.send_msg(user_data['user_id'], keyboard = keyboards.phone_keyb, botmessage='Сохранить этот номер?\n\n' + str(user_data['msg_text']))



#В З Р О С Л Ы Е
def adult_pool(user_data):
    db.set_pool(user_data['user_id'], user_data['msg_text'])
    worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление')
    db.set_position(user_data['user_id'], 'adult-type')


def adult_types(user_data):
    db.set_type(user_data['user_id'], user_data['msg_text'])
    if user_data['msg_text'] == 'Групповые тренировки':
        worker.send_msg(user_data['user_id'], 'Если хочешь кайфануть от плавания вместе с опытными тренерами, которые всё покажут, всему научат – тебе сюда 🔥 Длительность тренировок – 45 минут.')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_daytime_keyboard ,botmessage=user_data['user_name']+', когда тебе удобнее тренироваться?')
        db.set_position(user_data['user_id'], 'adult-daytime')
    elif user_data['msg_text'] == 'Здоровая спина':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.schedule_keyb, botmessage='Тренировки по направлению «Здоровая спина» подходят для тех, у кого есть проблемы с позвоночником, осанкой или другие моменты в спине, которые хочется улучшить. Длительность тренировок – 45 минут. Чтобы узнать расписание, жми на кнопку «Расписание 🗓️»')
        db.set_position(user_data['user_id'], 'schedule')
    elif user_data['msg_text'] == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.schedule_keyb, botmessage='Любишь плавать и танцевать, но не знаешь куда пойти? Правильно! На занятие по аквааэробике 💃🏻 Мощный фитнес в воде без элементов обучения плаванию. Длительность тренировок - 45 минут. Чтобы узнать расписание, жми на кнопку «Расписание 🗓️»')
        db.set_position(user_data['user_id'], 'schedule')
    elif user_data['msg_text'] == 'Свободное плавание':
        worker.send_msg(user_data['user_id'], 'Свободное плавание для тех, кто любит свободу и полный чилл в своё удовольствие 😇 \n\nРежим работы бассейна Swim Shot к1801: \nбудни с 6:45 до 23:00, \nвыходные и праздники с 8:15 до 22:15. \nС понедельника по субботу с 16:00 до 19:00 свободного плавания нет, поскольку тренируются детские спортгруппы. \n\nЗаниматься можно разово или по абонементу')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard, botmessage='Для уточнения стоимости занятий нажми 👇🏻')
        db.set_position(user_data['user_id'], 'price')
    elif user_data['msg_text'] == 'Персональные тренировки':
        worker.send_msg(user_data['user_id'], botmessage='Персональные тренировки для тех, кто хочет быстрый, мощный и, главное, кайфовый результат 🔥\n\nЗанятия проходят под руководством тренера, который покажет (да, прямо в воде) технику и расскажет, как правильно пускать пузырики в воду 😁 Самое главное, что возраст и уровень плавания ученика не важны – хочешь ты подготовиться к соревнованиям или только знакомишься с водной стихией. Длительность тренировок – 45 минут.\nПерсонально с тренером можно заниматься в любое время в рамках работы бассейна. \n\nРежим работы бассейна Swim Shot к1801: \n\nбудни с 6:45 до 23:00, \nвыходные и праздники с 8:15 до 22:15')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.trainer_keyboard_adult_personal, botmessage='Предлагаю познакомиться с тренерским составом. Возможно это будет «любовь» с первого взгляда 🥰 Осталась определить, с кем')
        db.set_position(user_data['user_id'], 'adult-trainer')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def adult_sched(user_data):
    adult_type = user_data['kid_type']
    if adult_type == 'Здоровая спина':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801). \nПонедельник, среда, пятница 20:30 тренер Любовь')
    elif adult_type == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801).\nПонедельник, четверг 20:30 тренер Любовь')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
    worker.send_msg(user_data['user_id'], keyboard=keyboards.introd_keyb, botmessage='Хочешь я познакомлю тебя с тренером? Тогда жми на кнопку «Познакомь с тренером 👋🏻»')
    db.set_position(user_data['user_id'], 'adult-trainer')


def adult_day(user_data):
    worker.send_msg(user_data['user_id'], 'Смотри, какие группы я нашел 🔎 Можно комбинировать любые дни и любых тренеров из списка ниже')

    if user_data['msg_text'] == 'Утром':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801)\n\nПонедельник\n7:45, 8:30 тренер Дарья\n\nВторник\n7:45, 8:30 тренер Сергей\n\nСреда\n7:45, 8:30 тренер Дарья\n\nЧетверг\n7:45, 8:30 тренер Сергей\n\nПятница\n7:45, 8:30 тренер Дарья\n\nСуббота\n9:15 тренер Илья\n\nВоскресенье\n8:30, 9:15 тренер Илья')
    elif user_data['msg_text'] == 'Вечером':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801)\n\nПонедельник\n20:30, 21:15 тренер Дарья\n\nВторник\n20:30, 21:15 тренер Сергей\n\nСреда\n20:30, 21:15 тренер Дарья\n\nЧетверг\n20:30, 21:15 тренер Сергей\n\nПятница\n20:30, 21:15 тренер Дарья\n\nСуббота\n19:45, 20:30 тренер Сергей\n\nВоскресенье\n19:45, 20:30 \nтренер Александра')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_group_trainer_keyb ,botmessage='Какие дни и время для тебя удобны, '+user_data['user_name']+'? Отправь мне в сообщении имя тренера, группы которого тебе подходят. Я познакомлю тебя с ним 🤝🏻')
    db.set_position(user_data['user_id'], 'adult-trainer')


def adult_trainer(user_data):
    ph = None
    if user_data['msg_text'] == 'Илья' or user_data['msg_text'] == 'Александра' or user_data['msg_text'] == 'Дарья' or user_data['msg_text'] == 'Сергей' or user_data['msg_text'] == 'Любовь' or user_data['msg_text'] == 'Владимир' or user_data['msg_text'] == 'Александр Д.' or user_data['msg_text'] == 'Александр А.':
        ph = photos[user_data['msg_text']]
        if user_data['kid_type'] == 'Групповые тренировки':
            keyb = keyboards.adult_group_trainer_keyb
        elif user_data['kid_type'] == 'Персональные тренировки':
            keyb = keyboards.trainer_keyboard_adult_personal
        else:
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=keyb)
        db.set_trainer(user_data['user_id'], user_data['msg_text'])
    elif user_data['msg_text'] == 'Выбрать тренера':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.confirm_keyb, botmessage='Хочешь выбрать тренера '+str(db.get_trainer(user_data['user_id']))+'?')
    elif user_data['msg_text'] == 'Подтвердить':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
    elif user_data['msg_text'] == 'Познакомь с тренером 👋🏻':
        ph = photos['Любовь']
        db.set_trainer(user_data['user_id'], 'Любовь')
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=keyboards.confirm_keyb)
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def adult_price(user_data):
    adult_type = user_data['kid_type']
    if adult_type == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц):\nРаз в неделю – 3 500\nДва раза в неделю – 5 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', пора тренироваться. Приглашаю тебя на пробную тренировку в школу плавания Swim Shot. Она стоит всего 500₽.')
    elif adult_type == 'Групповые тренировки' or 'Здоровая спина':
        worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц):\n\nРаз в неделю – 4 500\nДва раза в неделю – 7 900\nТри раза в неделю – 9 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', пора тренироваться. Приглашаю тебя на пробную тренировку в школу плавания Swim Shot. Она стоит всего 500₽.')
    elif adult_type == 'Свободное плавание':
        worker.send_msg(user_data['user_id'], 'Свободное плавание безлимит (нет ограничений по частоте и времени посещений):\n\nМесяц – 4 900\nТри месяца – 12 900\nПолгода – 20 900\nГод – 29 900\n\nРазовое посещение без ограничений по времени – 1 000')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', давай попробуем. Приглашаю тебя на первое занятие в школу плавания Swim Shot. Готов записаться?')
    elif adult_type == 'Персональные тренировки':
        worker.send_msg(user_data['user_id'], 'Персональные тренировки (покупаются блоком):\n\nОдна тренировка – 2 700\nТри тренировки – 7 800\nПять тренировок – 12 500\nДесять тренировок – 23 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', давай попробуем. Приглашаю тебя на первую тренировку в школу плавания Swim Shot. Готов записаться?')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
    db.set_position(user_data['user_id'], 'phone')


def adult_phone(user_data):
    if user_data['msg_text'] == 'Хочу записаться 🤩' or user_data['msg_text'] == 'Ввести заново':
        worker.send_msg(user_data['user_id'], 'Пришли свой номер телефона, чтобы наш менеджер с тобой связался')
    elif user_data['msg_text'] == 'Подтвердить':
        worker.send_form(user_data['user_id'])
        db.set_position(user_data['user_id'], 'fin')
        worker.send_msg(user_data['user_id'], 'Отлично 🎉 Заявка отправлена. Менеджер отдела продаж скоро свяжется с тобой. Ожидай, пожалуйста. А пока подпишись на наши страницы в соцсетях, чтобы не пропустить акции, изменения в расписании и прочую важную инфу о Swim Shot')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.end_keyb ,botmessage='Стать чуть ближе к Swim Shot:\n\n🔗 ВКонтакте: https://vk.com/swim_shot\n🔗 Телеграм: https://t.me/swimshot\n🔗 Розовая соц сеть (запрещенная в РФ): https://www.instagram.com/swim_shot\n🔗 Яндекс.Дзен: https://zen.yandex.ru/id/61f02212765d8f1266d725a4/\n🔗 Сайт: https://swimshot.ru/')
    else:
        db.set_phone(user_data['user_id'], user_data['msg_text'])
        worker.send_msg(user_data['user_id'], keyboard = keyboards.phone_keyb, botmessage='Сохранить этот номер?\n\n' + str(db.get_phone(user_data['user_id'])))
