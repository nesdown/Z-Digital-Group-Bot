import keyboards as k
from credentials import bot

app_price = {}

# Which platform should be chosen (Android, iOS, Both, Web)
def step_1(message, price, choice):
  bot.send_message(message.chat.id, "*Под какую платформу* предполагается приложение?", reply_markup=k.keyboard_1_screen, parse_mode='Markdown')

# Do you need a design? (Yes, No)
def step_2(message, price, choice):
  global app_price
  app_price[message.chat.id] = 0
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nНужен ли Вам *дизайн проекта*?", reply_markup=k.keyboard_2_screen, parse_mode='Markdown')

# How many screens does your app have? (1-6, 7-12, 13-20, 21+)
def step_3(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\n*Сколько примерно экранов* в Вашем приложении?", reply_markup=k.keyboard_3_screen, parse_mode='Markdown')

# How will your users log in (Email+Password, Via Social Networks, 2-Step, Nothing)
def step_4(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nКак будет реализована *авторизация* пользователей?", reply_markup=k.keyboard_4_screen, parse_mode='Markdown')

# How do you wish to secure? (Do not need, Simple Security, Basic Security, Complex Security)
def step_5(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nКакой *тип безопасности данных* нужно реализовать в приложении?", reply_markup=k.keyboard_5_screen, parse_mode='Markdown')

# Which 3rd party do you need? (Social Networks, Location, Media, eCommerce)
def step_6(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nКакие *сторонние сервисы* Вам нужны?", reply_markup=k.keyboard_6_screen, parse_mode='Markdown')

# Do you need an admin features? (User Management, Content Management, Analytics, News, Nothing)
def step_7(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nКакие элементы управления нужны в *панели Администратора?*", reply_markup=k.keyboard_7_screen, parse_mode='Markdown')

# Which additional features do you need? (Actifity Feed, In-app purchases, Shopping cart, Search, Referral System, Chatting, Ratings&Reviews, Integration, Nothing)
def step_8(message, price, choice):
  global app_price
  app_price[message.chat.id] += price

  bot.send_message(message.chat.id, "Текущая стоимость: *" + str(app_price[message.chat.id]) + "$*. \n\nКакие *дополнительные функции* нужны в приложении?", reply_markup=k.keyboard_8_screen, parse_mode='Markdown')

def final(message):
  global app_price
  bot.send_message(382372945, "Этот пользователь посчитал свой проект: @" + message.from_user.username)

  bot.send_message(message.chat.id, "Готово! *Итоговая стоимость: " + str(app_price[message.chat.id]) + "$*", parse_mode='Markdown')

  bot.send_message(message.chat.id, "*Готовы приступить к дальнейшему обсуждению проекта*? Оставьте Ваши *контактные данные* - мы будем рады ответить!", parse_mode='Markdown')

def say_goodbye(message):
  print(message.json)
  bot.send_message(382372945, "Пользователь @" + message.from_user.username + " оставил свои контактные данные: " + message.json['text'])

  bot.send_message(message.chat.id, "Спасибо, что воспользовались нашим калькулятором!\nМы свяжемся с Вами *в ближайшее время*. Хорошего дня!", parse_mode='Markdown')
