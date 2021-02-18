# configuration
from kivy.config import Config
Config.set("graphics", "width",  1100)
Config.set("graphics", "height", 700)

import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
from kivy.lang import Builder
from kivy.graphics import Mesh
from functools import partial
from math import cos, sin, pi
import serial, time
#--------------------------------------
# Comunicacion serial
#arduino = serial.Serial('COM4', 9600)

#---------------------------------------

##Builder.load_string("""
##<MyGridLayout>:
####    Y_UP = Y_UP
####    X_UP = X_UP
####    Z_UP = Z_UP
####    Y_DOWN = Y_DOWN
####    X_DOWN = X_DOWN
####    Z_DOWN = Z_DOWN
##    
##    GridLayout:
##        cols:1
####        size: root.width, root.heigth
###        padding: 50
###        spacing:20
##        Button: 
##            text:"Submt"
##            font_size:32
##            size_hint_y:None
##            height:50
##            size_hint_x:None
##            width:100
##            on_press:root.press()
##            
##
##    
##
##""")

class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0, 1, 0, 0.25)
            Rectangle(pos=self.pos, size=self.size)

class Display(FloatLayout):

    def __init__(self,**args):
        #Call grid layout constructor
        super().__init__(**args)
        
##        #add a label
        self.rect = Rectangle(size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=100,
                              pos_hint={'x':0.15,'y':0.60},
                              color = (1,0.49,0.31,1))
        
        self.add_widget(Label(text="CNC Status",
                              font_size=25,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=100,
                              pos_hint={'x':0.05,'y':0.90}))
       
##        
##        self.add_widget(Label(text="X: ",
##                              font_size=20,
##                              size_hint_y=None,
##                              height=50,
##                              size_hint_x=None,
##                              width=100,
##                              pos_hint={'x':0.005,'y':0.85}))
##        # add input box
        self.PX = TextInput(multiline=False,
                            font_size=25,
                            size_hint_y=None,
                            height=25,
                            size_hint_x=None,
                            width=50,
                            pos_hint={'x':0.08,'y':0.865})
        self.add_widget(self.PX)

#--------------------- BOTONES --------------------------
#========================= UP ===========================
        
        self.Y_UP = Button(text = "Y+",
                             font_size=25,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=100,
                             pos_hint={'x':0.10,'y':0.45},
                             color = (0,1,0,1),bold= True,
                             outline_color=(0,0,0,1),
                             outline_width=2)
        #self.Y_UP.bind(on_press=self.press_Y_UP)
        self.add_widget(self.Y_UP)
    #def press_Y_UP (self,instance):
        
        self.X_UP = Button(text = "X+",
                             font_size=25,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=100,
                             pos_hint={'x':0.15,'y':0.35},
                             background_color = (1,0.49,0.31,1))
        #self.X_UP.bind(on_press=self.press_X_UP)
        self.add_widget(self.X_UP)
    #def press_X_UP (self,instance):
        
        self.Z_UP = Button(text = "Z+",
                     font_size=25,
                     size_hint_y=None,
                     height=50,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.26,'y':0.45},
                     color = (0,1,0,1),bold= True,
                     outline_color=(0,0,0,1),
                     outline_width=2)
        #self.Z_UP.bind(on_press=self.press_Z_UP)
        self.add_widget(self.Z_UP)
    #def press_Z_UP (self,instance):

#========================= DOWN ===========================
        self.Y_DOWN  = Button(text = "Y-",
                     font_size=25,
                     size_hint_y=None,
                     height=50,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.10,'y':0.25},
                     color = (0,1,0,1),bold= True,
                     outline_color=(0,0,0,1),
                     outline_width=2)
        #self.Y_DOWN.bind(on_press=self.press_Y_DOWN)
        self.add_widget(self.Y_DOWN)
    #def press_Y_DOWN (self,instance):
        
        self.X_DOWN = Button(text = "X-",
                             font_size=25,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=100,
                             pos_hint={'x':0.05,'y':0.35},
                             background_color = (1,0.49,0.31,1))
        #self.X_DOWN.bind(on_press=self.press_X_DOWN)
        self.add_widget(self.X_DOWN)
    #def press_X_DOWN (self,instance):
        
        self.Z_DOWN = Button(text = "Z-",
                     font_size=25,
                     size_hint_y=None,
                     height=50,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.26,'y':0.25},
                     color = (0,1,0,1),bold= True,
                     outline_color=(0,0,0,1),
                     outline_width=2)
        #self.Z_DOWN.bind(on_press=self.press_Z_DOWN)
        self.add_widget(self.Z_DOWN)
    #def press_Z_DOWN (self,instance):

#---------------------------------------------------------------


class CNC(App):
    def build(self):
        Window.clearcolor= (0,0,0,1)
        return Display()


if __name__ == '__main__':
    CNC().run()
    
##time.sleep(2)
##rawString = arduino.readline()
##print(rawString)
##arduino.close()
