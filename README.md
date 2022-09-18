![Election System Logo](images/logo.JPG)

# Election System

Election System is my third portfolio project for code institute(Diploma of Full Stack Software Development.),  on this project we focuse on backend functionality with the Python.

This is an online system for voting, every person should register their name at first, after registration they can login to system and vote for their considered candidate. we using Google Sheet(one sheet for users, one for candidate and one for votes).

While users want to register their self, we need for Name, National ID(NID), DOB(year) and Password.
This system can accept only unique NID, and will not accept duplicate NID while registering, by using DOB(year) system will allow only those users which have more than 18 years old.

After registration complete, users can log in to system by using their NID and password. and system will display the candidate list which comes from Excel sheet (Candidate sheet), after choosing the considered candidate the vote going to save on google sheet (votes sheet), and display the success message.

 Link to the live site - [Election System](https://election-online-system.herokuapp.com/)

 **September 17, 2022**

![Election System main image](images/main-image.JPG)


## Contents

* [**Features**](<#features>)
* [**Login Option**](<#login-option>)
* [**Registration Option**](<#registration-option>)
* [**Voting Form**](<#voting-form>)
* [**Show Result**](<#show-result>)
* [**Back-end Code Explanation**](<#back-end-code-explanation>)
    * [**welcome_msg Function**](<#back-end-code-explanation>)
    * [**has_user function**](<#back-end-code-explanation>)
    * [**validate_data function**](<#back-end-code-explanation>)
    * [**login function**](<#back-end-code-explanation>)
    * [**registration function**](<#back-end-code-explanation>)
    * [**check-age function**](<#back-end-code-explanation>)
    * [**candidate-list fucntion**](<#back-end-code-explanation>)
    * [**vote_count function**](<#back-end-code-explanation>)
    * [**show_result function**](<#back-end-code-explanation>)
* [**Testing**](<#testing>)
    * [**Validator Tests**](<#validator-tests>)
    * [**Terminal Tests**](<#terminal-tests>)
* [**Technologies**](<#technologies>)
* [**Deployment**](<#deployment>)
* [**Credits**](<#credits>)
* [**Acknowledgements**](<#acknowledgements>)






## Features

As we know this is a backend program, and we have some functionality,
- First allows user to select one option
    - Login
    - Registration
    - Show Result

        ![Election System frist image](images/first-select.JPG)

## Login Option

If user already register their self and have account they can select login option and by using thier National ID (NID) and Password login to system

![Election System login image](images/login-image.JPG)

## Registration Option

If user want to register their self by this option they can do that,
for registration system need Name, National ID(NID), DOB(year) and Password. as shown in below image after selecting 2 for this option system move to regisration form and ask for their information.

 ![Election System register image](images/register-1.JPG)

* Name
    - Election System can accept everything(string and number) for name

    ![Election System register name  image](images/register-name.JPG)

* National ID (NID)
    - National ID has a unique number for everyone, and Election System can not accept duplicate cuz everyone can register their name, only and only a time and can vote for one time.

    ![Election System register national id image](images/register-nid.JPG)

    - if user enter dupicate NID system display " Sorry  , This 99262 NID already registrated, we can not accept duplicate" and ask for new NID and after accepting the new NID it will continue for next input

    ![Election System register national id image](images/register-nid2.JPG)

* DOB(year)
    - On this input we request form user to enter year of their birth, and we check for validation  if they user have more then 18 year old or not, if yes the form will continue for next input, if not the process end and display a msg like the image

    ![Election System register national id image](images/register-nid3.JPG)

* Password
    - The last input for registration is password and it will accept (alphabet and numbers with characters) for password. after entering this registration complete and display message and go for login form

    ![Election System register national id image](images/register-nid4.JPG)
    
## Voting Form
After Registering and login to system Successfully, The voting form will display automatically, and candidate list will be shown to user and allow them to select their considerate candidate. as shown in below image.

![Election System register national id image](images/voting.JPG)

- After selecting the candidate system will display a message and your vote is casted

    ![Election System register national id image](images/voting1.JPG)

## Show Result
Show result option, display the result for all votes, it will display number of vote for each candidate, show the percentage of votes for each candidate as will

![Election System register national id image](images/result.JPG)


## Back-end Code Explanation

This is a simple terminal python project, here i want to explain some of my code which written for this project. i'm using google sheet for storing data on excel file it's why import gspread, Credentials, importing datetime cuz i wnat to use date function to calculate age from year of born, importing Counter cuz wanna to display some arry count and importing title_art cuz on that file a create "Election System" with ASCII for the first time runing.

written some code to access the excel file from google sheet.
we have 3 sheets which are "users" , "candidate" , "votes" as showing in the image we access each sheet by their names.

## welcome_msg Function
Print out one art which come from title.py and simple welcome msg

![welcome_msg Function image](images/code1.JPG)

### has_user function
this is the first function which allow users to select login, register or show result 

![has_user function image](images/has_user.JPG)

### validate_data function
this validate function is using for valiate the entering data for has_user function

![validate_data function image](images/has_user1.JPG)

### login function
login function is using for requesting user to enter NID and Password and checking if correct or false.

![login function image](images/login-function.JPG)

### registration function
on this function users can register thier self at system

![registration function image](images/registration-function.JPG)

### check-age function
check-age function is user to check if the person who's registering have age more then 18 or not, if yes return true if not return false and display a message

![check-age function image](images/check-age.JPG)

### candidate-list fucntion
candidate-list function is getting list of candidate from excel sheet and display to user and after selecting the condiseret candidate save the result to Excel sheet

![check-age function image](images/candidate-list.JPG)

### vote_count function
this function get all votes from excel sheet and count them for each candidate and display for user while selecting Show Result from menu 

![check-age function image](images/vote_count.JPG)

### show_result function
show result function is going to display result of votes and precentage of votes for each candidate

![check-age function image](images/show_result.JPG)


## Testing
The Election has been tested extensively for bugs and errors throughout the development process.

### Validator Tests
Python project code has been passed through the [PEP8 online python validator tester](http://pep8online.com/). No errors were shown.

![Election System register national id image](images/testing.JPG)

### Terminal Tests
Election System Project has been tested with Gitpod terminal text editor and working well with no errors and bugs

![Election System register national id image](images/testing1.JPG)



## Technologies
* [Python](https://www.python.org/) - Python is a programming langauge using for this project.
* [Heroku](https://www.heroku.com) - Heroku is a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
* [GitPod](https://gitpod.io/) - An open source developer platform for remote development. Used to edit and build the program.
* [GitHub](https://github.com/) - An online host for web and software development projects. Used to store the repository. Linked to Heroku for automatic deployement with new commits.
* [Git](https://git-scm.com/) - Software for tracking changes to files. Used with GitPod to add, commit and push code changes to the repository on GitHub. 
* [patorjk](http://patorjk.com/) - A simple app used to Create text art from words, im using this for create the Election system on first time
* [dia](http://dia-installer.de/) - Dia is free (open source) drawing software. Sketch your favorite structured diagrams! Windows version available as a free download.
* [Google sheet](https://www.google.com/sheets/about/) - Use Google Sheets to create and edit online spreadsheets. Get insights together with secure sharing in real-time and from any device


## Deployment
Project Deployment with Heroku
Here is some steps for delopy Election System via Heroku.

1. Listing all requirement on requirements.txt by using below commend
```bash
pip3 freeze > requirements.txt
``` 
2. Add, commit and push new changes to GitHub.
3. Go [Heroku](https://www.heroku.com) on the browser and create an account and login.
4. Once the account is create/open , go to "New" and look for "Create new app"
5. Type an App Name(which should be unique on Heroku) and select the local region from dropdown box.
6. After create App the dashborad will display click on "Setting" tab in the menubar. Scroll down and add "Config Vars" any Sensitive information which not sent to github.
7. For projects using the Code Institute terminal, another Config Var needs to be added into this section. Enter "PORT" in all capitals into the "Key" field and "8000" into the "Value" field and click the "Add" button.
8. for using python project "Buildpacks" section click "Add buildpack" and select python and node.js
9. On the top of the page select Delopy from menu
10. on Delopy page scroll down to the "Deployment method" section click and select "GitHub" option to connect Heroku to the repository on GitHub. Click "Connect to GitHub", login to Github in the pop-up window if required, otherwise this should be done automatically.
11. In the 'connect to GitHub' section enter the repository name which your mentioned project exist on GitHub
12. If the last step was successful the "Deploy" page should change. Scroll down the page to the "Automatic deploys" and "Manual deploy" sections. To enable automatic deploys with each new GitHub push click the "Enable Automatic Deploys" button. To manually deploy click the "Deploy branch" button in the "Manual deploy" section. Ensure the "main"/"master" branch is selected from the drop down menus for both of these options if that is the latest branch of the project.
13. If deployment is successful a prompt should appear with a "View" button to view the deployed app. Click the button to view the app deployment.

Your site is published at [Election System](https://election-online-system.herokuapp.com/)

## Credits
- Content 
    - The Election System Project developed all by developer. 
- Media
    - The Election System ASCII work-art title in a font called ANSI shadow from [patorjk](http://patorjk.com/)

## Acknowledgements
- My Mentor for constant feedback.
- My Husband Walid Ahmadyar for inspiration, support and useful comments
    