import datetime

#Creates database information
class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()
#Loads user info
    def load(self):
        self.file = open(self.filename, "r")
        self.users = {}

        for line in self.file:
            email, password, name, created = line.strip().split(";")
            self.users[email] = (password, name, created)

        self.file.close()
#Get the users information
    def get_user(self, email):
        if email in self.users:
            return self.users[email]

        else:
            return -1
#Creates New Profile
    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1

        else:
            print("Email exists already")
            return -1
#Validates to make sure the user is there or not
    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False
    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n")
#Gets the date and time of the profile creation

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split (" ")[0]
