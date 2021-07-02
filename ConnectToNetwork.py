import urllib.request, urllib.error, time, datetime
import LogAutomation as Log


_NetworkConnection = False
_NetworkConsoleLog = ""
_Date = time.strftime("%m/%d/%Y")
_Time = datetime.datetime.time(datetime.datetime.now())


def internet_on():
    try:
        urllib.request.urlopen('http://216.58.192.142', timeout=1)
        _NetworkConnection = True
        _NetworkConsoleLog = "Network Connection = " + str(_NetworkConnection)

    except urllib.error.URLError as err:
       _NetworkConnection = False
       _NetworkConsoleLog = "Network Connection = " + str(_NetworkConnection) + ". Error: " + str(err)

    Log.openLog(_Date, _Time, _NetworkConsoleLog)