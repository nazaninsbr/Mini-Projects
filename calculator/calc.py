from tkinter import *
from tkinter import ttk 


class Calculator:

	calc_value = 0.0
	div_trigger = False
	mult_trigger = False
	add_trigger = False
	sub_trigger = False

	def first_row_of_buttons(self, root):
		self.button7 = ttk.Button(root, text="7", command=lambda: self.button_press('7')).grid(row=1, column=0)
		self.button8 = ttk.Button(root, text="8", command=lambda: self.button_press('8')).grid(row=1, column=1)
		self.button9 = ttk.Button(root, text="9", command=lambda: self.button_press('9')).grid(row=1, column=2)

		self.button_div = ttk.Button(root, text="/", command=lambda: self.math_button_press('/')).grid(row=1, column=3)



	def second_row_of_buttons(self, root):
		self.button4 = ttk.Button(root, text="4", command=lambda: self.button_press('4')).grid(row=2, column=0)
		self.button5 = ttk.Button(root, text="5", command=lambda: self.button_press('5')).grid(row=2, column=1)
		self.button6 = ttk.Button(root, text="6", command=lambda: self.button_press('6')).grid(row=2, column=2)

		self.button_mult = ttk.Button(root, text="*", command=lambda: self.math_button_press('*')).grid(row=2, column=3)


	def third_row_of_buttons(self, root):
		self.button1 = ttk.Button(root, text="1", command=lambda: self.button_press('1')).grid(row=3, column=0)
		self.button2 = ttk.Button(root, text="2", command=lambda: self.button_press('2')).grid(row=3, column=1)
		self.button3 = ttk.Button(root, text="3", command=lambda: self.button_press('3')).grid(row=3, column=2)

		self.button_add = ttk.Button(root, text="+", command=lambda: self.math_button_press('+')).grid(row=3, column=3)

	def forth_row_of_buttons(self, root):
		self.button_ac = ttk.Button(root, text="AC", command=lambda: self.clear_button_press()).grid(row=4, column=0)
		self.button0 = ttk.Button(root, text="0", command=lambda: self.button_press('0')).grid(row=4, column=1)
		self.button_eq = ttk.Button(root, text="=", command=lambda: self.equal_button_press()).grid(row=4, column=2)

		self.button_sub = ttk.Button(root, text="-", command=lambda: self.math_button_press('-')).grid(row=4, column=3)

	def button_press(self, value):
		entry_val = self.number_entry.get()

		entry_val += value

		self.number_entry.delete(0, "end")

		self.number_entry.insert(0, entry_val)


	def isfloat(self, str_val):
		try:
			float(str_val)
			return True
		except ValueError:
			return False

	def math_button_press(self, value):
		if self.isfloat(str(self.number_entry.get())):
			self.div_trigger = False
			self.mult_trigger = False
			self.add_trigger = False
			self.sub_trigger = False

			self.calc_value = float(self.entry_value.get())

			if value=="/":
				self.div_trigger = True
			elif value=="+":
				self.add_trigger = True
			elif value=="-":
				self.sub_trigger = True
			elif value=="*":
				self.mult_trigger = True

			self.number_entry.delete(0, "end")

	def clear_button_press(self):
		self.number_entry.delete(0, "end")

	def equal_button_press(self):
		if self.add_trigger or self.mult_trigger or self.div_trigger or self.sub_trigger:

			if self.add_trigger:
				solution = self.calc_value + float(self.entry_value.get())
			elif self.sub_trigger:
				solution = self.calc_value - float(self.entry_value.get())
			elif self.div_trigger:
				solution = self.calc_value / float(self.entry_value.get())
			elif self.mult_trigger:
				solution = self.calc_value * float(self.entry_value.get())

			self.number_entry.delete(0, "end")
			self.number_entry.insert(0, solution)

	def __init__(self, root):
		self.entry_value = StringVar(root, value="")
		root.title("Calculator")
		root.geometry("480x220")
		root.resizable(width=False, height=False)

		style = ttk.Style()
		style.configure("TButton", font="Serif 15", padding=10)
		style.configure("TEntry", font="Serif 18", padding=10)

		self.number_entry = ttk.Entry(root, textvariable=self.entry_value, width=50)
		self.number_entry.grid(row=0, columnspan=4)

		self.first_row_of_buttons(root)
		self.second_row_of_buttons(root)
		self.third_row_of_buttons(root)
		self.forth_row_of_buttons(root)

if __name__ == '__main__':
	root = Tk()
	calc = Calculator(root)
	root.mainloop()