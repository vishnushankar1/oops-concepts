class chatbook:
    __user_id=0
    def __init__(self):
        self.__name="Default User"
        self.id = chatbook.__user_id
        chatbook.__user_id += 1
        self.username=''
        self.password=''
        self.loggedin=False
        #self.Menu()

    def Menu(self):
        
        user_input=input("Welcome to Chatbook. \nHow would like to proceed? \n 1. Press 1 to SignUp. \n 2. press 2 to singin. \n 3. Press 3 to Write a post. \n 4.Press 4 to Meassage a Freind \n 5. Press any other key to exit. \n Please select Your choice : ")
        if user_input=='1':
            self.signup()
        elif user_input=='2':
            self.signin()
        elif user_input=='3':
            self.post()
        elif user_input=='4':
            self.send_msg()
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
        self.Menu()
    
    def post(self):
        if self.loggedin==True:
            txt= input("Please Enter your Msg Here that you want to post : ")
            print(f"Your post has been posted : {txt}")
        else:
            print("You have not logged in, Please login first to post a MSg.")

        self.Menu()

    def send_msg(self):
        if self.loggedin==True:
            txt =input("Please enter the msg that you want to send : ")
            frnd = input("please Mention the frnd the name whom you want to sned")
            print(f"Your msg has been sent to {frnd}")
        else:
            print("You have not logged in, Please login first to send a msg.")
        self.Menu()

    def get_name(self):
        return self.__name
    def set_name(self):
        self.__name=input("Enter your name : ")
    @staticmethod
    def get_id():
        return chatbook.__user_id
    @staticmethod
    def set_id(val):
        chatbook.__user_id=val
        
obj=chatbook()
print(obj.id)
#using static method directly from class rather than class
chatbook.set_id(10)
print(chatbook.get_id())
obj1=chatbook()
print(obj1.id)
obj2=chatbook()
print(obj2.id)
#getter and Setter Methods
print(obj.get_name())
print(obj.set_name())
print(obj.get_name())