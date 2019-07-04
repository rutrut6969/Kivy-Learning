import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from database import DataBase

#Where the user creates their account. 
class CreateAcc(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    loginf = ObjectProperty(None)
    create = ObjectProperty(None)

    pass

#Where the user logs in at.
class Login(Screen):
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    createf = ObjectProperty(None)
    login = ObjectProperty(None)

    pass

#Profile Page
class Profile(Screen):
    pass

#Manages all the windows
class WindowManager(ScreenManager):
    pass

#Global Variables to utilize
kv = Builder.load_file("prog.kv")
db = DataBase("users.txt")
wm = WindowManager()
screens = [CreateAcc(name="create"), Login(name="login"), Profile(name="profile")]
#Generates Screens
for screen in screens:
    wm.add_widget(Screen)

wm.current = "login"
class ProgressionApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ProgressionApp().run()
