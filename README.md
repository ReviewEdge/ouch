# ouch
Ouch helps you keep track of spending.

# help
* Example input:
    - gas 65.23
    - 1.23 g
* To get weekly totals, just send total (or "tot" for short) + the name of the category, or no category to see your overall total
    
    examples:
    - tot gas
    - total
* Accepted input formats:
   * [category] [amount] [currency]
   * [amount] [currency]
   * [category] [amount]
   * [amount] 
* Categories cannot contain only digits 
* Inputs must be divided by spaces
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
