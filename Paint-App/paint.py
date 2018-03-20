from tkinter import *
import tkinter.font

class PaintApp:
	
	drawing_tool = "pencil"
	left_button = "up"

	x_position, y_position = None, None

	x1_line_pt, y1_line_pt, x2_line_pt, y2_line_pt = None, None, None, None 

	@staticmethod
	def quit_app(event=None):
		root.quit()

	def __init__(self, root):
		drawing_area = Canvas(root)
		drawing_area.pack()

		drawing_area.bind("<Motion>", self.motion) 
		drawing_area.bind("<ButtonPress-1>", self.left_button_down) 
		drawing_area.bind("<ButtonRelease-1>", self.left_button_up) 

		the_menu = Menu(root)

		file_menu = Menu(the_menu, tearoff=0)
		file_menu.add_command(label="Line", command=self.set_line_drawing_tool)
		file_menu.add_command(label="Pencil", command=self.set_pencil_drawing_tool)
		file_menu.add_command(label="ARC", command=self.set_arc_drawing_tool)
		file_menu.add_command(label="Rectangle", command=self.set_rectangle_drawing_tool)
		file_menu.add_command(label="Oval", command=self.set_oval_drawing_tool)
		file_menu.add_command(label="Text", command=self.set_text_drawing_tool)

		file_menu.add_separator()
		file_menu.add_command(label="Quit", command=self.quit_app)

		the_menu.add_cascade(label="Options", menu=file_menu)
		root.config(menu=the_menu)

	def set_line_drawing_tool(self):
		self.drawing_tool = "line"

	def set_pencil_drawing_tool(self):
		self.drawing_tool = "pencil"

	def set_arc_drawing_tool(self):
		self.drawing_tool = "arc"

	def set_rectangle_drawing_tool(self):
		self.drawing_tool = "rectangle"

	def set_oval_drawing_tool(self):
		self.drawing_tool = "oval"

	def set_text_drawing_tool(self):
		self.drawing_tool = "text"

	def left_button_down(self, event=None):
		self.left_button = "down"
		self.x1_line_pt = event.x
		self.y1_line_pt = event.y 


	def left_button_up(self, event=None):
		self.left_button = "up"
		self.x_position = None
		self.y_position = None

		self.x2_line_pt = event.x
		self.y2_line_pt = event.y 

		if self.drawing_tool=="line":
			self.line_draw(event)
		if self.drawing_tool=="pencil":
			self.pencil_draw(event)
		if self.drawing_tool=="arc":
			self.arc_draw(event)
		if self.drawing_tool=="oval":
			self.oval_draw(event)
		if self.drawing_tool=="rectangle":
			self.rect_draw(event)
		if self.drawing_tool=="text":
			self.text_draw(event)

	def motion(self, event=None):
		if self.drawing_tool=="pencil":
			self.pencil_draw(event)

		self.x_position = event.x
		self.y_position = event.y 

	def pencil_draw(self, event=None):
		if self.left_button =="down":
			if self.x_position is not None and self.y_position is not None:
				event.widget.create_line(self.x_position, self.y_position, event.x, event.y, smooth=True)


	def line_draw(self, event=None):
		if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
			event.widget.create_line(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt, smooth=True, fill="green")

	def arc_draw(self, event=None):
		if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
			coords = self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt

			event.widget.create_arc(coords, start=0, extent=150, style=ARC, fill="blue")

	def oval_draw(self, event=None):
		if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
			event.widget.create_oval(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt, fill="midnight blue", outline="yellow", width=2)

	def rect_draw(self, event=None):
		if  None not in (self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt):
			event.widget.create_rectangle(self.x1_line_pt, self.x2_line_pt, self.y1_line_pt, self.y2_line_pt, fill="red", outline="pink", width=2)

	def text_draw(self, event=None):
		if  None not in (self.x1_line_pt, self.y1_line_pt):
			text_font = tkinter.font.Font(family="Helvetica", size=20, weight="bold", slant="italic")
			event.widget.create_text(self.x1_line_pt, self.y1_line_pt, fill="lightblue", font=text_font, text="helloooo!")




root = Tk()
paint_app = PaintApp(root)
root.mainloop()