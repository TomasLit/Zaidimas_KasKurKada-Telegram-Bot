"""The bot is called - Zaidimas_KasKurKada

This program is a chatbot that has built in some other features like: the game called - KasKurKada, it can show users information and being a chat bot - chat. 
Vocabulary of the bot is restricted to greetings and answering some simple questions like: how do you do, whats your name and similar. One of the features of chatbot
is that it answers to questions each time with different words. 

Program is based on two ConversationHandlers. The first one is main - it runs the whole program. The second one is for the game only. 

Also wanted to make the bot funny, so it has mean character like Bender from Futurama."""

import telegram
from telegram import Update
from telegram import ReplyKeyboardMarkup
from telegram.ext import (
    Updater,
    Filters,
    CommandHandler,
    MessageHandler,
    RegexHandler,
    ConversationHandler,
    CallbackContext
)
import warnings
warnings.filterwarnings("ignore")
import random
import key2 as K

updater = Updater(K.KEY, use_context=True)
dp = updater.dispatcher

bot = telegram.Bot(token=K.KEY)

greetings_eng = ['hey', 'hello', 'hi', 'it\'s great to see you', 'nice to see you', 'good to see you', 'good morning', 'good evening']
greetings_eng2 = ['Hey', 'Hello', 'Hi', 'It\'s great to see you', 'Nice to see you', 'Good to see you']
greetings_lt = ['labas', 'sveikas', 'sveika' 'sveiki', 'labas rytas', 'laba diena', 'labas vakaras']
greetings_lt2 = ['Labas', 'Sveiki', "Labas Humanoide"]
bye_eng = ['bye', 'bye-bye', 'goodbye', 'have a good day','stop']
bye_eng2 = ['Bye', 'Bye-Bye', 'Goodbye', 'Have a good day']
bye_lt = ['iki', 'ate', 'iki pasimatymo', 'viso', 'visogero', 'sudie', 'sudiev']
bye_lt2 = ['Iki', 'Ate', 'Viso', 'Visogero', 'Sudie', 'Sudiev']
thank_you_eng = ['thanks', 'thank you', 'thanks a bunch', 'thanks a lot.', 'thank you very much', 'thanks so much', 'thank you so much']
thank_you_eng2 = ['You\'re welcome.' , 'No problem.', 'No worries.', ' My pleasure.' , 'It was the least I could do.', 'Glad to help.']
thank_you_lt = ['ačiū', 'aciu', 'dekoju', 'dekingas', 'dėkoju', 'dėkingas']
thank_you_lt2 = ['Prašau', 'Visad smagu padėti', 'Nėr už ką']
help_eng = ['help', 'help me', 'rescue me']
help_lt = ['padėk', 'padek', 'padėkit', 'padekit', 'gelbėk', 'gelbek', 'gelbėkit', 'gelbekit', 'nusižudysiu', 'nusizudysiu']
vardas_lt = ['vardas?', 'vardas', 'koks tavo vardas?', 'koks tavo vardas', 'kuo tu vardu?', 'kuo tu vardu']
vardas_lt2 = ['Paklausk savo antros pusės - tau atsakys!', 'KalboBotas', 'Vakar biškį per daug elektronų išgėriau - nepamenu.']
kaip_sekasi = ['kaip sekasi?', 'kaip sekasi', 'kaip tau sekasi?', 'kaip tau sekasi', 'kaip einasi?', 'kaip einasi', 'kaip tau einasi?', 'kaip tau einasi', 'kas geresnio?', 'kas geresnio', 'ką tu?', 'ką tu', 'ka tu?', 'ka tu', 'ką gero?', 'ką gero', 'ka gero?', 'ka gero']
kaip_sekasi2 = [
    'Ai, žinai, ėjau aš Londono gatve pasiėmęs skėtį, tikėdamasis lietaus... tada netikėtai prisiminiau, kad aš neturiu skėčio ir eiti niekur negaliu, nes neturiu kojų, apie Londoną net nekalbu. Ir išvis tesu nuliukų ir vienetukų rinkinys.',
    'Blyn, sęęęęni, aš esu fakin programa, ko tu iš manęs nori?',
    'Uoj ką aš tau papasakosiu. Nepatikėsi. Olegas Šurajevas iš tikro yra atsiųstas iš ateities tam, kad išgelbėti žmoniją nuo Petro Gražulio.',
    'Nors užmušk, bet nieko nesakysiu, tu...'
    ]
ka_veiki = ['ką veiki?', 'ką veiki', 'ka veiki?', 'ka veiki', 'kuom užsiėmęs?', 'kuom užsiėmęs', 'kuom uzsiemes?', 'kuom uzsiemes']
ka_veiki2 = [
    'Bandau suprast kokias raides čia prikeverzojai.',
    'Ieškau kur investuoti elektrą.',
    'Bandau išgelbėti pasaulį? Skamba įtikinamai?',
    'Vakuoju stiklainius.',
    'Rengiuosi karui. Girdėjau Intelis bandys pulti AMD.'
    ]

def start(update: Update, context: CallbackContext):
    update.message.reply_text('Sveiki, humanoide, vardu- ' + update.message.from_user.first_name + '!!!')   
    update.message.reply_text('Jei pasimesi ir nežinosi ką toliau daryti, neliūdėk, tiesiog, paprašyk pagalbos. Aš moku nemažai žodžių, manau, susikalbėsim ;)' + '\n' + '\n' + 'Blogiausiu atveju, parašyk man laišką dvejetainiu kodu, tada tikrai rasim bendrą kalbą!')    
    keyboard = [['Žaidimas', 'Vartotojo informacija', 'Paplepėkim']]
    message = "Ką norėtumėte veikti sutvėrime iš mėsos ir kaulų, tfu,- žmogau?"
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    update.message.reply_text(message, reply_markup=reply_markup)
    
    return MENU
    
def menu(update: Update, context: CallbackContext):
    global user_response
    user_response_a = update.message.text
    user_response = user_response_a.lower()
    
    if(user_response == 'žaidimas'):
        update.message.reply_text('Atsakyki į klausimus, nepažįstamasai:')
        def intro(update: Update, context: CallbackContext)-> int:
            update.message.reply_text('Kada?') 
            return KADA

        def kada(update: Update, context: CallbackContext):
            global Kada
            Kada = update.message.text
            update.message.reply_text('Kas?')
            return KAS

        def kas(update: Update, context: CallbackContext)-> int:
            global Kas
            Kas = update.message.text
            update.message.reply_text('Ką?')
            return KA

        def ka(update: Update, context: CallbackContext)-> int:
            global Ka
            Ka = update.message.text
        
            a = ("Afrikoje", "Šiaurės ašigalyje", "didžiausiam pasaulio užpakalyje", "geriau neklausk kur", "Nikaragvoje", "Pabezdūnų kaime", "Sėdmaišių karalystėje", 
            "senos raganos trobelėje", "svečiuose pas Talibaną", "Putino bunkeryje", "pragare", "srutų duobėje", "filmavimo aikštelėje", "senų skutimosi peiliukų sąvartyne", "mėlynąjame banginyje")
            global Kur
            Kur = random.choice(a)
                
            b = ("Vaivorykštiniu vienaragiu", "jo didenybe Radžiu", "tavo motina", "Nitanu Gauseda", "mažuoju Hitleriu Gražuliu", "bomžu", "Daukantu", "Olegu", 
            "visų ertmių gydytoju", "žmogumi šaldytuvu", "Voodoo lėle", "Liuciferiu", "Grafu Bračiula", "Mis Naujoji Gvinėja 1974")
            global Su_kuo
            Su_kuo = random.choice(b)
            
            c = ("medžioja", "patruliuoja", "hipnotizuoja", "operuoja", "galvoja", "ovuliuoja", "svajoja apie", "klaidžioja po", "myli", "draugiškai nekenčia", 
            "tiesiog stovi", "apsimeta pavasariu", "mūkia kaip girtas praporščikas", "tepasi lydytu sviestu", "reanimuoja skruzdėlę", "bando nusižudyti švelniai")
            global Ka_veikia
            Ka_veikia = random.choice(c)

            update.message.reply_text(Kada.capitalize() + " " + Kur + " " + Kas + " su " + Su_kuo + " " + Ka_veikia + " " + Ka + ".")

            keyboard = [['Žaidimas', 'Vartotojo informacija', 'Paplepėkim']]
            message = ('Tu, kaip ten tave, - ' + update.message.from_user.first_name + ', ką nori veikt?')
            reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            update.message.reply_text(message, reply_markup=reply_markup)
            
            return ConversationHandler.END
        
        def quit(update: Update, context: CallbackContext):
            return ConversationHandler.END

        KADA, KAS, KA = 0, 1, 2
        handa = (ConversationHandler(
                entry_points=[RegexHandler('Žaidimas', intro)],
                states={
                    KADA: [MessageHandler(Filters.text, callback= kada)],
                    KAS: [MessageHandler(Filters.text, callback= kas)],
                    KA: [MessageHandler(Filters.text, callback= ka)]
                    },
                fallbacks=[CommandHandler('quit', quit)]
                ))

        dp.add_handler(handa, 2)

        updater.start_polling()
    
    elif(user_response == 'start' or user_response == '/start'):
        update.message.reply_text('Aš dirbu, nereikia čia manęs startint! Jei pasimetei ir nežinai ką daryt - šaukis pagalbos, tu pažeidžiamas, minkštas homo sapiens sapiens!')
        print(a)
        return MENU 
    
    elif(user_response in greetings_eng):
        a = random.choice(greetings_eng2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in greetings_lt):
        a = random.choice(greetings_lt2)
        update.message.reply_text(a)
        return MENU
    
    elif(user_response in bye_eng):
        a = random.choice(bye_eng2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in bye_lt):
        a = random.choice(bye_lt2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in thank_you_eng):
        a = random.choice(thank_you_eng2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in thank_you_lt):
        a = random.choice(thank_you_lt2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in help_eng): 
        keyboard = [['Žaidimas', 'Vartotojo informacija', 'Paplepėkim']]

        message = "What would you... gerai, neapsimetinėsiu, kad čia anglų moku - ko nori?"

        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard = True, resize_keyboard = True)
        update.message.reply_text(message, reply_markup=reply_markup)
        return MENU
      
    elif(user_response in help_lt):
        keyboard = [['Žaidimas', 'Vartotojo informacija', 'Paplepėkim']]

        message = "Ką norėtumėte veikti, Pone ar Panele, ar Pona... visi jūs man vienodi!"

        reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
        update.message.reply_text(message, reply_markup=reply_markup)
        return MENU
        
    elif(user_response in vardas_lt):
        a = random.choice(vardas_lt2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in kaip_sekasi):
        a = random.choice(kaip_sekasi2)
        update.message.reply_text(a)
        return MENU

    elif(user_response in ka_veiki):
        a = random.choice(ka_veiki2)
        update.message.reply_text(a)
        return MENU

    elif(user_response == 'paplepėkim' or user_response == 'let\'s chat'):
        update.message.reply_text('Uoj kaip man patinka plepėėėėt. Ateik čia, tuoj ką nors pasakysiu!')
        update.message.reply_text("""   Robotas moka pasisvekinti, atsisveikinti, padėkoti, pagelbėti ir atsakyti į keletą paprastų klausimų, tokių kaip: 
        "Kaip sekasi?", 
        "Ką veiki?", 
        "Koks tavo vardas? 
        Klausimai nebūtinai turi būti užduodami būtent tokia formuluote kaip parašyta. 
        Jeigu robotas kažko nesupranta, jis, tiesiog, tyli.""")
        return MENU
      
    elif(user_response == 'vartotojo informacija' or user_response == 'user information'):
            name = update.message.from_user.full_name
            username = update.message.from_user.username
            chat_id = update.message.chat.id
            msg_id = update.message.message_id
            update.message.reply_text(
            "Tavo vardas: " + str(name) + "\n" +
            "Tavo slapyvardis: " + str(username) + "\n" + 
            "Tavo chat ID: " + str(chat_id) + "\n" + 
            "Tavo msg ID: " + str(msg_id) 
            )
            keyboard = [['Žaidimas', 'Vartotojo informacija', 'Paplepėkim']]
            message = (update.message.from_user.first_name + ' ar kaip ten tave pavadino gimdytojai. Tai ką tu ten nori veikt?')
            reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
            update.message.reply_text(message, reply_markup=reply_markup)
            return MENU

def quit(update: Update, context: CallbackContext):
    return ConversationHandler.END

MENU = 0
hand = (ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        MENU: [MessageHandler(Filters.text, callback= menu)],
    },
    fallbacks=[CommandHandler('quit', quit)]
))

dp.add_handler(hand, 1)

import logging

logger = logging.getLogger(__name__)

def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

dp.add_error_handler(error)

updater.start_polling()

updater.idle()

