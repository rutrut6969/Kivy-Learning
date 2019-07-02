import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup

class Widgets(Widget):
    pass

class P(FloatLayout):
    pass
    
#Builds the App
class MyApp(App):
    def build(self):
        return Widgets()


def show_popup():
    #Another instance of P()
    show = P()
    #Creates the size of the popup window
    popupwindow = Popup(title="popup Window", content=show, size_hint(None,None), size=(400,400))
    #Shows the window-
    popupwindow.open()

#Runs the App
if __name__ == "__main__":
    MyApp().run()