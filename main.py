from tkinter import *
class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.pack()
		self.creatWidgets()
	
	def creatWidgets(self):
		self.hellolabel = Label(self,text="hello world!")
		self.hellolabel.pack()
		self.quitbutton = Button(self, text='Quit',command=self.quit)
		self.quitbutton.pack()
		
app = Application()
# 设置窗口标题
app.master.title('hello world')
# 主消息循环
app.mainloop()
		