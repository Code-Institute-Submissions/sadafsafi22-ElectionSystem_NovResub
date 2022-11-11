"""
this is a simple program for election system
for my project at codeinstitute
"""
import gspread
from google.oauth2.service_account import Credentials
import datetime
from collections import Counter
from title import title_art

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CANDIDATE_LIST = {
    'A': 'Donald Trump',
    'B': 'Joe Biden',
    'C': 'Howie Hawkins',
    'D': 'Jo Jordensen'
}

C_PATH = Credentials.from_service_account_file('credential-file.json')
SCOPE_C_PATH = C_PATH.with_scopes(SCOPE)
GSPREND_CLIENT = gspread.authorize(SCOPE_C_PATH)
SHEET = GSPREND_CLIENT.open('ElectionSystem')

users = SHEET.worksheet('users')
candidate_work_sheet = SHEET.worksheet('candidates')
vots_work_sheet = SHEET.worksheet('vots')


def welcome_msg():
    print('\033[95m'+title_art)
    print('\n \033[1m \033[94m Welcome to Election Voting System! \033[0m \n')


def has_user():
    """"
    This function is the first function,
    it's allow users to select Login or registred
    Login is for those user which already regisrated
    """
    while True:
        has_user = input('''1. Login\n2. Registration
3. Show Results\nPlease Select one(1/2/3):''').strip()
        if (validate_data(has_user)):
            print('\033[92m Data is valid! \033[0m')
            has_user = int(has_user)
            if (has_user == 1):
                login()
                break
            elif (has_user == 2):
                registration()
                break
            elif (has_user == 3):
                show_results()
                break


def validate_data(data):
    try:
        if len(data) < 1:
            raise ValueError('System cannot accept white space')
        elif (int(data) not in [1, 2, 3]):
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
    print('\033[94m \033[1m \nWelcome to login section\n \033[0m')

    NIDs = users.col_values(2)
    NIDs.remove('NID')
    NIDs = [int(num) for num in NIDs]
    passwords = users.col_values(4)

    while True:
        NID = ""
        while True:
            print('\033[93m You can go back by typing Back \033[0m')
            NID = input("Please enter NID : \n").strip()
            back_function(NID)
            if len(NID) > 1 and NID.isdigit():
                break
            else:
                print('''\033[91m Please enter a valid number\n \033[0m''')

        password = ""
        while True:
            password = input("please enter your Password : \n").strip()
            back_function(password)
            if len(password) > 1:
                break
            else:
                print('''\033[91m \nPlease enter password 
                correctly \033[0m \n''')

        NID = int(NID)
        if (not ((NID in NIDs) and (password in passwords))):
            print('''Sorry details entered are incorrect
please re-enter for Validation''')
        else:
            break

    print('\n \033[94m \033[1m login secceefully \033[0m')
    candidates_list()


def registration():
    """
    it's registration function,
    system register users for voting,
    and checking for duplicate National ID(NID),
    and age should be older then 18
    """
    print("\n")
    print('\n  \033[1m Registration Form \033[0m \n')
    print('''You need the below information for registration
    \nName, National ID(NID), DOB(year), Password''')

    user = []
    print('\033[93m You can go back by typing Back \033[0m')
    while True:
        name = input('\nPlease enter your Name:\n').strip()
        back_function(name)
        if (len(name) > 0 and name.isalpha()):
            break
        else:
            print('\033[91m Please Enter a valid Name \033[0m')

    while True:
        nid = input('Please enter your own National ID (NID):\n').strip()
        back_function(nid)
        if nid.isdigit():
            nid = int(nid)
            # checking for dubalicate NID, this system 
            # can not Accept duplicate NID
            saved_nids = users.col_values(2)
            saved_nids.remove('NID')
            int_saved_nids = [int(num) for num in saved_nids]
            # check for dublicate NID
            if (nid in int_saved_nids):
                print(f'''\033[91m  Sorry,
This {nid} NID already registrated,
we can not accept duplicate \033[0m''')
            else:
                break
        else:
            print('\033[91m Please Enter a valid NID Number \033[0m')
            print('\033[91m only digits can be accept \033[0m')
            continue
        
    while True:
        dob = input('Please enter Year of your Birth:\n').strip()
        back_function(dob)
        if dob.isdigit():
            check_age(int(dob))
            break
        else:
            print('\033[91m Please Enter a valid Year \033[0m')
            print('\033[91m only digits can be accept \033[0m')
            continue

    while True:
        password = input('Plase enter your Password:\n').strip()
        if (len(password) <= 0):
            print('\033[91m Please Enter a valid Password\033[0m')
            print('\033[91m only space can\'t be accept \033[0m')
        else:
            break

    back_function(password)
    user.append(name)
    user.append(nid)
    user.append(dob)
    user.append(password)
    users.append_row(user)
    print("\n \033[1m Registration has been successfuly done. \033[0m \n")
    login()


def check_age(dob):
    """
    check if the age is older then 18  by using the year of born
    """
    year = datetime.date.today().year
    age = year - dob
    if (age <= 18):
        print(f"""\nSorry, only above 18 years old  can vote.\n
        Your age is {age}\n\n""")
        has_user()


def candidates_list():
    """
    Here we list Candidates which is retriveing condidate data from Excel sheet
    and allow users to select their mentioned Candidate
    using while for validation and user can
    select only Code of mentioned candidate
    """
    candidate_code = candidate_work_sheet.col_values(1)
    candidate_name = candidate_work_sheet.col_values(2)
    while True:
        print(f'Please select {candidate_code}')
        for code, name in zip(candidate_code, candidate_name):
            print(f"Select {code} For {name}")

        selected_candidate = input('''\n which one is your consider 
candidate? \n''').strip()
        if (len(selected_candidate) > 0):
            back_function(selected_candidate)
            # using while for validation,
            if (selected_candidate.upper() not in candidate_code):
                print(''' \033[91m Please make sure you select Correctly: 
you have to select one of above candidate \033[0m ''')
            else:
                new_vote = []
                # print(f'you select {selected_candidate}')
                new_vote.append(selected_candidate.upper())
                vots_work_sheet.append_row(new_vote)
                print("Your vote was successfully casted\n\n")

                has_user()

                break
        else:
            print(''' \033[91m Worrying, 
space is not accepeted.  \033[0m ''')
            continue


def vote_count(code):
    """
    count and display vote for every candidate
    """
    votes = vots_work_sheet.col_values(1)
    votes_counts = Counter(votes)
    candidate_name = CANDIDATE_LIST[code]
    vote_count = votes_counts[code]
    vote_percentage = round(((votes_counts[code]) * 100) / (len(votes) - 1), 2)
    print(f"""Total vote for """'\033[94m'f"""{candidate_name}"""'\033[0m'f""" 
    is {vote_count} """'\033[91m'f"""({ vote_percentage } %)"""'\033[0m')


def show_results():
    """
    Display the result of voting after selected by user
    """
    candidate_code = candidate_work_sheet.col_values(1)
    for code in candidate_code:
        vote_count(code)

    # display total vote from voters
    print(f"Total Vote is {len(vots_work_sheet.col_values(1)) - 1}\n")
    has_user()


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def back_function(data):
    data = data.lower()
    if (data in ['back', 'exit', 'close']):
        print('\n')
        has_user()


def main():
    welcome_msg()
    has_user()


# main()

has_user()