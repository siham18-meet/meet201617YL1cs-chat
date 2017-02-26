import turtle
from turtle_chat_client import Client 
from turtle_chat_widgets import Button , TextInput

class TextBox(TextInput): 
    def draw_box(self):
        turtle.penup()
        turtle.goto(self.pos)
        turtle.pendown()
        turtle.goto(self.width,0)
        turtle.goto(self.width,self.height)
        turtle.goto(0,self.height)
        turtle.goto(self.pos)
        turtle.mainloop()

    def write_msg(self):
        self.setup_listeners()
        print(self.new_msg)
        self.writer.goto(self.height-6,0)
        self.writer.write(self.new_msg)
        self.writer.clear(self)
        self.writer.write(self.new_msg)
        
x= TextBox()
        
      
   
   def draw_box(self):
        self.draw= turtle.clone()
        self.draw.penup()
        self.draw.goto(pos)
        self.draw.pendown()
        self.draw.goto(100,0)
        self.draw.goto(100,100)
        self.draw.goto(0,100)
        self.draw.goto(pos)
        self.draw.mainloop()
        self.draw.stamp()
        print("will it work?")



    def write_msg(self):
        self.setup_listeners()
        print(self.new_msg)
        self.writer.goto(self.height-6,0)
        self.writer.clear(self)
        self.writer.write(self.new_msg)
        
