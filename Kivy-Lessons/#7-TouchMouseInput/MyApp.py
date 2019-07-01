import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
#Defines the Touch mechanic for touch screens:
class Touch(Widget):
     btn = ObjectProperty(None)
     #The parameter touch is not the same as the class name.
     def on_touch_down(self, touch):
         print("Mouse Down", touch)
         self.btn.opacity = 0.5

     def on_touch_move(self, touch):
         print("Mouse Move", touch)
    
     def on_touch_up(self, touch):
         print("Mouse Up", touch)
         self.btn.opacity = 1

#Builds the UI for the App
class MyApp(App):
    def build(self):
        return Touch() #Don't forget to use brackets where they're needed. 


#Runs the app:
if __name__ == "__main__":
     MyApp().run()
