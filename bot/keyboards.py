from vk_api.keyboard import VkKeyboard, VkKeyboardColor

        
kid_pool_buttons = ['Бассейн Swim Shot', 'СК «Орбита»']

# empty_kb = VkKeyboard(one_time=True)
# empty_kb.add_button('1')
# empty_kb.get_empty_keyboard()

start_keyboard = VkKeyboard(one_time=True)
start_keyboard.add_button('Начать', color=VkKeyboardColor.POSITIVE)

info_keyboard = VkKeyboard(one_time=False)
info_keyboard.add_button('Что такое Swim Shot? 🤔')
info_keyboard.add_button('Давай сразу к делу')

adult_keyboard = VkKeyboard(one_time=False)
adult_keyboard.add_button('Для ребёнка 👧🏻👦🏻')
adult_keyboard.add_button('Для взрослого 👩🏻👨🏻')

kid_pool_keyboard = VkKeyboard(one_time=False)
kid_pool_keyboard.add_button('Бассейн Swim Shot')
kid_pool_keyboard.add_button('СК «Орбита»')
kid_pool_keyboard.add_line()
kid_pool_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

kid_type_keyboard = VkKeyboard(one_time=False)
kid_type_keyboard.add_button('Групповые')
kid_type_keyboard.add_button('Персональные')
kid_type_keyboard.add_button('Свободное плавание')
kid_type_keyboard.add_line()
kid_type_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

kid_type_keyboard_orbita = VkKeyboard(one_time=False)
kid_type_keyboard_orbita.add_button('Групповые')
kid_type_keyboard_orbita.add_line()
kid_type_keyboard_orbita.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

kid_age_k18_keyboard = VkKeyboard(one_time=False)
kid_age_k18_keyboard.add_button('6-8')
kid_age_k18_keyboard.add_button('9-12')
kid_age_k18_keyboard.add_button('13-17')
kid_age_k18_keyboard.add_line()
kid_age_k18_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

kid_age_ankor_keyboard = VkKeyboard(one_time=False)
kid_age_ankor_keyboard.add_button('4-5')
kid_age_ankor_keyboard.add_button('6-8')
kid_age_ankor_keyboard.add_button('9-12')
kid_age_ankor_keyboard.add_button('13-17')
kid_age_ankor_keyboard.add_line()
kid_age_ankor_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

kid_age_orbita_keyboard = VkKeyboard(one_time=False)
kid_age_orbita_keyboard.add_button('2-3')
kid_age_orbita_keyboard.add_button('4-6')
kid_age_orbita_keyboard.add_line()
kid_age_orbita_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_kid_group_shot_6x8 = VkKeyboard(one_time=False)
trainer_keyboard_kid_group_shot_6x8.add_button('Дарья')
trainer_keyboard_kid_group_shot_6x8.add_button('Любовь')
trainer_keyboard_kid_group_shot_6x8.add_button('Илья')
trainer_keyboard_kid_group_shot_6x8.add_line()
trainer_keyboard_kid_group_shot_6x8.add_button('Александра')
trainer_keyboard_kid_group_shot_6x8.add_button('Анна')
trainer_keyboard_kid_group_shot_6x8.add_line()
trainer_keyboard_kid_group_shot_6x8.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_kid_group_shot_6x8.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_kid_group_shot_9x12 = VkKeyboard(one_time=False)
trainer_keyboard_kid_group_shot_9x12.add_button('Илья')
trainer_keyboard_kid_group_shot_9x12.add_button('Любовь')
trainer_keyboard_kid_group_shot_9x12.add_line()
trainer_keyboard_kid_group_shot_9x12.add_button('Анна')
trainer_keyboard_kid_group_shot_9x12.add_button('Александра')
trainer_keyboard_kid_group_shot_9x12.add_line()
trainer_keyboard_kid_group_shot_9x12.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_kid_group_shot_9x12.add_button('Назад', color=VkKeyboardColor.NEGATIVE)


trainer_keyboard_kid_group_shot_13x17 = VkKeyboard(one_time=False)
trainer_keyboard_kid_group_shot_13x17.add_button('Илья')
trainer_keyboard_kid_group_shot_13x17.add_button('Любовь')
trainer_keyboard_kid_group_shot_13x17.add_button('Анна')
trainer_keyboard_kid_group_shot_13x17.add_button('Александра')
trainer_keyboard_kid_group_shot_13x17.add_line()
trainer_keyboard_kid_group_shot_13x17.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_kid_group_shot_13x17.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_kid_group_orbita_2x6 = VkKeyboard(one_time=False)
trainer_keyboard_kid_group_orbita_2x6.add_button('Дарья')
trainer_keyboard_kid_group_orbita_2x6.add_button('Владимир')
trainer_keyboard_kid_group_orbita_2x6.add_line()
trainer_keyboard_kid_group_orbita_2x6.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_kid_group_orbita_2x6.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_kid_personal = VkKeyboard(one_time=False)
trainer_keyboard_kid_personal.add_button('Илья')
trainer_keyboard_kid_personal.add_button('Александра')
trainer_keyboard_kid_personal.add_line()
trainer_keyboard_kid_personal.add_button('Дарья')
trainer_keyboard_kid_personal.add_button('Сергей')
trainer_keyboard_kid_personal.add_button('Любовь')
trainer_keyboard_kid_personal.add_line()
trainer_keyboard_kid_personal.add_button('Анна')
trainer_keyboard_kid_personal.add_button('Владимир')
trainer_keyboard_kid_personal.add_line()
trainer_keyboard_kid_personal.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_kid_personal.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_adult_group = VkKeyboard(one_time=False)
trainer_keyboard_adult_group.add_button('Дарья')
trainer_keyboard_adult_group.add_button('Илья')
trainer_keyboard_adult_group.add_button('Анна')
trainer_keyboard_adult_group.add_line()
trainer_keyboard_adult_group.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_adult_group.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_adult_group_evn = VkKeyboard(one_time=False)
trainer_keyboard_adult_group_evn.add_button('Дарья')
trainer_keyboard_adult_group_evn.add_button('Анна')
trainer_keyboard_adult_group_evn.add_button('Александра')
trainer_keyboard_adult_group_evn.add_line()
trainer_keyboard_adult_group_evn.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_adult_group_evn.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

trainer_keyboard_adult_personal = VkKeyboard(one_time=False)
trainer_keyboard_adult_personal.add_button('Дарья')
trainer_keyboard_adult_personal.add_button('Илья')
trainer_keyboard_adult_personal.add_button('Александра ')
trainer_keyboard_adult_personal.add_line()
trainer_keyboard_adult_personal.add_button('Любовь')
trainer_keyboard_adult_personal.add_button('Александр А.')
trainer_keyboard_adult_personal.add_line()
trainer_keyboard_adult_personal.add_button('Александр Д.')
trainer_keyboard_adult_personal.add_button('Сергей')
trainer_keyboard_adult_personal.add_line()
trainer_keyboard_adult_personal.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
trainer_keyboard_adult_personal.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

price_keyboard = VkKeyboard(one_time=False)
price_keyboard.add_button('Отправь цены 💳')
price_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

signup_keyboard = VkKeyboard(one_time=False)
signup_keyboard.add_button('Хочу записаться 🤩')
signup_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

adult_pool_keyboard = VkKeyboard(one_time=False)
adult_pool_keyboard.add_button('Бассейн Swim Shot')
adult_pool_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

adult_type_keyboard = VkKeyboard(one_time=False)
adult_type_keyboard.add_button('Групповые')
adult_type_keyboard.add_button('Спина')
adult_type_keyboard.add_line()
adult_type_keyboard.add_button('Аквааэробика')
adult_type_keyboard.add_button('Свободное')
adult_type_keyboard.add_line()
adult_type_keyboard.add_button('Персональные ')
adult_type_keyboard.add_line()
adult_type_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

adult_daytime_keyboard = VkKeyboard(one_time=False)
adult_daytime_keyboard.add_button('Утром ☀️')
adult_daytime_keyboard.add_button('Вечером 🌚')
adult_daytime_keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

adult_group_trainer_keyb = VkKeyboard(one_time=False)
adult_group_trainer_keyb.add_button('Илья ')
adult_group_trainer_keyb.add_button('Дарья')
adult_group_trainer_keyb.add_button('Анна')
adult_group_trainer_keyb.add_line()
adult_group_trainer_keyb.add_button('Выбрать Тренера', color=VkKeyboardColor.POSITIVE)
adult_group_trainer_keyb.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

schedule_keyb = VkKeyboard(one_time=False)
schedule_keyb.add_button('Расписание 🗓️')
schedule_keyb.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

introd_keyb = VkKeyboard(one_time=False)
introd_keyb.add_button('Познакомь с Тренером 👋🏻')
introd_keyb.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

confirm_keyb = VkKeyboard(one_time=False)
confirm_keyb.add_button('Подтвердить', color=VkKeyboardColor.POSITIVE)
confirm_keyb.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

phone_keyb = VkKeyboard(one_time=False)
phone_keyb.add_button('Подтвердить', color=VkKeyboardColor.POSITIVE)
phone_keyb.add_button('Ввести заново')

end_keyb = VkKeyboard(one_time=True)
end_keyb.add_button('Новая заявка', color=VkKeyboardColor.PRIMARY)
