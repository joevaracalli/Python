#1 Trading Symbol
TradingSymbol = 'CS2067'
print ('Trading Symbol is = ' + TradingSymbol)

#2 Share Purchased on December 1st, 2018
Share_Price_Per_Share = 1.13
Share_Quantity = 5000
Total_Value_Of_Share = Share_Price_Per_Share * Share_Quantity
print "Price of share on Dec 1st is = " , Share_Price_Per_Share


#3 Shares sold on Jan 1, 2019
Value_Price_Per_Share = 1.59
Value_Quantity = 3567
Total_Value_Of_Shares_Sold = Value_Price_Per_Share * Value_Quantity

#4 The price stock on Jan 21, 2019
Share_Price_Per_Share = 1.80

#5 Calculate the profit(loss) for the item 3(trade on Jan 1)
After_Value = Share_Price_Per_Share * Share_Quantity
Profit_Lost = After_Value - Total_Value_Of_Shares_Sold

#6 What would be the profit selling the remaining shares on Jan 21
Remaining_Shares = Share_Quantity - Value_Quantity * Share_Price_Per_Share

#7 What is the total profit on the trades (item 3 and item 5)
Total_Profit_On_Trades = (Share_Price_Per_Share * Value_Quantity) - Total_Value_Of_Shares_Sold
