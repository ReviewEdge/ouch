# ouch
Ouch is a Telegram bot that helps you keep track of spending.  Send a message (start with ? ) to @the_ouch_bot on Telegram to get stared.
# Features
- Track individual purchases by category and date
- View a weekly or all-time spending report, sorted by category
- View weekly or all-time totals in each or all categories
- Ouch automatically creates a new account with it's own table in the database when you text it for the first time
- Ouch automatically converts between currencies, making it perfect for international travel

# help
* Example input:
    - gas 65.23
    - 1.23 g
* To get weekly totals, just send total (or "tot" for short) + the name of the category, or no category to see your overall total
* Send report to see your spending across all categories for the week (since Monday), or alltimereport to see your alltime spending
    
    Examples:
    - gas 23
    - food 
    - tot gas
    - total
    - report
    - alltimereport
* Accepted tracking input formats:
   * [category] [amount] [currency]
   * [amount] [currency]
   * [category] [amount]
   * [amount] 
* Category names cannot contain only digits 
* Currently supported currencies: 
    - default: US Dollar
    - Euro (e)
    - Great British Pound (g)
* You can undo a tracking by entering a negative amount

    (for example: "food -3.45 e")
* You can get an all-time report or all-time totals using alltimereport or alltimetot