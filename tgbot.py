import telebot 
from telebot import types 

from CRUD_and_List import ToDoList

bot = telebot.TeleBot("6227613925:AAHrfx0Z_cJ4Zf75g5xJ1pcvBTa0mAFiR_A")

todo_list = ToDoList()

commands = ['create', 'read', 'retrieve', 'update', 'delete']

# def set_keyboard():
#     keyboard = types.ReplyKeyboardMarkup()
#     for command in commands:
#         keyboard.row(command)
#     return keyboard

@bot.message_handler(commands=['start'])
def start_bot(message: types.Message):
    bot.send_message(message.chat.id, 'привет я бот созданный для управления твоим списком дел \nдля того чтобы добавить запись в список дел пропиши команду /create затем запись которую хочешь добавить \nдля того чтобы обновить какую либо запись введи команду /update затем через пробел номер записи и текст \n для того чтобы удалить запись введи команду /delete и номер записи через пробел \nдля того чтобы вывести на экран весь список дел введи команду /read \nдля того чтобы вывести определенную запись введи команду /retrieve и номер записи через пробел')

@bot.message_handler(commands=['create'])
def create_item(message: types.Message):
    item = message.text.replace('/create', '')
    todo_list.create(item)
    bot.send_message(message.chat.id, 'запись успешно добавлена')

@bot.message_handler(commands=['read'])
def read_items(message: types.Message):
    items = todo_list.read()
    if len(items) > 0:
        items_list = '\n'.join(items)
        bot.send_message(message.chat.id, f"Список дел:\n{items_list}")
    else: 
        bot.send_message(message.chat.id, "Список дел пуст")

@bot.message_handler(commands=['update'])
def update_item(message: types.Message):
    message_commands = message.text.split(" ")
    if len(message_commands) < 3:
        bot.send_message(message.chat.id, "Неверный формат команды. Используйте: /update <индекс> <текст>")
    
    todo_list.update(message_commands[1], message_commands[2])
    bot.send_message(message.chat.id, "Запись обновлена")
    
@bot.message_handler(commands=['delete'])
def delete_item(message: types.Message):
    pk = int(message.text.replace("/delete ", ""))
    todo_list.delete(pk)
    bot.send_message(message.chat.id, "Запись удалена")
    
@bot.message_handler(commands=['retrieve'])
def retrieve_item(message: types.Message):
    pk = int(message.text.replace("/retrieve ", ""))
    bot.send_message(message.chat.id, todo_list.retrieve(pk))
    


bot.polling()