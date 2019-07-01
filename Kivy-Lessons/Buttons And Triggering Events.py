# Basically to import a widget you need to be able to know what widget you want, Then be able to import that widget EX:
# To import a label you need to call the label issued from the kivy module.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # Adds the number of columns in the program, I'm sure there's one for rows aswell
        self.cols = 1

    #Inner Grid
        # This will allow us to move everything from the outer grid to the inner grid
        self.inside = GridLayout()
        # Sets the number of columns in the inner grid
        self.inside.cols = 2 

         
    #Label First Name
        # This adds a label widget from the kivy module
        self.inside.add_widget(Label(text="First Name: "))
        # This assigns a widget value to this
        self.name = TextInput(multiline=False)
        # This utilizes that widget value
        self.inside.add_widget(self.name)  

    # Label Last Name
        self.inside.add_widget(Label(text="Last Name: ")) 
        # TextBox for input
        self.Lname = TextInput(multiline=False)  
        # Puts the textbox on the screen
        self.inside.add_widget(self.Lname) 

    # Label E-Mail
        self.inside.add_widget(Label(text="E-mail:  "))  
        # Text
        self.email = TextInput(multiline=False)
        # Shows Textbox
        self.inside.add_widget(self.email)  

    #Inner Grid
        # This puts the inner grid into action, putting everything that has the .inside tag into the inner grid.
        self.add_widget(self.inside) 

    #Submit Button
        # This adds a button widget to the form, allowins us to utilize a submit function
        self.submit = Button(text="Confirm", font_size=25)

        self.submit.bind(on_press=self.press)
         # Shows the button on the form
        self.add_widget(self.submit)
    
    def press(self, Instance):
        #Assigns the variable to each of the textboxes to retrieve the information we need.
        name = self.name.text
        last = self.Lname.text
        email = self.email.text

        #Prints out the information we like to collect. 
        print("Name: \n" + name + " \nLast Name: \n" + last + " \nE-mail: \n" + email)
        
        #Clears the textboxes to be blank for next entry.
        self.name.text = ""
        self.Lname.text = ""
        self.email.text = ""





#Calls the grid class to build the application's UI and piece it all together.
class MyApp(App):
    def build(self):
        return MyGrid()


#Calls the application to run, and function properly. 
if __name__ == "__main__":
    MyApp().run()
