class chatbook:
    def __init__(self):
        self.username=''
        self.password=''
        self.loggedin=False
        self.Menu()

    def Menu(self):
        
        user_input=input("Welcome to Chatbook. \nHow would like to proceed? \n 1. Press 1 to SignUp. \n 2. press 2 to singin. \n 3. Press 3 to Write a post. \n 4.Press 4 to Meassage a Freind \n 5. Press any other key to exit. \n Please select Your choice : ")
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            pass
        elif user_input=='4':
            pass
        else:
            exit()
    
    def signup(self):
        email=input("Enter  Your Email Here : ")
        password=input("Create Your Password Here : ")
        self.username=email
        self.password=password
        print(" You Have Signed Up Sucessfully \n")
        self.Menu()

    def signin(self):
        if self.username=='' and self.password=='' :
            print("Please Sign Up First")
            self.signup()
        else:
            uname=input("ENter the mail or Username : ")
            pwd=input("Enter the Password : ")
            if self.username==uname and self.password==pwd:
                print("You have to logged in Sucessfully")
                self.loggedin=True
            else:
                print("Invalid Username or Password")


        
obj=chatbook()
