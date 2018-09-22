import os
import csv

PyBankCSV = os.path.join(".", "Resources", "budget_data.csv")

TotalnumofMonths=1
TotalNetAmount = 0
TotalChange = 0
profit=0
loss=0


# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(PyBankCSV, newline="") as PyBankCSVfile:
    CsvReader = csv.reader(PyBankCSVfile, delimiter=",")
    CsvHeader = next(CsvReader)
    CsvRowPrev = next(CsvReader)
   
    TotalNetAmount = int(CsvRowPrev[1])
    
    for row in CsvReader:

        # Total number of months

        TotalnumofMonths = TotalnumofMonths+1

        TotalNetAmount = int(row[1]) + TotalNetAmount

        MonthlyChange = int(row[1]) - int(CsvRowPrev[1])

        TotalChange = MonthlyChange + TotalChange

        if MonthlyChange > 0:
            if MonthlyChange > profit:
                profit=MonthlyChange
                profitMonth=row[0]
        elif MonthlyChange < 0:
            if abs(MonthlyChange) > abs(loss):
                loss=MonthlyChange
                lossMonth=row[0]
        
        CsvRowPrev=row

        AverageChange=TotalChange/(TotalnumofMonths-1)


    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {TotalnumofMonths}")
    print(f"Total : {TotalNetAmount}")
    print(f"Average Change: {AverageChange}")
    print(f"Greatest Increase in Profits: {profitMonth} ({profit})")
    print(f"Greatest Increase in Profits: {lossMonth} ({loss})")



