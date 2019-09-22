import telebot
from credentials import bot
import steps as s

step = {}

@bot.message_handler(commands=['start'])
def start_message(message):
  s.step_1(message, 0, "")
  step[message.chat.id] = 0

@bot.message_handler(content_types=['text'])
def process_step(message):
  global step

  # Step 1: Platform
  if ('android' in message.text.lower()) or ('ios' in message.text.lower()):
   s.step_2(message, 3900, "")
   step[message.chat.id] += 1

  elif 'обе платформы' in message.text.lower():
    s.step_2(message, 7800, "")
    step[message.chat.id] += 1

  elif 'web' in message.text.lower():
    s.step_2(message, 2600, "")
    step[message.chat.id] += 1

  # Step 2: Design
  elif 'да, мне нужен дизайн' in message.text.lower():
    s.step_3(message, 1500, "")
    step[message.chat.id] += 1

  elif 'нет, обойдусь' in message.text.lower():
    s.step_3(message, 0, "")
    step[message.chat.id] += 1

  # Step 3: Screens amount
  elif '1-6' in message.text.lower():
    s.step_4(message, 360, "")
    step[message.chat.id] += 1

  elif '7-12' in message.text.lower():
    s.step_4(message, 720, "")
    step[message.chat.id] += 1

  elif '13-20' in message.text.lower():
    s.step_4(message, 1080, "")
    step[message.chat.id] += 1

  elif '21+' in message.text.lower():
    s.step_4(message, 2040, "")
    step[message.chat.id] += 1

  # Step 4: Log in
  elif 'email и пароль' in message.text.lower():
    s.step_5(message, 400, "")
    step[message.chat.id] += 1

  elif ('через соц.сети' in message.text.lower()) or ('2-х факторная аутентификация' in message.text.lower()):
    s.step_5(message, 1000, "")
    step[message.chat.id] += 1

  elif 'логина не будет' in message.text.lower():
    s.step_5(message, 0, "")
    step[message.chat.id] += 1

  # Step 5: Security
  elif 'простой' in message.text.lower():
    s.step_6(message, 200, "")
    step[message.chat.id] += 1

  elif 'базовый' in message.text.lower():
    s.step_6(message, 400, "")
    step[message.chat.id] += 1

  elif 'комплексный' in message.text.lower():
    s.step_6(message, 800, "")
    step[message.chat.id] += 1

  elif 'обойдусь' in message.text.lower():
    s.step_6(message, 0, "")
    step[message.chat.id] += 1

  # Step 6: 3rd party
  elif 'социальные сети' in message.text.lower():
    s.step_6(message, 300, "")

  elif 'геолокация' in message.text.lower():
    s.step_6(message, 600, "")

  elif 'медиа' in message.text.lower():
    s.step_6(message, 800, "")

  elif 'ecommerce' in message.text.lower():
    s.step_6(message, 1500, "")

  elif 'далее' in message.text.lower():
    s.step_7(message, 0, "")
    step[message.chat.id] += 1

  # Step 7: admin
  elif 'управление пользователями' in message.text.lower():
    s.step_7(message, 600, "")

  elif 'управление контентом' in message.text.lower():
    s.step_7(message, 800, "")

  elif 'аналитика и статистика' in message.text.lower():
    s.step_7(message, 200, "")

  elif 'добавление новостей' in message.text.lower():
    s.step_7(message, 600, "")

  elif ('ничего не надо!' in message.text.lower()) or ('готово, дальше' in message.text.lower()):
    s.step_8(message, 0, "")
    step[message.chat.id] += 1

  elif ('лента активности (feed)' in message.text.lower()):
    s.step_8(message, 300, "")

  elif ('встроенные покупки' in message.text.lower()):
    s.step_8(message, 1000, "")

  elif ('корзина' in message.text.lower()):
    s.step_8(message, 300, "")

  elif ('поиск' in message.text.lower()):
    s.step_8(message, 100, "")

  elif ('реферральная система' in message.text.lower()):
    s.step_8(message, 2000, "")

  elif ('чаты' in message.text.lower()):
    s.step_8(message, 300, "")

  elif ('рейтинг и отзывы' in message.text.lower()):
    s.step_8(message, 200, "")

  elif ('итеграция внешних сервисов (напр. crm)' in message.text.lower()):
    s.step_8(message, 300, "")

  elif ('ничего не нужно' in message.text.lower()) or ('все выбрал(а)' in message.text.lower()):
    s.final(message)
    step[message.chat.id] += 1
    print(str(step[message.chat.id]))

  elif (step[message.chat.id] == 8):
    s.say_goodbye(message)

bot.infinity_polling()
