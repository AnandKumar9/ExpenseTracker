#### ExpenseTracker

1. Open the latest transactions csv in `US Expenses/Transactions History/` folder, and check the latest date it has QuickSilver card transactions for. Also, ensure that the actual sheet's latest QuickSilver transactions are for the same date. <br>
2. Download transactions from CapitalOne website with the start date being a date prior to the above date, and save it in `US Expenses/` folder. <br>
3. From the downloaded csv, remove any transactions for which entries have already been made in the sheet. <br>
4. Make manual entries for cash, checking account, 2 BOA credit cards, and FSA transactions. Again, ensure that any of these transactions are not already in the sheet. <br>
5. Run this Python script. <br>
6. Copy the formatted transactions from Console, paste in Google Sheet's script, modify all 'unknown' (and any other necessary) transactions to have the appropriate name and category, and run the Google Sheets script. <br> 
7. Move the local csv from `US Purse Strings/` to `US Expenses/Transactions History/` folder. <br>