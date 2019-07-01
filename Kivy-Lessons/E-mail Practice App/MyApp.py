# Basically to import a widget you need to be able to know what widget you want, Then be able to import that widget EX:
# To import a label you need to call the label issued from the kivy module.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


#All the styling is done in a separate file, 
#calling the Widget function from Kivy 
#Allows us to pass this into another file without really 
#having to open it using python.
class MyGrid(Widget): #Using the MyGrid class in the .kv file with the tag <> will allow us to style this any way we want to.
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    def btn(self):
        print("Name:", self.name.text, "\nE-mail: ", self.email.text)
        self.name.text = ""
        self.email.text = ""


#Calls the grid class to build the application's 
#UI and piece it all together.
class MyApp(App):
    def build(self):
        return MyGrid()


#Calls the application to run, and function properly.
if __name__ == "__main__":
    MyApp().run()
