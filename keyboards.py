import telebot

# Which platform should be chosen (Android, iOS, Both, Web)
keyboard_1_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_1_screen.row('🤖 Android', '🍏 iOS')
keyboard_1_screen.row('💪 Обе платформы', "🌐 Web")

# Do you need a design? (Yes, No)
keyboard_2_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_2_screen.row('🖌️ Да, мне нужен дизайн!', '😎 Нет, обойдусь!')

# How many screens does your app have? (1-6, 7-12, 13-20, 21+)
keyboard_3_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_3_screen.row('😇 1-6', '🙂 7-12', '🙃 13-20', '😈 21+')

# How will your users log in (Email+Password, Via Social Networks, 2-Step, Nothing)
keyboard_4_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_4_screen.row('📬 Email и Пароль', '☮️ Через соц.сети')
keyboard_4_screen.row('🔐 2-х факторная аутентификация', '😎 Логина не будет')

# How do you wish to secure? (Do not need, Simple Security, Basic Security, Complex Security)
keyboard_5_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_5_screen.row('💾 Простой', '🔒 Базовый')
keyboard_5_screen.row('🔫 Комплексный', '😎 Обойдусь!')

# Which 3rd party do you need? (Social Networks, Location, Media, eCommerce)
keyboard_6_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_6_screen.row('🌐 Социальные Сети', '🗺️ Геолокация')
keyboard_6_screen.row('🖼️ Медиа', '💳 eCommerce')
keyboard_6_screen.row('⏩ Далее!')

# Do you need an admin features? (User Management, Content Management, Analytics, News, Nothing)
keyboard_7_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_7_screen.row('👥 Управление пользователями', '🗣️ Управление контентом')
keyboard_7_screen.row('📈 Аналитика и статистика', '📑 Добавление новостей')
keyboard_7_screen.row('❌ Ничего не надо!', '⏩ Готово, дальше!')

# Which additional features do you need? (Actifity Feed, In-app purchases, Shopping cart, Search, Referral System, Chatting, Ratings&Reviews, Integration, Nothing)
keyboard_8_screen = telebot.types.ReplyKeyboardMarkup(True, True, True)
keyboard_8_screen.row('🔔 Лента активности (feed)', '💰 Встроенные покупки')
keyboard_8_screen.row('🛒 Корзина', '🔎 Поиск')
keyboard_8_screen.row('💵 Реферральная система', '📨 Чаты')
keyboard_8_screen.row('📊 Рейтинг и отзывы', '🛠️ Итеграция внешних сервисов (напр. CRM)')
keyboard_8_screen.row('😎 Ничего не нужно', '⏩ Все выбрал(а)')
