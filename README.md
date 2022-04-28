# ouch
Ouch is a Telegram bot that helps you keep track of spending.
With ouch you can track individual purchases by category and date, and then easily view a weekly or all-time spending report.
Ouch automatically creates a new account with it's own table in the database when you text it for the first time.
Ouch automatically converts between currencies, making it perfect for international travel.

# help
* Example input:
    - gas 65.23
    - 1.23 g
* To get weekly totals, just send total (or "tot" for short) + the name of the category, or no category to see your overall total
* Send report to see your spending across all categories for the week (since Monday), or alltimereport to see your alltime spending
    
    examples of input:
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
* You can get all-time totals using alltimetot

## ideas
* update help message
* fix weekly report not giving error message if no data yet
* code to make new db on first run
* undo!
* give full totals report
* sums by week, past 7 days, month
* set default category
* daily report, analysis
* help message
* get it running on raspberry pi
* change default currency
* ability to add description
  - some sort of key character before description input
