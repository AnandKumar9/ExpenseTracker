import csv
import functools
import Merchants
import os
import re

def parseTransactionsFromCSVFile():

    # directory = '/Volumes/GoogleDrive/My Drive/Synced/Monetary/Expenses/US/US Expenses/'
    directory = '/Users/anandkumar/Library/CloudStorage/GoogleDrive-write2anand.kumar@gmail.com/My Drive/Synced/Monetary/Expenses/US/US Expenses'

    matchingFilePaths = []
    for _, _, files in os.walk(directory):
        regex = re.compile('.*_transaction_download\.csv')
        for file in files:
            if regex.match(file):
                matchingFilePaths.append(os.path.join(directory, file))
                print(f'MATCHING FILE FOUND - {file}')

        # The first iteration happens on root folder, and only then does recursive iteration through sub-folders start. As recursive
        # iteration is not needed here, getting out of the loop after the first iteration.
        break

    if len(matchingFilePaths) != 1:
        print("Unexpected number of matching Transactions file")
        return

    filePath = matchingFilePaths[0]

    with open(filePath) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        allExpenses = []
        expensesBasedOnCategories = {expenseCategory: [] for expenseCategory in Merchants.ExpenseCategory}

        def populateExpensesInAllExpensesArray():
            line_count = 0
            for row in csv_reader:
                if len(row) == 0:
                    continue

                csv_rawMerchantName = row[3]
                csv_transactionDate = row[0]
                csv_transactionAmount = row[5]

                # Print csv column names
                if line_count == 0:
                    print(f'Columns in csv file:  {", ".join(row)}\n')
                    line_count += 1

                # Skip 'Credit' rows
                elif csv_transactionAmount == '':
                    continue

                else:
                    # Use a bunch of regular expressions to form a list of possible key names that will then be looked up in
                    # `merchants` dictionary for any possible match.
                    def getPossibleMerchantKeys() -> []:
                        candidateKeys = [csv_rawMerchantName]

                        csv_rawMerchantName_Words = csv_rawMerchantName.split()

                        csv_rawMerchantName_FirstWord = csv_rawMerchantName_Words[0].replace('\'', '')
                        candidateKeys.append(csv_rawMerchantName_FirstWord)

                        csv_rawMerchantName_FirstOneOrTwoWords = ((csv_rawMerchantName_Words[0] + " " + csv_rawMerchantName_Words[1])
                                                                  if (len(csv_rawMerchantName_Words) >= 2)
                                                                  else csv_rawMerchantName_Words[0]).replace('\'', '')
                        candidateKeys.append(csv_rawMerchantName_FirstOneOrTwoWords)

                        # Looks for leading 4-5 digits. Useful when a merchant has some 4-5 digits in beginning.
                        # Example - 10046 CAVA PIKE 7 PLZ
                        csv_rawMerchantName_TrimLeadingDigits = re.sub(r"(\d){4,5} (.*)", r"\2", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimLeadingDigits)
                        csv_rawMerchantName_TrimmedLeadingDigitsFirstWord = csv_rawMerchantName_TrimLeadingDigits.split()[0]
                        candidateKeys.append(csv_rawMerchantName_TrimmedLeadingDigitsFirstWord)

                        # Looks for trailing 4-5 digits. Useful when just the first word alone is not definitively distinct.
                        # Example - HAIR CUTTERY 1827
                        csv_rawMerchantName_TrimTrailingDigits = re.sub(r"(.*) (\d){4,5}", r"\1", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimTrailingDigits)
                        # print(row[3])
                        # print(csv_rawMerchantName_TrimLeadingDigits)
                        # Looks for patterns for payment provider LevelUp when followed by 4 digits
                        # Replaces `LEVELUP<MerchantName><4 digits>` with `<MerchantName>`
                        # Example - LEVELUPSWEETGREEN8555
                        csv_rawMerchantName_TrimLevelUp4Digits = re.sub(r"LEVELUP(.*)(\d){4}", r"\1", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimLevelUp4Digits)

                        # Looks for patterns for payment provider LevelUp when followed by 5 digits
                        # Replaces `LEVELUP<MerchantName><5 digits>` with `<MerchantName>`
                        # Example - LEVELUPSWEETLEAF35786
                        csv_rawMerchantName_TrimLevelUp5Digits = re.sub(r"LEVELUP(.*)(\d){5}", r"\1", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimLevelUp5Digits)

                        # Looks for patterns for payment providers PayPal, Square, Toast, Grubhub
                        # Replaces `PP<MerchantName>`, `TST <MerchantName>`, `SQ *<MerchantName>`, `GRUBHUB* <MerchantName>` with `<MerchantName>`
                        # Examples - PP*KUNG FU TEA, TST* TOOSSO PAKISTANI, SQ *BEN & JERRY'S FAIR, GRUBHUB* CHINAEXPRESS
                        csv_rawMerchantName_TrimProviders = re.sub(r"(PP\*|TST\* |TST\*|SQ \*|GRUBHUB\* )(.*)", r"\2", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimProviders)

                        # Looks for a specific patterns for Grubhub
                        # Replaces `GRUBHUB<MerchantName>` with `<MerchantName>`
                        # Examples - GRUBHUBCHINAEXPRESS
                        csv_rawMerchantName_TrimGrubhub = re.sub(r"(GRUBHUB)(.*)", r"\2", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimGrubhub)

                        # Peculiar patterns

                        # Example - Amazon Prime*HZ19307T3
                        csv_rawMerchantName_AmazonPrime = re.sub(r".*Amazon Prime.*", r"Amazon Prime", row[3])
                        candidateKeys.append(csv_rawMerchantName_AmazonPrime)

                        # Example - AAudible*SL5YB4EO3
                        csv_rawMerchantName_Audible = re.sub(r".*Audible.*", r"Audible", row[3])
                        candidateKeys.append(csv_rawMerchantName_Audible)

                        # Example - SQ *BEN & JERRY'S VIEN, SQ *BEN & JERRY'S FAIR.
                        csv_rawMerchantName_BenJerrys = re.sub(r".*BEN & JERRY'S.*", r"BEN & JERRY'S", row[3])
                        candidateKeys.append(csv_rawMerchantName_BenJerrys)

                        # Example - Prime Video*6E7CF3PO3
                        csv_rawMerchantName_PrimeVideo = re.sub(r"Prime Video.*", r"Prime Video", row[3])
                        candidateKeys.append(csv_rawMerchantName_PrimeVideo)

                        # Example - TST* SWEET LEAF - MCLE, TST* SWEET LEAF - VIEN
                        csv_rawMerchantName_SweetLeaf = re.sub(r".*Sweet Leaf.*", r"Sweet Leaf", row[3])
                        candidateKeys.append(csv_rawMerchantName_SweetLeaf)

                        # Example - TWP*SUB43231056
                        csv_rawMerchantName_WashingtonPost = re.sub(r"TWP\*.*", r"Washington Post", row[3])
                        candidateKeys.append(csv_rawMerchantName_WashingtonPost)

                        return candidateKeys

                    possibleKeys = getPossibleMerchantKeys()

                    def determineMerchantNameAndCategory():
                        for key in possibleKeys:
                            if key in Merchants.merchants:
                                return Merchants.merchants[key][0], Merchants.merchants[key][1]
                        return csv_rawMerchantName, Merchants.ExpenseCategory.Unknown

                    merchantName, merchantType = determineMerchantNameAndCategory()
                    transactionAmount = csv_transactionAmount
                    transactionDate = csv_transactionDate

                    # Shared expenses - Rent, Electricity Bill, Water Bill, Car Insurance

                    if merchantName == "Atley":
                        monthlyRent = 2409
                        transactionAmount = monthlyRent/2
                        standardGasBill = 15
                        waterBill = round(float(csv_transactionAmount) - monthlyRent - standardGasBill, 2)

                        monthlyRentExpense = Merchants.Expense(
                            rawMerchantName="Atley",
                            merchantName="Atley",
                            category=Merchants.ExpenseCategory.HouseRent,
                            transactionDate=csv_transactionDate,
                            transactionAmount=monthlyRent/2,
                            isShared=True
                        )
                        allExpenses.append(monthlyRentExpense)
                        expensesBasedOnCategories[monthlyRentExpense.category].append(monthlyRentExpense)

                        waterBillExpense = Merchants.Expense(
                            rawMerchantName="Water, Atley",
                            merchantName="Water, Atley",
                            category=Merchants.ExpenseCategory.WaterBill,
                            transactionDate=csv_transactionDate,
                            transactionAmount=waterBill/2,
                            isShared=True
                        )
                        allExpenses.append(waterBillExpense)
                        expensesBasedOnCategories[waterBillExpense.category].append(waterBillExpense)

                        gasBillExpense = Merchants.Expense(
                            rawMerchantName="Gas, Atley",
                            merchantName="Gas, Atley",
                            category=Merchants.ExpenseCategory.GasBill,
                            transactionDate=csv_transactionDate,
                            transactionAmount=standardGasBill/2,
                            isShared=True
                        )
                        allExpenses.append(gasBillExpense)
                        expensesBasedOnCategories[gasBillExpense.category].append(gasBillExpense)

                    elif merchantName == "Dominion Energy":
                        electricityExpense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName=merchantName,
                            category=Merchants.ExpenseCategory.ElectricityBill,
                            transactionDate=csv_transactionDate,
                            transactionAmount=round(float(transactionAmount)/2, 2),
                            isShared=True
                        )
                        allExpenses.append(electricityExpense)
                        expensesBasedOnCategories[electricityExpense.category].append(electricityExpense)

                    elif merchantName == "Progressive Car Insurance":
                        carInsuranceExpense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName=merchantName,
                            category=Merchants.ExpenseCategory.Car,
                            transactionDate=csv_transactionDate,
                            transactionAmount=round(float(transactionAmount)/2, 2),
                            isShared=True
                        )
                        allExpenses.append(carInsuranceExpense)
                        expensesBasedOnCategories[carInsuranceExpense.category].append(carInsuranceExpense)

                    elif merchantName == "7-Eleven" and transactionAmount == "2.18":
                        sevenElevenCoffeeExpense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName=merchantName,
                            category=Merchants.ExpenseCategory.Coffee,
                            transactionDate=csv_transactionDate,
                            transactionAmount=transactionAmount,
                            isShared=False
                        )
                        allExpenses.append(sevenElevenCoffeeExpense)
                        expensesBasedOnCategories[sevenElevenCoffeeExpense.category].append(sevenElevenCoffeeExpense)

                    elif merchantName == "APPLE.COM/BILL" and transactionAmount == "19.99":
                        chatGPTSubscriptionExpense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName="ChatGPT Subscription, Apple",
                            category=Merchants.ExpenseCategory.AllElse,
                            transactionDate=csv_transactionDate,
                            transactionAmount=transactionAmount,
                            isShared=False
                        )
                        allExpenses.append(chatGPTSubscriptionExpense)
                        expensesBasedOnCategories[chatGPTSubscriptionExpense.category].append(chatGPTSubscriptionExpense)

                    else:
                        expense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName=merchantName,
                            category=merchantType,
                            transactionDate=transactionDate,
                            transactionAmount=float(transactionAmount),
                            isShared=False
                        )
                        allExpenses.append(expense)
                        expensesBasedOnCategories[expense.category].append(expense)

                    def printExpense(expenseCategory=None, printAll=False):
                        if (merchantType == expenseCategory) or printAll:
                            print(f'{csv_transactionDate} - {merchantType.value} - {merchantName} - {csv_transactionAmount}')
                    # printExpense(printAll=True)
                    # printExpense(expenseCategory=Merchants.ExpenseCategory.Unknown)

                    line_count += 1

            print(f'PROCESSED {line_count} lines')
            print('------------------------------------------------------------------------------')
        populateExpensesInAllExpensesArray()

        def printExpenses(knownCategories):
            for expense in allExpenses[::-1]:
                if (knownCategories and expense.category != Merchants.ExpenseCategory.Unknown) or \
                        (not knownCategories and expense.category == Merchants.ExpenseCategory.Unknown):
                    a = expense.merchantName.replace('\'', '\\\'')
                    print(f'\'{expense.transactionDate} : {expense.category.value} : {a} : {expense.transactionAmount}\',')

        printExpenses(knownCategories=True)
        printExpenses(knownCategories=False)
        print('------------------------------------------------------------------------------')

        def printExpensesBasedOnCategories(detailed=False):
            sumAcrossAllCategories = round(functools.reduce(lambda a, expense: a + float(expense.transactionAmount), allExpenses, 0), 2)
            print(f'TOTAL : ${sumAcrossAllCategories}')
            for expenseCategory in expensesBasedOnCategories:
                categoryTransactionsList = list(map(lambda expense: float(expense.transactionAmount),
                                                    expensesBasedOnCategories[expenseCategory]))
                categoryTransactionsSum = round(functools.reduce(lambda a, b: a + b, categoryTransactionsList, 0), 2)
                print(f'{expenseCategory.value}: {(len(categoryTransactionsList))} times - {categoryTransactionsSum}')

            if not detailed:
                return

            for category in Merchants.ExpenseCategory:
                categoryExpensesBasedOnDates = {}
                totalAmount = 0
                for expense in expensesBasedOnCategories[category]:
                    totalAmount += float(expense.transactionAmount)
                    if expense.transactionDate in categoryExpensesBasedOnDates:
                        transactionsSum, transactionsMerchants = categoryExpensesBasedOnDates[expense.transactionDate]
                        updatedMerchantList = transactionsMerchants
                        updatedMerchantList.append(f'{expense.transactionAmount} - {expense.merchantName}')
                        categoryExpensesBasedOnDates[expense.transactionDate] = (transactionsSum + float(
                            expense.transactionAmount)), updatedMerchantList
                    else:
                        categoryExpensesBasedOnDates[expense.transactionDate] = float(expense.transactionAmount), [
                            f'{expense.transactionAmount} - {expense.merchantName}']

                print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

                print(f'{category} - {len(expensesBasedOnCategories[category])} times on {(len(categoryExpensesBasedOnDates.keys()))} days - ${round(totalAmount, 2)}')
                for expenseDate in categoryExpensesBasedOnDates:
                    totalAmount, merchants = categoryExpensesBasedOnDates[expenseDate]
                    print(f'{expenseDate} : ${round(totalAmount, 2)} : {merchants}')

            print('------------------------------------------------------------------------------')
        printExpensesBasedOnCategories(detailed=False)
        print('------------------------------------------------------------------------------')


        def printSharedExpenses():
            for expense in allExpenses[::-1]:
                if expense.isShared:
                    a = expense.merchantName.replace('\'', '\\\'')
                    print(f'\'{expense.transactionDate} : {expense.category.value} : {a} : {expense.transactionAmount*2}\',')
        print("SHARED EXPENSES:")
        printSharedExpenses()
