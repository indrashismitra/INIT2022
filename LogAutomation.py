import csv

def openLog(date, time, text):
    with open("AutomationLog.csv", "a") as log:
        csv_app = csv.writer(log)
        csv_app.writerow([date, time, str(text)])