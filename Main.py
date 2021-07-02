import ConnectToNetwork as NetConnect
import OpenOutlook as Outlook
import OpenFireFox as FireFox
import Nope as Nope
import os
import wx, wxGUI

def main():
    try:
        NetConnect.internet_on()
        Outlook.openMail()
        FireFox.openFireFox()

    except Exception as e:
        print("Error with Automation: " + str(e))
        app = wx.PySimpleApp()
        frame = wxGUI.bucky(parent=None, id=-1)
        frame.Show()
        app.MainLoop()
        #Nope.nope()

    os.startfile("AutomationLog.csv")

if __name__ == "__main__": main()