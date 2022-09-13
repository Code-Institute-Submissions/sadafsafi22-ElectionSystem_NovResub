import gspread
from google.oauth2.service_account import Credentials
import datetime

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

C_PATH = Credentials.from_service_account_file('credential-file.json')
SCOPE_C_PATH = C_PATH.with_scopes(SCOPE)
GSPREND_CLIENT = gspread.authorize(SCOPE_C_PATH)
SHEET = GSPREND_CLIENT.open('ElectionSystem')

users = SHEET.worksheet('users')
data = users.get_all_values()
# print(data)
1

def welcome_msg():
    print('\n \033[1m Welcome to Election Voting System! \033[0m \n')

def has_user():
    """"
    This function is the first function,
    it's allow users to select Login or registred
    Login is for those user which already regisrated
    """

    while True:
        has_user = int(input("1. Login \n2. Registration \nPlease Select one(1/2):"))
        if(has_user == 1):
            login()
            break
        elif(has_user == 2):
            registration()
            break
        else:
            print("You can Select only 1/2")
            continue


def login():
    """
    Request for user to Enter NID and password, 
    after checking allow users to go voting section
    """
    print('Welcome to login section \n')
    NID = int(input("Please Enter NID : \n"))
    password = input("please Enter your Password : \n")
    NIDs = users.col_values(2)
    NIDs.remove('NID')
    NIDs = [int(num) for num in NIDs]
    passwords = users.col_values(4)
    # print(usernames,password)

    while(not((NID in NIDs) and (password in passwords))):
        print(" Sorry NID and password incorrect please re-enter for Validation ")
        NID = int(input("Please enter your NID : \n"))
        password = input("Please enter your password : \n")
    
    print('login secceefully ')


def registration():

    print('Registration Form')
    print('You need the below information for registration \nName, NID, DOB(year), Password')
    
    user = []
    name = input('Please Enter your Name:\n')
    nid = int(input('Please Enter your National ID (NID):\n'))
    # checking for dubalicate NID, this system can not Accept dublicate NID
    saved_nids = users.col_values(2)
    saved_nids.remove('NID')
    int_saved_nids = [int(num) for num in saved_nids]
    # check for dublicate NID
    while(nid in int_saved_nids):
        print('Sorry, This NID already registrated, we can not accept dublicate')
        nid = int(input('Please Enter your own National ID (NID):\n'))
    
    dob = int(input('Please Enter Year of your Birth:\n'))
    check_age(dob)
    password = input('Plase Enter your Password:\n')
    user.append(name)
    user.append(nid)
    user.append(dob)
    user.append(password)
    users.append_row(user)
    
    print(f"Registration has been successfuly done.")
    login()

    

def check_age(dob):
    """
    check if the age is older then 18  by using the year of born
    """
    year = datetime.date.today().year
    age = year - dob
    if(age <= 18 ):
        print(f"Sorry, only above 18 years old  can vote.\n Your age is {age}")
        has_user()


# welcome_msg()
# has_user()
registration()

