class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.Menu()

    def Menu(self):
        
        user_input=input("Welcome to Chatbook. \nHow would like to proceed? \n 1. Press 1 to SignUp. \n 2. press 2 to singin. \n 3. Press 3 to Write a post. \n 4.Press 4 to Meassage a Freind \n 5. Press any other key to exit")
        if user_input=='1':
            pass
        elif user_input=='2':
            pass
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()

obj=chatbook()
