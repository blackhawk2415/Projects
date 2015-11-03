import wx

# app = wx.App()

# # the window is known as the frame

# frame = wx.Frame(None, -1, 'Window Title')
# frame.Show()

# app.MainLoop()



class windowClass(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(windowClass, self).__init__(*args, **kwargs)
		self.Centre()
		self.basicGUI()

	def basicGUI(self): #menu and drop down bar
		
		panel = wx.Panel(self)

		menuBar = wx.MenuBar()

		fileButton = wx.Menu()
		editButton = wx.Menu()

		importItem = wx.Menu()

		importItem.Append(wx.ID_ANY, 'Import Document')
		importItem.Append(wx.ID_ANY, 'Import Picture')
		importItem.Append(wx.ID_ANY, 'Import Video')

		fileButton.AppendMenu(wx.ID_ANY, 'Import', importItem)

		toolBar = self.CreateToolBar()

		#quitToolButton = toolBar.AddLabelTool(wx.ID_ANY, 'Quit')

		#toolBar.Realize()


		exitItem = wx.MenuItem(fileButton, wx.ID_EXIT, 'Quit')
		# exitItem.SetBitmap(wx.Bitmap('quit.png'))

		nameBox = wx.TextEntryDialog(None, 'Name?', 'Welcome', 'name')

		if nameBox.ShowModal() == wx.ID_OK:
			userName = nameBox.GetValue()


		exitItem = fileButton.Append(wx.ID_EXIT, 'Exit') #Button type and name in drop down

		menuBar.Append(fileButton, 'File')  # a & infront of a name, will create a shortkey
		menuBar.Append(editButton, 'Edit')

		self.SetMenuBar(menuBar)

		self.Bind(wx.EVT_MENU, self.Quit, exitItem)

		yesNoBox = wx.MessageDialog(None, 'Testing 123 Question', 'Box title', wx.YES_NO)
		yesNoAnswer = yesNoBox.ShowModal()
		yesNoBox.Destroy()

		

		if yesNoAnswer == wx.ID_NO:
			userName = 'Unamed Admin'

		ChooseOneBox = wx.SingleChoiceDialog(None, "Controls", 'Color Question', ['one', 'two', 
			'three'])

		if ChooseOneBox.ShowModal() == wx.ID_OK:
			response = ChooseOneBox.GetStringSelection()

		wx.TextCtrl(panel, pos=(150,50), size=(150,50))

		aweText = wx.StaticText(panel, -1, 'Label', (3,3))
		aweText.SetForegroundColour('yellow')
		aweText.SetBackgroundColour('black')

		self.SetTitle('Testing Window Name for ' + userName)

		self.Show(True)

	def Quit(self, e):
		self.Close()

def main():
	app = wx.App()
	windowClass(None)
	app.MainLoop()



if __name__ == '__main__':
	main()
