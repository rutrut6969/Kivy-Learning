import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols = 4 #Adds the number of columns in the program, I'm sure there's one for rows aswell

        self.add_widget(Label(text="First Name: ")) #This adds a label widget from the kivy module
        self.name = TextInput(multiline=False) #This assigns a widget value to this
        self.add_widget(self.name) #This utilizes that widget value

        self.add_widget(Label(text="Last Name: ")) #Label
        self.Lname = TextInput(multiline=False) #TextBox for input
        self.add_widget(self.Lname) #Puts the textbox on the screen

        self.add_widget(Label(text="E-mail:  ")) #Label
        self.email = TextInput(multiline=False) #Text
        self.add_widget(self.email) #Shows Textbox




class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    MyApp().run()


