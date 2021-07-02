import webbrowser, time, datetime
import LogAutomation as log

_FireFoxLog = ""
_Date = time.strftime("%m/%d/%Y")
_Time = datetime.datetime.time(datetime.datetime.now())


def openFireFox():
    try:
        #webbrowser.open("https://wearlenses.slack.com/")
        #webbrowser.open("https://trello.com/b/H7f9C7jE/welcome-board")
        webbrowser.open("https://kallysoft-alcon.atlassian.net/issues/?filter=15181&jql=reporter%20in%20(currentUser())%20ORDER%20BY%20updated%20DESC%2C%20created%20DESC%2C%20key%20ASC%2C%20summary%20ASC")
        _FireFoxLog ="FireFox Opened.\nhttps://wearlenses.slack.com/ Opened.\nhttps://trello.com/b/H7f9C7jE/welcome-board Opened.\nhttps://kallysoft-alcon.atlassian.net/issues/?filter=15181&jql=reporter%20in%20(currentUser())%20ORDER%20BY%20updated%20DESC%2C%20created%20DESC%2C%20key%20ASC%2C%20summary%20ASC Opened"

    except Exception as e:
        _FireFoxLog = "Error opening URL: " + str(e)

    log.openLog(_Date, _Time, _FireFoxLog)

