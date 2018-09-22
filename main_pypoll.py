import os
import csv

ElecDataCSV = os.path.join(".", "Resources", "election_data.csv")

TotalnumofVotes=0
CanditatesVotes={}
a = 0


# with open(udemy_csv, newline="", encoding='utf-8') as csvfile:
with open(ElecDataCSV, newline="") as ElecDataCSVfile:
    CsvReader = csv.reader(ElecDataCSVfile, delimiter=",")
    CsvHeader = next(CsvReader)
   
    
    for row in CsvReader:
        TotalnumofVotes = TotalnumofVotes + 1
        if row[2] not in CanditatesVotes:
            CanditatesVotes[row[2]] = a
        if row[2]  in CanditatesVotes:
               CanditatesVotes[row[2]] = CanditatesVotes.get(row[2]) +1

    
    print("Election Results")
    print("---------------------")
    print(f"Total Votes : {TotalnumofVotes}")
    print("---------------------")
    
    for key in  CanditatesVotes:
        print(f" {key}:{(CanditatesVotes[key]/TotalnumofVotes) * 100}% ({CanditatesVotes[key]})")









