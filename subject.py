from telebot import types

bio = types.InlineKeyboardButton(text='Биология', callback_data='bio')
geo = types.InlineKeyboardButton(text='География', callback_data='geo')
art = types.InlineKeyboardButton(text='Искусство', callback_data='art')
his = types.InlineKeyboardButton(text='История', callback_data='his')
ikb = types.InlineKeyboardButton(text='ИКБ', callback_data='ikb')
lit = types.InlineKeyboardButton(text='Литература', callback_data='lit')
math = types.InlineKeyboardButton(text='Математика', callback_data='math')
phys = types.InlineKeyboardButton(text='Физика', callback_data='phys')
chm = types.InlineKeyboardButton(text='Химия', callback_data='chm')
com = types.InlineKeyboardButton('Обществознание', callback_data='com')