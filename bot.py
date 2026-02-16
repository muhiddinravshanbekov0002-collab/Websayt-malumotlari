import telebot
import os
from dotenv import load_dotenv
from handlers.order_handler import OrderHandler
from handlers.admin_handler import AdminPanel
from keyboards.keyboards import main_menu_keyboard, category_keyboard

# Load environment variables
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# Initialize handlers
order_handler = OrderHandler()
admin_panel = AdminPanel()

# Sample menu data
MENU_ITEMS = {
    'Burgers': [
        {'name': 'Klassik Burger', 'price': 15000, 'description': 'Klassik burger qoq va go\'shtning ajoyib kombinatsiyasi'},
        {'name': 'Double Burger', 'price': 25000, 'description': 'Ikki go\'sht pattysi bilan'},
        {'name': 'Spicy Burger', 'price': 20000, 'description': 'Achchiq va mazali'}
    ],
    'Pizza': [
        {'name': 'Margherita', 'price': 35000, 'description': 'Tomato, pishloq va basil'},
        {'name': 'Pepperoni', 'price': 40000, 'description': 'Pepperoni va pishloq'},
        {'name': 'Vegetarian', 'price': 30000, 'description': 'Sabzavotlar bilan pizza'}
    ],
    'Drinks': [
        {'name': 'Cola', 'price': 5000, 'description': 'Sovuq cola'},
        {'name': 'Juice', 'price': 8000, 'description': 'Tazelik mevali sharbat'},
        {'name': 'Coffee', 'price': 10000, 'description': 'Issiq kofe'}
    ]
}

# User carts
user_carts = {}

# START COMMAND
@bot.message_handler(commands=['start'])
def start_message(message):
    chat_id = message.chat.id
    user_name = message.from_user.first_name
    
    welcome_text = f"Assalamu alaikum, {user_name}! 👋\n\nFast Food Telegram Bot ga xush kelibsiz!\n\nQo'shimcha ma'lumot uchun /help ni bosing"
    
    bot.send_message(chat_id, welcome_text, reply_markup=main_menu_keyboard())

# HELP COMMAND
@bot.message_handler(commands=['help'])
def help_message(message):
    chat_id = message.chat.id
    help_text = """
📋 Mana buyruqlar:

/start - Botni qayta boshlash
/help - Yordam olish
/menu - Menyu ko'rish
/cart - Savat ko'rish
/orders - Mening buyurtmalarim
/admin - Admin paneli (faqat adminlar)
"""
    bot.send_message(chat_id, help_text)

# MENU COMMAND
@bot.message_handler(commands=['menu'])
def menu_message(message):
    chat_id = message.chat.id
    menu_text = "🍔 Kategoriyalarni tanlang:\n\n"
    
    bot.send_message(chat_id, menu_text, reply_markup=category_keyboard())

# CART COMMAND
@bot.message_handler(commands=['cart'])
def cart_message(message):
    chat_id = message.chat.id
    
    if chat_id not in user_carts or len(user_carts[chat_id]) == 0:
        bot.send_message(chat_id, "🛒 Sizning savatingiz bo'sh")
        return
    
    cart_text = "🛒 Savatingiz:\n\n"
    total = 0
    for item in user_carts[chat_id]:
        cart_text += f"{item['name']} - {item['price']} so'm x {item['quantity']}\n"
        total += item['price'] * item['quantity']
    
    cart_text += f"\n💰 Jami: {total} so'm"
    
    bot.send_message(chat_id, cart_text)

# CATEGORY SELECTION
@bot.message_handler(func=lambda message: message.text in MENU_ITEMS.keys())
def show_category(message):
    chat_id = message.chat.id
    category = message.text
    
    items_text = f"📍 {category} kategoriyasi:\n\n"
    
    for idx, item in enumerate(MENU_ITEMS[category], 1):
        items_text += f"{idx}. {item['name']} - {item['price']} so'm\n"
        items_text += f"   {item['description']}\n\n"
    
    bot.send_message(chat_id, items_text)

# TEXT MESSAGE HANDLER
@bot.message_handler(func=lambda message: True)
def handle_text(message):
    chat_id = message.chat.id
    text = message.text
    
    if "Qo'shish" in text or "qo'shish" in text.lower():
        add_to_cart_message(message)
    else:
        bot.send_message(chat_id, "❓ Kechirasiz, bu buyruqni tushunamadim. /help ni bosing.")

def add_to_cart_message(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Mahsulot nomini yozing:")

# POLLING
if __name__ == '__main__':
    print("🤖 Bot ishga tushdi...")
    bot.infinity_polling()