import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from database import DataBase
from kivy.lang import Builder

#This is the window that you create your account on:
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        #Adds user information to the data file
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)
                self.reset()
                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()
    #Sets the login screen
    def login(self):
        self.reset()
        sm.current = "login"
    #Resets the textboxes
    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""

class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)
    #Validates Information and logs the user in
    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()
    #Changes the screen to the create account screen
    def createBtn(self):
        self.reset()
        sm.current = "create"
    #Resets the login form on the login window
    def reset(self):
        self.email.text = ""
        self.password.text = ""

class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "E-mail: " + self.current
        self.created.text = "Created On: " + created

class WindowManager(ScreenManager):
    pass

def invalidLogin():
    pop = Popup(title="Invalid Login",
        content=Label(text='Invalid Username or Password.'),
        size_hint=(None,None), size=(400,400))

    
    
    pop.open()

def invalidForm():
    pop = Popup(title='Invalid Form',
                    content=Label(text='Please fill in all input with valid information.'),
                    size_hint=(None,None), size=(400,400))
    pop.open()
kv = Builder.load_file("login.kv")
sm = WindowManager()
db = DataBase("users.txt")
screens = [LoginWindow(name="login"), CreateAccountWindow(name="create"), MainWindow(name="main")]
for screen in screens:
    sm.add_widget(screen)

sm.current = "login"
class LoginApp(App):
    def build(self):
        return sm

if __name__ == "main":
    LoginApp().run()




