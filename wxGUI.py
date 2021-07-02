import wx


class bucky(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Error Occurred', size=(300, 235))
        panel = wx.Panel(self)

        status = self.CreateStatusBar()

        # Creating the MenuBar
        menubar = wx.MenuBar()

        # Creating two menu buttons for the menu bar
        first = wx.Menu()
        second = wx.Menu()

        # adding title and description to the buttons
        first.Append(wx.NewId(), "More Info", "This will give more info on what Error occurred")
        second.Append(wx.NewId(), "Quit", "Close the window/frame")

        # Adding two menu items to the menubar
        menubar.Append(first, "File")  # Adds the FILE menu to the first menubar item
        menubar.Append(second, "Exit")  # Adds the EXIT menu to the second menubar item
        self.SetMenuBar(menubar)  # Sets the new menubar with appended items

        # BUTTONS
        button = wx.Button(panel, label="OK", pos=(115, 120), size=(60, 30))
        self.Bind(wx.EVT_BUTTON, self.closebutton,
                  button)  # binds the button click event to the button, and calls the closebutton function
        self.Bind(wx.EVT_CLOSE,
                  self.closewindow)  # binds the close even to the button and calls the closewindow function

    def closebutton(self, event):
        self.Close(True)  #

    def closewindow(self, event):
        self.Destroy()  # Destroy the window/Frame


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = bucky(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
