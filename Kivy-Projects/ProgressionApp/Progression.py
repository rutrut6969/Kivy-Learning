import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivy.properties import ObjectProperty

class CreateAcc(Screen):
    username = ObjectProperty(None)
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    loginf = ObjectProperty(None)
    create = ObjectProperty(None)

    pass

class Login(Screen):
    email = ObjectProperty(None)
    passw = ObjectProperty(None)
    createf = ObjectProperty(None)
    login = ObjectProperty(None)

    pass

class Profile(Screen):
    pass


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("prog.kv")

class ProgressionApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    ProgressionApp().run()
