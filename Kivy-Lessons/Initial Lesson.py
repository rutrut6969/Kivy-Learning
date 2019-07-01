import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyApp(App):
    def build(self):
        return Label(text="Isaac's App")

if __name__ == "__main__":
    MyApp().run()