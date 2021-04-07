import requests
from telegram.ext import *


key='1770775770:AAGTJBPBF8tmMptfHoMmm1kGbT_AUC9zItE'

def responses(asset):
    
    asset=str(asset).lower()
    asset='http://api.coincap.io/v2/assets/'+asset
    request=requests.get(asset)
    is_positive=float(request.json()['data']['changePercent24Hr'])>=0
    text='Symbol:                 '+request.json()['data']['symbol']+'\n'
    text=text+'Price:                     '+str(round(float(request.json()['data']['priceUsd']),4))+' USD\n'
    text=text+'Change(24h):       '+'+'*is_positive+str(round(float(request.json()['data']['changePercent24Hr']),4))+' %\n\n\nStart another search by typing the name of a crypto asset:'
    return text



def start_command(update,context):
    update.message.reply_text('''Type the name of the crypto asset!''')

def handle_message(update,context):
    text=str(update.message.text)
    reponse= responses(text)
    update.message.reply_text(reponse)

def main():
    updater=Updater(key,use_context=True)
    dp=updater.dispatcher
    dp.add_handler(CommandHandler("start",start_command))
    dp.add_handler(MessageHandler(Filters.text,handle_message))

    updater.start_polling()
    updater.idle()

main()