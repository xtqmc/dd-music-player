from tkinter.ttk import *
from tkinter import *
from tkinter import font
from browser import b

class GUI(Frame):

	def __init__(self, parent, *args, **kwargs):
		Frame.__init__(self, parent)
		self.parent = parent
		self.init_ui()

	def init_ui(self):
		self.parent.title('Python Music Player')
		self.pack(fill = BOTH, expand = 1)

		small_font = font.Font(size = 12)

		self.lb = Listbox(self, font=small_font)
		self.lb.pack(fill = BOTH, expand = 1)

		self.lb.insert(END, 'Back')
		for item in b.curlist():
			self.lb.insert(END, item)

		self.lb.bind('<Return>', self.on_select)

		self.lb.bind('<p>', self.on_pause)
		self.lb.bind('<o>', self.on_next)
		self.lb.bind('<i>', self.on_prev)

		self.lb.focus_set()
		self.lb.selection_set(0)

	def on_select(self, val):
		newlist = []

		if val.widget.get(val.widget.curselection()[0]) == 'Back':
			newlist = b.back()
		else:
			newlist = b.select(val.widget.curselection()[0] - 1)

		if not self.lb.get(1, END) == tuple(newlist):
			print('refreshing')
			self.lb.delete(0, END)
			self.lb.insert(END, 'Back')
			for item in newlist:
				self.lb.insert(END, item)

		self.lb.selection_clear(0, END)
		self.lb.selection_set(0)

	def on_pause(self, val):
		b.togglepause()

	def on_next(self, val):
		b.next()

	def on_prev(self, val):
		b.prev()

def main():
	root = Tk()
	app = GUI(root)
	root.geometry('300x250+300+300')
	root.mainloop()
