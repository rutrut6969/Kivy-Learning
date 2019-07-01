#Imports from Kivy
import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout

#Calling all the styling from the .kv file.
class MyApp(App):
    def build(self):
        return FloatLayout()

#Running the application.
if __name__ == "__main__":
    MyApp().run()