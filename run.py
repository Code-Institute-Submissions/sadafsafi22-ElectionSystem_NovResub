import gspread
from google.oauth2.service_account import Credentials
import datetime
from collections import Counter

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
candidate_work_sheet = SHEET.worksheet('candidates')
vots_work_sheet  = SHEET.worksheet('vots')


def welcome_msg():
    print('\n \033[1m Welcome to Election Voting System! \033[0m \n')

def has_user():
    """"
    This function is the first function,
    it's allow users to select Login or registred
    Login is for those user which already regisrated
    """

    while True:
        has_user = input("1. Login \n2. Registration\n3. Show Results \nPlease Select one(1/2/3):")
        if(validate_data(has_user)):
            print("Data is valid!")
            has_user = int(has_user)
            if(has_user == 1):
                login()
                break
            elif(has_user == 2):
                registration()
                break
            elif(has_user == 3):
                show_results()
                break
            

def validate_data(data):
    try:
        if(int(data) not in [1,2,3]):
            raise ValueError(f'You can enter only (1/2/3), you entered {data}')
    except ValueError as e:
        print(f"Invalid data: {e}, Please try again.\n")
        return False

    return True

def login():
    """
    Request for user to enter NID and password, 
    after checking allow users to go voting section
    """
    print('Welcome to login section \n')
    NID = int(input("Please enter NID : \n"))
    password = input("please enter your Password : \n")
    NIDs = users.col_values(2)
    NIDs.remove('NID')
    NIDs = [int(num) for num in NIDs]
    passwords = users.col_values(4)

    while(not((NID in NIDs) and (password in passwords))):
        print(" Sorry NID and password incorrect please re-enter for Validation ")
        NID = int(input("Please enter your NID : \n"))
        password = input("Please enter your password : \n")
    
    print('login secceefully ')
    candidates_list()


def registration():
    """ 
    it's registration function, 
    system register users for voting, and checking for dublicate National ID(NID), and age should be older then 18
    """
    print("\n")
    print('Registration Form')
    print('You need the below information for registration \nName, National ID(NID), DOB(year), Password')
    
    user = []
    name = input('\nPlease enter your Name:\n')
    nid = int(input('Please enter your own National ID (NID):\n'))

    # checking for dubalicate NID, this system can not Accept dublicate NID
    saved_nids = users.col_values(2)
    saved_nids.remove('NID')
    int_saved_nids = [int(num) for num in saved_nids]
    # check for dublicate NID
    while(nid in int_saved_nids):
        print("\n")
        print('Sorry, This NID already registrated, we can not accept dublicate')
        nid = int(input('Please enter your own National ID (NID):\n'))
    
    dob = int(input('Please enter Year of your Birth:\n'))
    check_age(dob)
    password = input('Plase enter your Password:\n')
    user.append(name)
    user.append(nid)
    user.append(dob)
    user.append(password)
    users.append_row(user)
    print("\n")
    print("Registration has been successfuly done.\n")
    login()

def check_age(dob):
    """
    check if the age is older then 18  by using the year of born
    """
    year = datetime.date.today().year
    age = year - dob
    if(age <= 18 ):
        print(f"\nSorry, only above 18 years old  can vote.\n Your age is {age}")
        has_user()

def candidates_list():
    """
    Here we list Candidates which is retriveing condidate data from Excel sheet
    and allow users to select their mentioned Candidate
    using while for validation and user can select only Code of mentioned candidate 
    """
    candidate_code = candidate_work_sheet.col_values(1)
    candidate_name = candidate_work_sheet.col_values(2)

    print("\n")
    print(f'Please select {candidate_code}')
    for code, name in zip(candidate_code, candidate_name):
        print(f"Select {code} For {name}")

    selected_candidate = input('which one is your consider candidate? \n')
    # using while for validation,
    while(selected_candidate.upper() not in candidate_code):
        print('Please make sure you select Correctly:\n')
        selected_candidate = input('which one is your consider candidate? \n')
        
    new_vote = []
    # print(f'you select {selected_candidate}')
    new_vote.append(selected_candidate.upper())
    vots_work_sheet.append_row(new_vote)
    print("Your vote was successfully casted\n\n")

    has_user()
    
def vote_count(code):
    """
    count and display vote for every candidate
    """
    votes = vots_work_sheet.col_values(1)
    votes_counts = Counter(votes)
    print(f"Total vote for {code} is {votes_counts[code]}")

def show_results():
    """
    Display the result of voting after selected by user
    """
    candidate_code = candidate_work_sheet.col_values(1)
    for code in candidate_code:
        vote_count(code)

    # display total vote from voters
    print(f"Total Vote is {len(vots_work_sheet.col_values(1)) - 1}")

def main():
    welcome_msg()
    has_user()
main()
