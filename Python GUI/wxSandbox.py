import wx


class SandBox(wx.Frame):
    
    def __init__(self, *args, **kwargs):
        super(SandBox, self).__init__(*args, **kwargs) 
            
        self.InitUI()
        self.Centre()
        
    def InitUI(self):

        menubar = wx.MenuBar()
        
        fileMenu = wx.Menu() # ---------------------- File Menu -------------------------
        
        # Main Labels
        fileMenu.Append(wx.ID_NEW, 'New')
        fileMenu.Append(wx.ID_NEW, 'Open')
        fileMenu.Append(wx.ID_NEW, 'Save')
        fileMenu.AppendSeparator()  # Seperator Item

        # Subgroup for Imports
        imp = wx.Menu()
        imp.Append(wx.ID_ANY, 'Import NewsFeed')
        imp.Append(wx.ID_ANY, 'Import Bookmarks')
        imp.Append(wx.ID_ANY, 'Import Mail')
        fileMenu.AppendMenu(wx.ID_ANY, 'Import', imp) # Append to File Menu


        #Exit
        fileMenu.Append(wx.ID_EXIT, 'Exit')
        menubar.Append(fileMenu, '&File') # Append File

        # Event Handliers
        self.Bind(wx.EVT_MENU, self.OnQuit, id=wx.ID_EXIT)

        # --------------------------panel ------------------------------
        panel = wx.Panel(self)
        
        sizer = wx.GridBagSizer(5, 5)

        text1 = wx.StaticText(panel, label="Java Class")
        sizer.Add(text1, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, 
            border=15)

        icon = wx.StaticBitmap(panel, bitmap=wx.Bitmap('exec.png'))
        sizer.Add(icon, pos=(0, 4), flag=wx.TOP|wx.RIGHT|wx.ALIGN_RIGHT, 
            border=5)

        line = wx.StaticLine(panel)
        sizer.Add(line, pos=(1, 0), span=(1, 5), 
            flag=wx.EXPAND|wx.BOTTOM, border=10)

        text2 = wx.StaticText(panel, label="Name")
        sizer.Add(text2, pos=(2, 0), flag=wx.LEFT, border=10)

        tc1 = wx.TextCtrl(panel)
        sizer.Add(tc1, pos=(2, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND)

        text3 = wx.StaticText(panel, label="Package")
        sizer.Add(text3, pos=(3, 0), flag=wx.LEFT|wx.TOP, border=10)

        tc2 = wx.TextCtrl(panel)
        sizer.Add(tc2, pos=(3, 1), span=(1, 3), flag=wx.TOP|wx.EXPAND, 
            border=5)

        button1 = wx.Button(panel, label="Browse...")
        sizer.Add(button1, pos=(3, 4), flag=wx.TOP|wx.RIGHT, border=5)

        text4 = wx.StaticText(panel, label="Extends")
        sizer.Add(text4, pos=(4, 0), flag=wx.TOP|wx.LEFT, border=10)

        combo = wx.ComboBox(panel)
        sizer.Add(combo, pos=(4, 1), span=(1, 3), 
            flag=wx.TOP|wx.EXPAND, border=5)

        button2 = wx.Button(panel, label="Browse...")
        sizer.Add(button2, pos=(4, 4), flag=wx.TOP|wx.RIGHT, border=5)

        sb = wx.StaticBox(panel, label="Optional Attributes")

        boxsizer = wx.StaticBoxSizer(sb, wx.VERTICAL)
        boxsizer.Add(wx.CheckBox(panel, label="Public"), 
            flag=wx.LEFT|wx.TOP, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Default Constructor"),
            flag=wx.LEFT, border=5)
        boxsizer.Add(wx.CheckBox(panel, label="Generate Main Method"), 
            flag=wx.LEFT|wx.BOTTOM, border=5)
        sizer.Add(boxsizer, pos=(5, 0), span=(1, 5), 
            flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT , border=10)

        button3 = wx.Button(panel, label='Help')
        sizer.Add(button3, pos=(7, 0), flag=wx.LEFT, border=10)

        button4 = wx.Button(panel, label="Ok")
        sizer.Add(button4, pos=(7, 3))

        button5 = wx.Button(panel, label="Cancel")
        sizer.Add(button5, pos=(7, 4), span=(1, 1),  
            flag=wx.BOTTOM|wx.RIGHT, border=5)

        sizer.AddGrowableCol(2)
        
        panel.SetSizer(sizer)



        viewMenu = wx.Menu() # ------------------------ view Menu ------------------------

        self.tool = viewMenu.Append(wx.ID_ANY, 'Show toolbar', 
            'Show Toolbar', kind=wx.ITEM_CHECK)
            
        viewMenu.Check(self.tool.GetId(), False)

        self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.tool)

        menubar.Append(viewMenu, '&View')

        self.toolbar = self.CreateToolBar()
        qtool = self.toolbar.AddLabelTool(wx.ID_ANY, 'Quit', wx.Bitmap('exit.png'))
        self.toolbar.Realize()
        self.toolbar.Hide()

        self.Bind(wx.EVT_TOOL, self.OnQuit, qtool)

        self.SetMenuBar(menubar)
        self.Show(True)


    def ToggleToolBar(self, e):
        
        if self.tool.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()       
        
    def OnQuit(self, e):
        self.Close()

def main():
    
    ex = wx.App()
    SandBox(None)
    ex.MainLoop()    


if __name__ == '__main__':
    main()