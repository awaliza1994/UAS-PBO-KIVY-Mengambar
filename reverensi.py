from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.properties import ListProperty
from kivy.uix.screenmanager.RiseInTransition import RiseInTransition

class ScreenCircle (Screen):
    pass
class ScreenSquare (Screen):
    pass
class ScreenColor (Screen):
    pass
class reverensi(ScreenManager):
    selected_color = ListProperty([1,0,0,1])

class reverensiapp(App):
    def build(self):
        return reverensi()   
if __name__=='__main__':
    reverensiapp().run()
