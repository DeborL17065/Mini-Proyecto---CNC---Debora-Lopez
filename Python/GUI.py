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
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
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

class Display(FloatLayout):

    def __init__(self,**args):
        #Call grid layout constructor
        super().__init__(**args)
        
        #add a label
        self.add_widget(Label(text="X: ",
                              font_size=25,
                              size_hint_y=None,
                              height=50,
                              size_hint_x=None,
                              width=100,
                              pos_hint={'x':0.1,'y':0.55}))
        # add input box
        self.PX = TextInput(multiline=False,
                            font_size=25,
                            size_hint_y=None,
                            height=50,
                            size_hint_x=None,
                            width=100,
                            pos_hint={'x':0.2,'y':0.55})
        self.add_widget(self.PX)
        
        self.submit = Button(text = "Submit",
                             font_size=25,
                             size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=100,
                             pos_hint={'x':0.1,'y':0.85})
        #self.submit.bind(on_press=self.press)
        self.add_widget(self.submit )
    #def press (self,instance):
        


class CNC(App):
    def build(self):
        return Display()


if __name__ == '__main__':
    CNC().run()
    
##time.sleep(2)
##rawString = arduino.readline()
##print(rawString)
##arduino.close()
