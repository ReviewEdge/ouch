from telethon import TelegramClient, events
from forex_python.converter import CurrencyRates
import re
import database_connector as dbc
import config

api_id = config.my_api_id
api_hash = config.my_api_hash
bot_token = config.my_bot_token

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


def is_float(element):
    try:
        float(element)
        return True
    except ValueError:
        return False


def track_spend(user_id, message):
    # gets rid of leading dollar sign
    message = message.replace("$", "")

    delim = message.split()

    """
        accepted inputs:
            gf 4 e
            4 e
            gf 4
            4
    """

    currency = "u"
    category = None

    if len(delim) == 3:
        category = delim[0]
        if is_float(delim[1]):
            total = delim[1]
        else:
            return "Invalid input"
        currency = delim[2]

    elif len(delim) == 2:
        if is_float(delim[0]):
            total = delim[0]
            currency = delim[1]
        elif is_float(delim[1]):
            category = delim[0]
            total = delim[1]
        else:
            return "Invalid input"
    elif (len(delim) == 1) and (is_float(delim[0])):
        total = delim[0]
    else:
        return "Invalid input"

    total = float(total)

    # converts from Euros
    if (currency == "e") or (currency == "€"):
        c = CurrencyRates(force_decimal=False)
        total = c.convert("EUR", "USD", total)

    # converts from Great British Pounds
    if (currency == "g") or (currency == "£"):
        c = CurrencyRates(force_decimal=False)
        total = c.convert("GBP", "USD", total)

    # converts from Romanian Leis
    if currency == "l":
        c = CurrencyRates(force_decimal=False)
        total = c.convert("RON", "USD", total)

    total = round(total, 2)

    print("created spend " + str(dbc.create_spend(user_id, total, category)) + " for user " + user_id)
    return "tracking $" + "{:.2f}".format(total) + " USD in category: " + str(category)


def send_sum(user_id, message):
    delim = message.split()

    if len(delim) <= 1:
        try:
            output = "All-time total: $" + str(dbc.get_all_spend_cost_sum(user_id))
        except TypeError:
            output = "You haven't tracked anything yet"
    else:
        category = delim[1]
        try:
            output = "All-time total in \"" + category + "\" is $" + str(dbc.get_cost_sum_in_cat(user_id, category))
        except TypeError:
            output = "Category not found"

    return output


def send_weekly_sum(user_id, message):
    delim = message.split()

    if len(delim) <= 1:
        try:
            output = "Total since Monday: $" + str(dbc.get_all_weekly_sum(user_id))
        except TypeError:
            output = "You haven't tracked anything yet"
    else:
        category = delim[1]
        try:
            output = "Total since Monday in \"" + category + "\" is $" + str(dbc.get_weekly_sum_in_cat(user_id, category))
        except TypeError:
            output = "Category not found"

    return output


def send_all_time_report(user_id):
    try:
        output = dbc.get_all_time_report(user_id)
    except TypeError:
        output = "You haven't tracked anything yet"
    return output


def send_weekly_report(user_id):
    try:
        output = dbc.get_weekly_report(user_id)
    except TypeError:
        output = "You haven't tracked anything yet"
    return output


# read new messages
@bot.on(events.NewMessage)
async def new_message_handler(event):
    event.raw_text = event.raw_text.lower()
    user_id = str(event.peer_id.user_id)

    # creates new table if new user
    if dbc.check_if_new_user(user_id):
        print("found new user: " + user_id)
        print(dbc.add_new_user_to_db(user_id))

    if "?" in event.raw_text:
        await event.reply("""   
* Example tracking input:
    gas 65.23
* To get weekly (since Monday) totals, send total (or "tot" for short) plus the name of the category, or no category to see your overall total
* To get a weekly spending report, send report, and you will see your spending across all categories
    examples:
    tot gas
    report
* Accepted inputs:
    [category] [amount] [currency]
    [amount] [currency]
    [category] [amount]
    [amount] 
* Categories cannot contain only digits
* Capital letters are ignored
* Currently supported currencies: 
    - default: US Dollar
    - Euro (e)
    - Great British Pound (g)
* You can undo a tracking by entering a negative amount
    (for example: "food -3.45 e")
* You can get an all-time report or all-time totals using alltimereport or alltimetot
        """)

    elif "alltimetot" in event.raw_text:
        await event.reply(send_sum(user_id, event.raw_text))

    elif "tot" in event.raw_text:
        await event.reply(send_weekly_sum(user_id, event.raw_text))

    elif "alltimereport" in event.raw_text:
        await event.reply(send_all_time_report(user_id))

    elif "report" in event.raw_text:
        await event.reply(send_weekly_report(user_id))

    # tracks spend if message contains numbers
    elif re.search(r'\d', event.raw_text):
        await event.reply(track_spend(user_id, event.raw_text))


# run the bot
if __name__ == '__main__':
    bot.start()
    print("Running...")
    bot.run_until_disconnected()
