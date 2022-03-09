from telethon import TelegramClient, events
from forex_python.converter import CurrencyRates
import re
import config

api_id = config.my_api_id
api_hash = config.my_api_hash
bot_token = config.my_bot_token

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


def track_spend(message):
    # gets rid of leading dollar sign
    message = message.replace("$", "")
    delim = message.split()

    try:
        total = float(delim[0])
    except ValueError:
        return "Invalid input"

    # ignores if parameters are missing and assumes usd spend
    try:
        currency = delim[1]
    except IndexError:
        currency = "u"

    if (currency == "e") or (currency == "€"):
        c = CurrencyRates(force_decimal=False)
        total = c.convert("EUR", "USD", total)

    # if currency == "g" or "£":
    #     c = CurrencyRates(force_decimal=False)
    #     total = c.convert("GBP", "USD", total)

    return "tracking $" + "{:.2f}".format(total) + " USD"


@bot.on(events.NewMessage)
async def my_event_handler(event):
    if re.search(r'\d', event.raw_text):
        await event.reply(track_spend(event.raw_text))

    if "undo" in event.raw_text:
        print("this is where you undo the last db transaction")


bot.start()
bot.run_until_disconnected()
