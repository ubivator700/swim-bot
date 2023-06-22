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
    'Александр Д.': 'photo-165657041_457239463',
    'Владимир': 'photo-201905325_457239152',
    'Анна': 'photo-201905325_457239153'
}


#Д Е Т И
def kid_adult(user_data):
    if user_data['msg_text'] == 'Для ребёнка 👧🏻👦🏻':
        db.set_adult(user_data['user_id'], 'kid')
        db.set_position(user_data['user_id'], 'kid-pool')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_pool_keyboard, botmessage='Выбери бассейн:\n\n\n👉Бассейн Swim Shot: с 3 лет персонально, с 6 лет – в группу (Зеленоград, к1801)\n\n👉СК «Орбита» для детей 2-6 лет (Зеленоград, Озёрная аллея, 6)')
    elif user_data['msg_text'] == 'Для взрослого 👩🏻👨🏻':
        db.set_adult(user_data['user_id'], 'adult')
        db.set_position(user_data['user_id'], 'adult-pool')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_pool_keyboard, botmessage='Выбери бассейн:\n\n\n👉Бассейн Swim Shot (Зеленоград, к1801)')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_keyboard, botmessage = user_data['user_name'] + ', теперь задам пару вопросов, чтобы предложить именно то, что для тебя будет полезно. Для кого интересуешься занятиями?')

def kid_pool(user_data):
    if user_data['msg_text'] == 'Бассейн Swim Shot':
        db.set_pool(user_data['user_id'], user_data['msg_text'])
        db.set_position(user_data['user_id'], 'kid-type')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)\n\n👉Персональные тренировки (один на один с Тренером)\n\n👉Свободное плавание (до 14 лет в сопровождении взрослого, с 14 лет – самостоятельно)')
    elif user_data['msg_text'] == 'СК «Орбита»':
        db.set_pool(user_data['user_id'], user_data['msg_text'])
        db.set_position(user_data['user_id'], 'kid-type')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.kid_type_keyboard_orbita, botmessage='Выбери направление:\n\n\n👉Групповые тренировки по плаванию (в группе ДО 8 человек на одного Тренера, в – среднем 5-7 человек)')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_type(user_data):
    if user_data['msg_text'] == 'Групповые':
        db.set_type(user_data['user_id'], 'Групповые')
        age_keyboard = []
    
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            age_keyboard = keyboards.kid_age_k18_keyboard
        elif user_data['user_pool'] == 'СК «Орбита»':
            age_keyboard = keyboards.kid_age_orbita_keyboard
        else:
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

        db.set_position(user_data['user_id'], 'kid-age')
        worker.send_msg(user_data['user_id'], keyboard=age_keyboard, botmessage = user_data['user_name'] + ', выбери возрастную категорию ребенка')
    elif user_data['msg_text'] == 'Персональные':
        db.set_position(user_data['user_id'], 'trainer')
        worker.send_msg(user_data['user_id'], 'Персональные тренировки для тех, кто хочет быстрый, мощный и, главное, кайфовый результат🔥\n\nЗанятия проходят под руководством Тренера, который покажет (да, прямо в воде) технику и расскажет, как правильно пускать пузырики в воду 😁 \n\nСамое главное, что возраст и уровень плавания ученика не важны – хочешь ты подготовиться к соревнованиям или только знакомишься с водной стихией. Длительность тренировок – 45 минут. Персонально с Тренером можно заниматься в любое время в рамках работы бассейна, записавшись заранее. \n\nРежим работы бассейна  «Swim Shot» к1801: будни с 6:45 до 23:00, выходные и праздники с 8:15 до 22:15')       
        worker.send_msg(user_data['user_id'], keyboard=keyboards.trainer_keyboard_kid_personal, botmessage='Предлагаю познакомиться с Тренерским составом. Скорее всего, это будет «любовь» с первого взгляда 🥰 Осталось определить, с кем')
        db.set_type(user_data['user_id'], 'Персональные')
    elif user_data['msg_text'] == 'Свободное плавание':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], 'Свободное плавание для тех, кто любит свободу и полный чилл в своё удовольствие 😇\n\nСвободное плавание могут посещать дети с 5 лет:\n🔹до 14 лет в сопровождении представителя и по письменному заявлению об его ответственности за ребенка;\n🔹с 14 лет до 17  – самостоятельно, но с письменным заявлением представителя.\n\nРежим работы бассейна Swim Shot к1801:\n 🔹будни с 6:45 до 23:00\n🔹выходные и праздники с 8:15 до 22:15. \n\nС понедельника по субботу с 16:00 до 19:00 свободного плавания нет, поскольку тренируются спортгруппы. Заниматься можно разово или по абонементу')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
        db.set_type(user_data['user_id'], 'Свободное плавание')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_age(user_data):
    kb = keyboards.trainer_keyboard_adult_personal
    worker.send_msg(user_data['user_id'], 'Смотри, какие группы я нашел \n\n🔹Можно комбинировать любые дни и любых Тренеров из списка ниже\n🔹Можно заниматься разово или по абонементу\n🔹Можно заниматься 1 р/нед, 2 р/нед, 3 р/нед. Да и вообще сколько угодно раз, всё зависит от твоей цели')
    db.set_position(user_data['user_id'], 'trainer')

    if user_data['user_pool'] == 'Бассейн Swim Shot':
        if user_data['msg_text'] == '6-8' or user_data['user_age'] == '6-8':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн «Swim Shot» (Зеленоград, к1801)\n\nПонедельник \n🔹13:00 — ТренераДарья\n🔹14:30, 15:15, 16:45 — ТренераЛюбовь\n🔹16:00, 17:30, 18:15 — ТренераИлья\n\nВторник\n🔹13:45, 14:30, 15:15, 16:00, 16:45, 19:45 — ТренераАлександра\n🔹14:30, 19:00 — ТренераЛюбовь\n🔹12:15, 16:00, 18:15 — ТренераАнна\n\nСреда\n🔹13:45 — ТренераДарья\n🔹15:15, 16:45 — ТренераЛюбовь\n🔹19:00 — ТренераАнна\n\nЧетверг\n🔹13:45, 14:30, 15:15, 16:00, 16:45, 19:45 — ТренераАлександра\n🔹14:30, 19:00 — ТренераЛюбовь\n🔹12:15, 16:00, 18:15 — ТренераАнна\n\nПятница\n🔹13:00 — ТренераДарья\n🔹14:30, 15:15, 16:45 — ТренераЛюбовь\n🔹16:00, 17:30, 18:15 — ТренераИлья\n\nСуббота\n🔹10:45, 11:30, 12:15, 14:30, 16:45 — ТренераАлександра\n🔹12:15, 13:00, 13:45 — ТренераИлья\n🔹15:15, 17:30, 19:45 — ТренераАнна\n\nВоскресенье\n🔹10:45, 11:30, 12:15, 14:30, 15:15, 16:45 — ТренераАлександра\n🔹12:15, 13:00, 13:45 — ТренераИлья')
            kb = keyboards.trainer_keyboard_kid_group_shot_6x8
        elif user_data['msg_text'] == '9-12' or user_data['user_age'] == '9-12':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн «Swim Shot» (Зеленоград, к1801)\n\nПонедельник\n🔹13:00, 14:30, 15:15, 16:45 — ТренераИлья\n🔹16:00, 19:00 — ТренераЛюбовь\n\nВторник\n🔹15:15, 17:30 — ТренераЛюбовь\n🔹11:30, 13:45, 16:45 — ТренераАнна\n🔹19:00 — ТренераАлександра\n\nСреда\n🔹13:00, 13:45, 15:15 — ТренераАнна\n🔹16:00, 18:15, 19:00 — ТренераЛюбовь\n\nЧетверг\n🔹11:30, 13:45, 16:45 — ТренераАнна\n🔹15:15, 17:30 — ТренераЛюбовь\n🔹19:00 — ТренераАлександра\n\nПятница\n🔹13:00, 14:30, 15:15, 16:45 — ТренераИлья\n🔹16:00, 19:00 — ТренераЛюбовь\n\nСуббота\n🔹14:30, 16:45, 18:15 — ТренераАнна\n🔹10:15, 11:30 — ТренераИлья\n🔹13:00, 13:45 — ТренераАлександра\n\nВоскресенье\n🔹10:15, 11:30, 15:15, 16:00, 16:45 — ТренераИлья\n🔹13:00, 13:45 — ТренераАлександра')
            kb = keyboards.trainer_keyboard_kid_group_shot_9x12
        elif user_data['msg_text'] == '13-17' or user_data['user_age'] == '13-17':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'Бассейн «Swim Shot» (Зеленоград, к1801)\n\nПонедельник\n🔹13:45 — ТренераИлья\n🔹17:30 — ТренераЛюбовь\n\nВторник\n🔹13:00 — ТренераАнна\n🔹18:15 — ТренераЛюбовь\n\nСреда\n🔹12:15 — ТренераАнна\n🔹17:30 — ТренераЛюбовь\n\nЧетверг\n🔹13:00 — ТренераАнна\n🔹18:15 — ТренераЛюбовь\n\nПятница\n🔹13:45 — ТренераИлья\n🔹17:30 — ТренераЛюбовь\n\nСуббота\n🔹16:00 — ТренераАлександра\n\nВоскресенье\n🔹16:00 — ТренераАлександра ')
            kb = keyboards.trainer_keyboard_kid_group_shot_13x17
        elif user_data['user_pool'] != 'СК «Орбита»':
            worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    if user_data['user_pool'] == 'СК «Орбита»':
        if user_data['msg_text'] == '2-3' or user_data['msg_text'] == '4-6' or user_data['user_age'] == '2-3' or user_data['user_age'] == '4-6':
            db.set_kid_age(user_data['user_id'], user_data['msg_text'])
            worker.send_msg(user_data['user_id'], 'СК «Орбита» (Зеленоград, Озёрная аллея, 6)\n🔹Суббота: 11:15, 12:00\n🔹Воскресенье: 12:45, 13:30\nТренеры Дарья и Владимир')
            kb = keyboards.trainer_keyboard_kid_group_orbita_2x6
    worker.send_msg(user_data['user_id'], keyboard=kb, botmessage='Какие дни и время для тебя удобны, '+user_data['user_name']+'? \nОтправь мне в сообщении имя Тренера, группы которого тебе подходят. Я познакомлю тебя с ним 🤝🏻')


def kid_group_trainer(user_data):
    ph = None
    kb = keyboards.trainer_keyboard_adult_personal
    if user_data['user_pool'] == 'СК «Орбита»':
        kb = keyboards.trainer_keyboard_kid_group_orbita_2x6
    if user_data['user_pool'] == 'Бассейн Swim Shot' and user_data['user_age'] == '6-8':
        kb = keyboards.trainer_keyboard_kid_group_shot_6x8
    if user_data['user_pool'] == 'Бассейн Swim Shot' and user_data['user_age'] == '9-12':
        kb = keyboards.trainer_keyboard_kid_group_shot_9x12
    if user_data['user_pool'] == 'Бассейн Swim Shot' and user_data['user_age'] == '13-17':
        kb = keyboards.trainer_keyboard_kid_group_shot_13x17
    if user_data['msg_text'] == 'Илья' or user_data['msg_text'] == 'Александра' or user_data['msg_text'] == 'Дарья' or user_data['msg_text'] == 'Сергей' or user_data['msg_text'] == 'Любовь' or user_data['msg_text'] == 'Владимир' or user_data['msg_text'] == 'Александр Д.' or user_data['msg_text'] == 'Александр А.' or user_data['msg_text'] == 'Анна':
        ph = photos[user_data['msg_text']]
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=kb)
        db.set_trainer(user_data['user_id'], user_data['msg_text'])
    elif user_data['msg_text'] == 'Выбрать Тренера':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.confirm_keyb, botmessage='Хочешь выбрать Тренера '+db.get_trainer(user_data['user_id'])+'?')
    elif user_data['msg_text'] == 'Подтвердить':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def kid_price(user_data):
    if user_data['msg_text'] != 'Отправь цены 💳':
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    db.set_position(user_data['user_id'], 'phone')
    if user_data['kid_type'] == 'Групповые':
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц) в бассейне Swim Shot:\nРаз в неделю – от 4 500 до 4 900\nДва раза в неделю – от 7 500 до 8 500\nТри раза в неделю – от 9 900 до 10 900\n\n* стоимость варьируется в зависимости от выбранного времени')
            worker.send_msg(user_data['user_id'], user_data['user_name']+', пора тренироваться🔥. \nПриглашаю тебя на пробную тренировку в Школу плавания Swim Shot. Она стоит всего 500₽.')
        if user_data['user_pool'] == 'СК «Орбита»':
            worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц) в бассейне Swim Shot:\nРаз в неделю – от 4 500 до 4 900\nДва раза в неделю – от 7 500 до 8 500\nТри раза в неделю – от 9 900 до 10 900\n* стоимость варьируется в зависимости от выбранного времени')
            worker.send_msg(user_data['user_id'], user_data['user_name']+', пора тренироваться🔥. \nПриглашаю тебя на пробную тренировку в Школу плавания Swim Shot. Она стоит всего 500₽.')
    
    if user_data['kid_type'] == 'Персональные':
        if user_data['user_pool'] == 'Бассейн Swim Shot':
            worker.send_msg(user_data['user_id'], 'Персональные тренировки (покупаются блоком) в бассейне Swim Shot:\n\nОдна тренировка – 2 700\nТри тренировки – 7 800\nПять тренировок – 12 500\nДесять тренировок – 23 900')
            worker.send_msg(user_data['user_id'], user_data['user_name'] + ', давай попробуем. Приглашаю тебя на первую тренировку в Школу плавания Swim Shot.')
    
    if user_data['kid_type'] == 'Свободное плавание':
        worker.send_msg(user_data['user_id'], 'Свободное плавание безлимит (нет ограничений по частоте и длительности посещений):\n\nМесяц – 4 900\nТри месяца – 12 900\nПолгода – 20 900\nГод – 29 900\n\nРазовое посещение без ограничений по времени – 1 000')
        worker.send_msg(user_data['user_id'], user_data['user_name'] + ', давай попробуем.\nПриглашаю тебя на первую тренировку в Школу плавания Swim Shot.')
    worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage='Готов записаться?🐬')


def kid_phone(user_data):
    if user_data['msg_text'] == 'Хочу записаться 🤩' or user_data['msg_text'] == 'Ввести заново':
        worker.send_msg(user_data['user_id'], 'Пришли свой номер телефона, чтобы наш менеджер с тобой связался')
    elif user_data['msg_text'] == 'Подтвердить':
        worker.send_form(user_data['user_id'])
        db.set_position(user_data['user_id'], 'fin')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.end_keyb, botmessage='Отлично💙\n\nМенеджер скоро свяжется с тобой. А пока подпишись на наши страницы в соцсетях, чтобы не пропустить новинки и акции, а также стать ещё ближе к Swim Shot\n\n📎ВКонтакте: vk.com/swim_shot\n📎Телеграм: t.me/swimshot\n📎Розовая соцсеть (запрещённая в РФ): www.instagram.com/swim_shot\n📎Яндекс.Дзен: zen.yandex.ru/id/61f02212765d8f1266d725a4/\n📎Сайт: swimshot.ru/')
    else:
        db.set_phone(user_data['user_id'], user_data['msg_text'])
        worker.send_msg(user_data['user_id'], keyboard = keyboards.phone_keyb, botmessage='Сохранить этот номер?\n\n' + str(user_data['msg_text']))



#В З Р О С Л Ы Е
def adult_pool(user_data):
    db.set_pool(user_data['user_id'], user_data['msg_text'])
    worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_type_keyboard ,botmessage='Выбери направление:\n\n👉Групповые тренировки\n👉Здоровая спина\n👉Аквааэробика\n👉Свободное плавание\n👉Персональные тренировки')
    db.set_position(user_data['user_id'], 'adult-type')


def adult_types(user_data):
    db.set_type(user_data['user_id'], user_data['msg_text'])
    if user_data['msg_text'] == 'Групповые':
        worker.send_msg(user_data['user_id'], 'Если хочешь кайфануть от плавания вместе с опытными Тренерами, которые всё покажут, всему научат – тебе сюда🔥 \nДлительность тренировок – 45 минут.')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.adult_daytime_keyboard ,botmessage=user_data['user_name']+', когда тебе удобнее тренироваться?')
        db.set_position(user_data['user_id'], 'adult-daytime')
    elif user_data['msg_text'] == 'Спина':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.schedule_keyb, botmessage='Тренировки по направлению «Здоровая спина» подходят для тех, у кого есть проблемы с позвоночником, осанкой или другие моменты в спине, которые хочется улучшить.\nДлительность тренировок – 45 минут. \n\nЧтобы узнать расписание, жми на кнопку «Расписание 🗓️»')
        db.set_position(user_data['user_id'], 'schedule')
    elif user_data['msg_text'] == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.schedule_keyb, botmessage='Любишь плавать и танцевать, но не знаешь куда пойти? \n\nПравильно! На занятие по аквааэробике 💃🏻 \nМощный фитнес в воде без элементов обучения плаванию. \nДлительность тренировок – 45 минут. \n\nЧтобы узнать расписание, жми на кнопку «Расписание 🗓️»')
        db.set_position(user_data['user_id'], 'schedule')
    elif user_data['msg_text'] == 'Свободное':
        worker.send_msg(user_data['user_id'], 'Свободное плавание для тех, кто любит свободу и полный чилл в своё удовольствие 😇\n\nСвободное плавание могут посещать дети с 5 лет:\n🔹до 14 лет в сопровождении представителя и по письменному заявлению об его ответственности за ребенка;\n🔹с 14 лет до 17  – самостоятельно, но с письменным заявлением представителя.\n\nРежим работы бассейна Swim Shot к1801: \n🔹будни с 6:45 до 23:00\n🔹выходные и праздники с 8:15 до 22:15. \n\nС понедельника по субботу с 16:00 до 19:00 свободного плавания нет, поскольку тренируются спортгруппы. Заниматься можно разово или по абонементу')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard, botmessage='Для уточнения стоимости занятий нажми 👇🏻')
        db.set_position(user_data['user_id'], 'price')
    elif user_data['msg_text'] == 'Персональные':
        worker.send_msg(user_data['user_id'], botmessage='Персональные тренировки для тех, кто хочет быстрый, мощный и, главное, кайфовый результат 🔥\n\nЗанятия проходят под руководством Тренера, который покажет (да, прямо в воде) технику и расскажет, как правильно пускать пузырики в воду 😁\n\nСамое главное, что возраст и уровень плавания ученика не важны – хочешь ты подготовиться к соревнованиям или только знакомишься с водной стихией. Длительность тренировок – 45 минут.\n\nПерсонально с Тренером можно заниматься в любое время в рамках работы бассейна. \n\nРежим работы бассейна «Swim Shot»» к1801: будни с 6:45 до 23:00, выходные и праздники с 8:15 до 22:15')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.trainer_keyboard_adult_personal, botmessage='Предлагаю познакомиться с Тренерским составом. Возможно это будет «любовь» с первого взгляда 🥰 Осталось определить, с кем')
        db.set_position(user_data['user_id'], 'adult-trainer')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def adult_sched(user_data):
    adult_type = user_data['kid_type']
    if adult_type == 'Спина':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801). \n🔹Вторник и четверг 19:45  — ТренераЛюбовь')
    elif adult_type == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], 'Бассейн Swim Shot (Зеленоград, к1801).\n🔹Понедельник, пятница 19:45 – ТренераЛюбовь')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
    worker.send_msg(user_data['user_id'], keyboard=keyboards.introd_keyb, botmessage='Хочешь я познакомлю тебя с Тренером? Тогда жми на кнопку «Познакомь с Тренером 👋🏻»')
    db.set_position(user_data['user_id'], 'adult-trainer')


def adult_day(user_data):
    kb = keyboards.trainer_keyboard_adult_group
    worker.send_msg(user_data['user_id'], 'Смотри, какие группы я нашёл 🔎 \n\nМожно комбинировать любые дни и любых Тренеров из списка ниже👇🏻')
    if user_data['msg_text'] == 'Утром ☀️':
        worker.send_msg(user_data['user_id'], 'Бассейн «Swim Shot» (Зеленоград, к1801)\n\nПонедельник\n🔹7:45, 8:30 — ТренераДарья\n🔹12:15 — ТренераИлья\n\nВторник\n🔹7:45, 8:30 — ТренераАнна\n\nСреда\n🔹7:45, 8:30 — ТренераДарья\nЧетверг\n🔹7:45, 8:30 — ТренераАнна\n\nПятница\n🔹7:45, 8:30 — ТренераДарья\n🔹12:15 — ТренераИлья\n\nСуббота\n🔹8:30, 9:15 — ТренераИлья\n\nВоскресенье\n🔹8:30, 9:15 — ТренераИлья')
    elif user_data['msg_text'] == 'Вечером 🌚':
        worker.send_msg(user_data['user_id'], 'Бассейн «Swim Shot» (Зеленоград, к1801)\n\nПонедельник\n🔹20:30, 21:15 — ТренераДарья\n\nВторник\n🔹20:30, 21:15 — ТренераАнна\n\nСреда\n🔹20:30, 21:15 — ТренераДарья\n\nЧетверг\n🔹20:30, 21:15 — ТренераАнна\n\nПятница\n🔹20:30, 21:15 — ТренераДарья\n\nСуббота\n🔹20:30 — ТренераАнна\n\nВоскресенье\n🔹19:45, 20:30 — ТренераАлександра')
        kb = keyboards.trainer_keyboard_adult_group_evn
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')

    worker.send_msg(user_data['user_id'], keyboard=kb,botmessage='Какие дни и время для тебя удобны, '+user_data['user_name']+'?\n\nОтправь мне имя Тренера, группы которого тебе подходят. Я познакомлю тебя с ним 🤝🏻')
    db.set_position(user_data['user_id'], 'adult-trainer')


def adult_trainer(user_data):
    ph = None
    if user_data['msg_text'] == 'Илья' or user_data['msg_text'] == 'Александра' or user_data['msg_text'] == 'Дарья' or user_data['msg_text'] == 'Сергей' or user_data['msg_text'] == 'Любовь' or user_data['msg_text'] == 'Владимир' or user_data['msg_text'] == 'Александр Д.' or user_data['msg_text'] == 'Александр А.' or user_data['msg_text'] == 'Анна':
        ph = photos[user_data['msg_text']]
        if user_data['kid_type'] == 'Групповые тренировки':
            keyb = keyboards.trainer_keyboard_adult_personal
        elif user_data['kid_type'] == 'Персональные тренировки':
            keyb = keyboards.trainer_keyboard_adult_personal
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=keyboards.trainer_keyboard_adult_personal)
        db.set_trainer(user_data['user_id'], user_data['msg_text'])
    elif user_data['msg_text'] == 'Выбрать Тренера':
        worker.send_msg(user_data['user_id'], keyboard=keyboards.confirm_keyb, botmessage='Хочешь выбрать Тренера '+str(db.get_trainer(user_data['user_id']))+'?')
    elif user_data['msg_text'] == 'Подтвердить':
        db.set_position(user_data['user_id'], 'price')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.price_keyboard ,botmessage='Для уточнения стоимости занятий нажми 👇🏻')
    elif user_data['msg_text'] == 'Познакомь с Тренером 👋🏻':
        ph = photos['Любовь']
        db.set_trainer(user_data['user_id'], 'Любовь')
        worker.send_msg(user_data['user_id'], photo=ph, keyboard=keyboards.confirm_keyb)
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')


def adult_price(user_data):
    adult_type = user_data['kid_type']
    if adult_type == 'Аквааэробика':
        worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц):\nРазово – 1 400\nРаз в неделю – 4 500\nДва раза в неделю – 7 900\nТри раза в неделю – 10 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', пора тренироваться🔥 \nПриглашаю тебя на пробную тренировку в Школу плавания Swim Shot. Она стоит всего 500₽.')
    elif adult_type == 'Групповые':
        worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц):\n\nРаз в неделю – 4 500\nДва раза в неделю – 7 900\nТри раза в неделю – 9 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', пора тренироваться🔥 \nПриглашаю тебя на пробную тренировку в Школу плавания Swim Shot. Она стоит всего 500₽.')
    elif adult_type == 'Спина':
        worker.send_msg(user_data['user_id'], 'Групповые тренировки (стоимость за месяц):\n\nРазово – 1 200\nРаз в неделю – 3 500\nДва раза в неделю – 5 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', пора тренироваться🔥 \nПриглашаю тебя на пробную тренировку в Школу плавания Swim Shot. Она стоит всего 500₽.')
    elif adult_type == 'Свободное':
        worker.send_msg(user_data['user_id'], 'Свободное плавание безлимит (нет ограничений по частоте и времени посещений):\n\nМесяц – 4 900\nТри месяца – 12 900\nПолгода – 20 900\nГод – 29 900\n\nРазовое посещение без ограничений по времени – 1 000')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', давай попробуем. Приглашаю тебя на первое занятие в Школу плавания Swim Shot. Готов записаться?')
    elif adult_type == 'Персональные':
        worker.send_msg(user_data['user_id'], 'Персональные тренировки (покупаются блоком):\n\nОдна тренировка – 2 700\nТри тренировки – 7 800\nПять тренировок – 12 500\nДесять тренировок – 23 900')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.signup_keyboard, botmessage=user_data['user_name']+', давай попробуем. Приглашаю тебя на первую тренировку в Школу плавания Swim Shot. Готов записаться?')
    else:
        worker.send_msg(user_data['user_id'], 'Не понимаю, лучше пользуйтесь кнопками')
    db.set_position(user_data['user_id'], 'phone')


def adult_phone(user_data):
    if user_data['msg_text'] == 'Хочу записаться 🤩' or user_data['msg_text'] == 'Ввести заново':
        worker.send_msg(user_data['user_id'], 'Пришли свой номер телефона, чтобы наш менеджер с тобой связался')
    elif user_data['msg_text'] == 'Подтвердить':
        worker.send_form(user_data['user_id'])
        db.set_position(user_data['user_id'], 'fin')
        worker.send_msg(user_data['user_id'], keyboard=keyboards.end_keyb, botmessage='Отлично💙\n\nМенеджер скоро свяжется с тобой. А пока подпишись на наши страницы в соцсетях, чтобы не пропустить новинки и акции, а также стать ещё ближе к Swim Shot\n\n📎ВКонтакте: vk.com/swim_shot\n📎Телеграм: t.me/swimshot\n📎Розовая соцсеть (запрещённая в РФ): www.instagram.com/swim_shot\n📎Яндекс.Дзен: zen.yandex.ru/id/61f02212765d8f1266d725a4/\n📎Сайт: swimshot.ru/')
    else:
        db.set_phone(user_data['user_id'], user_data['msg_text'])
        worker.send_msg(user_data['user_id'], keyboard = keyboards.phone_keyb, botmessage='Сохранить этот номер?\n\n' + str(db.get_phone(user_data['user_id'])))
