import os, time, datetime
import LogAutomation as Log


_OutlookLog = ""
_Date = time.strftime("%m/%d/%Y")
_Time = datetime.datetime.time(datetime.datetime.now())

def openMail():
    try:
        os.startfile('OUTLOOK.EXE')
        _OutlookLog = str("Outlook Opened")

    except Exception as e:
        _OutlookLog = str("Error Opening Outlook.\nError Message: " + str(e))

    Log.openLog(_Date, _Time, _OutlookLog)