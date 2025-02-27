#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import sys
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async
import re
from luhn import verify
import pymongo

# Logging configuration
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# MongoDB Connection
MONGO_URI = "your_mongodb_connection_string"
client = pymongo.MongoClient(MONGO_URI)
db = client.credit_cards

# Bot Configuration
developers = ['6440962840']
addusr = "6440962840"
TOKEN = "7393252205:AAG55M3Zv9cOnTVoHS3a3FDlMOzxVVAqPf4"
POSTING_CHANNEL = "https://t.me/barry_info"

# Function to start the bot
@run_async
def start(update, context):
    update.message.reply_text("This CC Scraper has been started successfully | Developed by [BARRY] Barry")

# Function to extract credit card details
@run_async
def extract(update, context):
    excluded_groups = ['-1002496101252,']  # List of groups to exclude

    try:
        chat_id = str(update.message.chat_id)
    except:
        return

    if chat_id not in excluded_groups and chat_id == POSTING_CHANNEL:
        raw_data = update.message.text

        # Regular expressions to identify credit card formats
        regex_16_digit = r"[0-9]{16}\|[0-9]{1,2}\|[0-9]{2,4}\|[0-9]{3}"
        regex_15_digit = r"[0-9]{15}\|[0-9]{1,2}\|[0-9]{2,4}\|[0-9]{4}"
        detect_visa = r"[0-9]{16}"
        detect_amex = r"[0-9]{15}"

        try:
            # Determine card type
            if re.findall(detect_visa, raw_data):
                card_number = re.findall(detect_visa, raw_data)[0]
                card_type = card_number[0]
            else:
                card_number = re.findall(detect_amex, raw_data)[0]
                card_type = card_number[0]

            # Extract card details
            if card_type == "3":
                extracted_card = re.findall(regex_15_digit, raw_data)[0]
            else:
                extracted_card = re.findall(regex_16_digit, raw_data)[0]

            # Check if card exists in database
            existing_card = db.credit_card.find_one({'cc_num': extracted_card.split("|")[0]})
            card_exists = bool(existing_card)

            # Verify card using Luhn Algorithm
            if not card_exists and verify(extracted_card.split("|")[0]):
                card_data = {
                    "bin": extracted_card[:6],
                    "cc_full": extracted_card,
                    "cc_num": extracted_card.split("|")[0]
                }
                db.credit_card.insert_one(card_data)

                formatted_message = f'''
CC: {extracted_card}
                '''
                context.bot.send_message(
                    chat_id=POSTING_CHANNEL,
                    text=formatted_message,
                    parse_mode='HTML'
                )
        except:
            pass

# Main function to start the bot using polling (suitable for VPS)
def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, extract))

    # Start bot with polling
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()