# configuration
from kivy.config import Config
Config.set("graphics", "width",  1100)
Config.set("graphics", "height", 700)

import os
os.environ["KIVY_NO_CONSOLELOG"] = "1"

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import matplotlib.pyplot as plt
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar
from kivy.core.text import Label as CoreLabel
from kivy.graphics import Color, Ellipse, Rectangle
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.graphics import Mesh
from functools import partial
from math import cos, sin, pi
from kivy.uix.image import Image
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

#==========================================

#==========================================
class MyLabel(Label):
    def on_size(self, *args):
        self.canvas.before.clear()
        with self.canvas.before:
            Color(0.93, 0.93, 0.93, 1)
            Rectangle(pos=self.pos, size=self.size)

class Display(FloatLayout):

    def __init__(self,**args):
        #Call grid layout constructor
        super().__init__(**args)

        # Set the timer for redrawing the screen
        refresh_time = 0.5
        Clock.schedule_interval(self.timer, refresh_time)
       
        
        
        #add a label
        self.label = MyLabel(
            text='Machine Coordinates:',
            color = (0,0,0,1),
            pos=(780, 620),
            size_hint=(0.2, 0.05))   
        self.add_widget(self.label)
        

        
##      # add input box
##        self.PX = TextInput(multiline=False,
##                            font_size=9.5,
##                            size_hint_y=None,
##                            height=25,
##                            size_hint_x=None,
##                            width=60,
##                            pos_hint={'x':0.8,'y':0.4})
##        self.add_widget(self.PX)
##        
##        self.PY = TextInput(multiline=False,
##                    font_size=9.5,
##                    size_hint_y=None,
##                    height=25,
##                    size_hint_x=None,
##                    width=60,
##                    pos_hint={'x':0.8,'y':0.5})
##        self.add_widget(self.PY)
##        
##        self.PZ = TextInput(multiline=False,
##                    font_size=9.5,
##                    size_hint_y=None,
##                    height=25,
##                    size_hint_x=None,
##                    width=60,
##                    pos_hint={'x':0.8,'y':0.6})
##        self.add_widget(self.PZ)
#---------------------  --------------------------
        self.plano = Button(size_hint_y=None,
                             height=350,
                             size_hint_x=None,
                             width=600,
                             pos_hint={'x':0.04,'y':0.44},
                             background_normal='C2.png',
                             background_down ='C2.png')
        #self.Y_UP.bind(on_press=self.press_Y_UP)
        self.add_widget(self.plano)


#--------------------- BOTONES --------------------------
#========================= RUN ======================
        self.run = Button(text = "RUN",
                     font_size=20,
                     size_hint_y=None,
                     height=40,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.04,'y':0.25},
                     color = (0,0,0,1),
                     background_color = (0.24,0.36,0.39,0.5))
        #self.run.bind(on_press=self.press_run)
        self.add_widget(self.run)
    #def press_run (self,instance):
#========================= STOP ======================
        self.stop = Button(text = "STOP",
                     font_size=20,
                     size_hint_y=None,
                     height=40,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.04,'y':0.10},
                     color = (0,0,0,1),
                     background_color = (0.24,0.36,0.39,0.5))
        #self.stop.bind(on_press=self.press_stop)
        self.add_widget(self.stop)
    #def press_stop (self,instance):
#========================= ZERO XY ======================
        self.Zeroxy = Button(text = "Zero XY",
                     font_size=20,
                     size_hint_y=None,
                     height=40,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.15,'y':0.25},
                     color = (0,0,0,1),
                     background_color = (0.24,0.36,0.39,0.5))
        #self.Zeroxy.bind(on_press=self.press_Zeroxy)
        self.add_widget(self.Zeroxy)
    #def press_Zeroxy (self,instance):
#========================= ZERO z ======================
        self.Zeroz = Button(text = "Zero Z",
                     font_size=20,
                     size_hint_y=None,
                     height=40,
                     size_hint_x=None,
                     width=100,
                     pos_hint={'x':0.15,'y':0.10},
                     color = (0,0,0,1),
                     background_color = (0.24,0.36,0.39,0.5))
        #self.Zeroz.bind(on_press=self.press_Zeroz)
        self.add_widget(self.Zeroz)
    #def press_Zeroz (self,instance):   
#========================= UP ===========================
        
        self.Y_UP = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.35,'y':0.25},
                             background_normal='up.png',
                             background_down ='up2.png')
        #self.Y_UP.bind(on_press=self.press_Y_UP)
        self.add_widget(self.Y_UP)
    #def press_Y_UP (self,instance):
        
        self.X_UP = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.40,'y':0.175},
                             background_normal='right.png',
                             background_down ='right2.png')
        #self.X_UP.bind(on_press=self.press_X_UP)
        self.add_widget(self.X_UP)
    #def press_X_UP (self,instance):
        
        self.Z_UP = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.48,'y':0.25},
                             background_normal='up.png',
                             background_down ='up2.png')
        #self.Z_UP.bind(on_press=self.press_Z_UP)
        self.add_widget(self.Z_UP)
    #def press_Z_UP (self,instance):

#========================= DOWN ===========================
        self.Y_DOWN  = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.35,'y':0.10},
                             background_normal='down.png',
                             background_down ='down2.png')
        #self.Y_DOWN.bind(on_press=self.press_Y_DOWN)
        self.add_widget(self.Y_DOWN)
    #def press_Y_DOWN (self,instance):
        
        self.X_DOWN = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.30,'y':0.175},
                             background_normal='left.png',
                             background_down ='left2.png')
        #self.X_DOWN.bind(on_press=self.press_X_DOWN)
        self.add_widget(self.X_DOWN)
    #def press_X_DOWN (self,instance):
        
        self.Z_DOWN = Button(size_hint_y=None,
                             height=50,
                             size_hint_x=None,
                             width=50,
                             pos_hint={'x':0.48,'y':0.10},
                             background_normal='down.png',
                             background_down ='down2.png')
        #self.Z_DOWN.bind(on_press=self.press_Z_DOWN)
        self.add_widget(self.Z_DOWN)
    #def press_Z_DOWN (self,instance):

#---------------------------------------------------------------


class CNC(App):


    def build(self):     
                
        Window.clearcolor= (0.98,0.98,0.98,0.5)
        return Display()
   
    


if __name__ == '__main__':
    
   # CNC().run()
    try:
        arduino = serial.Serial('COM7', 9600)
    except:
        print ("Failed to connect")
        exit()

    # Launch the app
    CNC().run()

    # Close serial communication
    arduino.close()

##time.sleep(2)
##rawString = arduino.readline()
##print(rawString)
##arduino.close()
