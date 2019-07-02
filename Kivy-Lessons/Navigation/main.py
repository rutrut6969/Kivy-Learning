import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class SecondWindow(Screen):
    pass

class WindowsManager(ScreenManager):
    pass

    



kv = Builder.load_file("main.kv")






#Building the app from the kv file.
class MainApp(App):
    def build(self):
        return kv


#Running application.
if __name__ == "__main__":
    MainApp().run()