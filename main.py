from pyrogram import Client, filters, idle

# from decouple import config as getEnv

from pyrogram.types import Message

import asyncio

import re

import os



API_ID = 22092598

HASH_ID = "93de73c78293c85fd6feddb92f91b81a"

SESSION_ID = """6439956881"""



userbot = Client(name="barry", session_string=SESSION_ID, api_id=API_ID, api_hash=HASH_ID)



# add channel or group id where you want to forward the messages

forwardChannels = [-1002046472570]



# add owner id here

owner_ids = [6439956881]



# Scrape Limit is here

max_scrape_limit = 6000





def get_cards(message_text: str):



    nums = re.findall(r'\b[0-9]+\b', message_text)

    cards = [card for card in nums if len(card) == 15 or len(card) == 16]

    filterCards = list(

        filter(lambda x: x.startswith(("5", "6", "3", "4")), cards))

    return filterCards





def create_lista(text: str):

    m = re.findall(

        r'\d{15,16}(?:/|:|\|)\d+(?:/|:|\|)\d{2,4}(?:/|:|\|)\d{3,4}', text)

    lis = list(filter(lambda num: num.startswith(

        ("5", "4", "3", "6")), [*set(m)]))

    return [xx.replace("/", "|").replace(":", "|") for xx in lis]





def scrape_cards(text):

    try:

        if get_cards(text):

            card = re.findall(r'\b[0-9]+\b', text)

            ccn = get_cards(text)[0]

            mes = [mes for mes in card if int(mes) >= 1 and int(mes) <= 12]

            cvc = [cvc for cvc in card if len(cvc) >= 3 and len(cvc) <= 4]

            ano = [ano for ano in card if int(ano) >= 24 and int(

                ano) <= 2035 and len(ano) != 3]

            cvc = [cvc for cvc in cvc if len(

                cvc) >= 3 and not cvc.startswith("20")]

            return ["|".join([ccn, mes[0],  ano[0], cvc[0]])]

        else:

            return []

    except:

        return []





def get_urls(text):

    urls = re.findall(

        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)

    return [url for url in urls if url.startswith(("http://t.me/SayBarry", "https://t.me/SayBarry"))]





def extract_usernames(text):

    return re.findall(r'@\w+', text)\







@userbot.on_message(filters.command("start"))

async def start_bot(client, message: Message):

    if message.from_user and message.from_user.id in owner_ids:

        await message.reply_text(f"Hello {message.from_user.first_name}, your personal assistant.")

        return





@userbot.on_message(filters.command("scr"))

async def scrape_cards_bot(client, message: Message):

    if message.from_user and message.from_user.id in owner_ids:

        try:

            xx = await message.reply("Scraping...")

            args = message.command[1:3] if len(message.command) >= 3 else None

            if not args:

                await message.reply_text("Usage: /scr {username|chat_id} {limit}")

                return

            username, limit = args

            limit = int(limit) if limit.isdigit() else None

            if not limit:

                await message.reply_text("Limit must be a number")

                return



            if limit > 6000 :

    await message.reply_text(f"Limit must be less than {max_scrape_limit}.")

    return

            print(username, limit)

            cards = []

            messages = [msg async for msg in userbot.get_chat_history(username, limit) if msg and msg.text]

            scraper1 = [

                x for msg in messages if msg and msg.text for x in scrape_cards(msg.text)]

            cards.extend(scraper1)

            scraper2 = [

                x for msg in messages if msg and msg.text for x in create_lista(msg.text)]

            cards.extend(scraper2)

            if not cards:

                await message.reply_text(f"No cards found in {username}")

                return

            await xx.edit(f"Scraped {len(cards)} cards from {username}")

            filterCards = [*set(cards)]

            fln = f"x_{len(filterCards)}__cards.txt"



            with open(fln, "w", encoding="utf-8") as f:

                f.write("\n".join(filterCards))

            caption = f"Scraped {len(filterCards)} cards from {username}"

            await userbot.send_document(message.chat.id, fln, caption=caption)

            os.remove(fln)

            await xx.delete()

            return

        except Exception as e:

            await message.reply_text(f"Failed scrapping: {e}")

            return



    #  except Exception as e:

    #      await message.reply_text(f"Failed scrapping: {e}")

    #      return





@userbot.on_message(filters.command("join"))

async def join_bot(client, message: Message):



    text = message.text or ""

    if message.reply_to_message and message.reply_to_message.from_user:

        text = message.reply_to_message.text or ""



    if message.from_user and message.from_user.id in owner_ids:

        try:

            usernames = extract_usernames(text)

            if not usernames:

                usernames = get_urls(text)

            await userbot.join_chat(usernames[0])

            await message.reply_text(f"Joined {usernames[0]}")

            return

        except Exception as e:

            await message.reply_text(f"Failed to join: {e}")

            return







async def main():

    try:

        await userbot.start()

        me = await userbot.get_me()

        print(f"Barry : {me.username}")

        await idle()  # Keeps the bot running

    except Exception as e:

        print(f"An error occurred: {e}")

    finally:

        if userbot.is_connected:

            await userbot.stop()



if __name__ == '__main__':

    asyncio.run(main())
