import csv
import functools
import Merchants
import os
import re

def parseTransactionsFromCSVFile():

    directory = '/Volumes/GoogleDrive/My Drive/Synced/Monetary/Purse Strings/US/US Purse Strings/'

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

                        # Looks for trailing 4-5 digits. Useful when just the first word alone is not definitively distinct.
                        # Example - HAIR CUTTERY 1827
                        csv_rawMerchantName_TrimDigits = re.sub(r"(.*) (\d){4,5}", r"\1", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimDigits)

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

                        # Looks for patterns for payment providers PayPal, Square, Toast
                        # Replaces `PP<MerchantName>`, `TST <MerchantName>`, `SQ *<MerchantName>` with `<MerchantName>`
                        # Examples - PP*KUNG FU TEA, TST* TOOSSO PAKISTANI, SQ *BEN & JERRY'S FAIR
                        csv_rawMerchantName_TrimProviders = re.sub(r"(PP\*|TST\* |SQ \*)(.*)", r"\2", row[3])
                        candidateKeys.append(csv_rawMerchantName_TrimProviders)

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
                        csv_rawMerchantName_SweetLeaf = re.sub(r".*SWEET LEAF.*", r"SWEET LEAF", row[3])
                        candidateKeys.append(csv_rawMerchantName_SweetLeaf)

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

                    if merchantName == "Avalon Tysons Corner":
                        monthlyRent = 2335
                        transactionAmount = monthlyRent/2
                        waterBill = round(float(csv_transactionAmount) - monthlyRent, 2)

                        waterBillExpense = Merchants.Expense(
                            rawMerchantName=csv_rawMerchantName,
                            merchantName=merchantName,
                            category=Merchants.ExpenseCategory.WaterBill,
                            transactionDate=csv_transactionDate,
                            transactionAmount=waterBill
                        )
                        allExpenses.append(waterBillExpense)
                        expensesBasedOnCategories[waterBillExpense.category].append(waterBillExpense)

                    expense = Merchants.Expense(
                        rawMerchantName=csv_rawMerchantName,
                        merchantName=merchantName,
                        category=merchantType,
                        transactionDate=transactionDate,
                        transactionAmount=float(transactionAmount)
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

            print('------------------------------------------------------------------------------')

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
