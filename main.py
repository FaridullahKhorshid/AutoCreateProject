import os
from github import Github
from getpass import getpass

# Eerste versie eindopdracht || ik moest even weer ombowen wegens verandering in github https://developer.github.com/changes/2020-02-14-deprecating-password-auth/
# in this project i manged to automate the whole process of creating a project
# and used github to get some data from github, for example al repos from your github account
# with this code you can create an project with a local dir and a github repo, and yor repo list
# module PyGithub is required, if don't install PyGithub you cant use github
# here you can get you are github access token: https://github.com/settings/tokens

NUMBER_OF_HEART = 30


class MyGithub:
    def __init__(self, access_token):
        self.my_github = False

        try:

            github = Github(access_token)
            if github.get_user().login:
                self.my_github = github
                f = open("env.txt", "a")
                f.truncate(0)
                f.write(access_token)
                f.close()
        except:
            print('')
            print(f'Wrong github token! Please tray again! ')

    def create_project(self, project_name):

        path = 'C:\\Projects'

        if not os.path.isdir(path):
            os.mkdir(path)

        dir_name = path + '/' + project_name
        user = self.my_github.get_user()
        login = user.login
        new_repo = user.create_repo(project_name)

        commands = [
            f'echo "#Initial {new_repo.name}" >> README.md',
            'git init',
            f'git remote add origin https://github.com/{login}/{project_name}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git push -u origin master',
        ]

        os.mkdir(dir_name)
        os.chdir(dir_name)

        for command in commands:
            os.system(command)

        print(f'{project_name} project created successfully!')
        os.system('code .')

    def get_repo_list(self):
        user = self.my_github.get_user()
        print('')
        for repo in user.get_repos():
            print(repo.name)

    def logout(self):
        self.my_github = False
        f = open("env.txt", "a")
        f.truncate(0)
        f.close()

        print('You are now logged out, please restart the program to login again! ')

        return False


# get standard choices for the user
def get_choice():
    print('')
    print(NUMBER_OF_HEART * '❤')
    print(f'Welcome {oGithub.my_github.get_user().name} what can i do for you? ')

    choices = [
        '1: Create automatic project! ',
        '2: Get my repo list!',
        '3: Close program! ',
        '4: Logout! ',
    ]

    for choice in choices:
        print(choice)

    return input('Choose a number: ')


oGithub = False
active = True
while active:
    if not oGithub:
        key = ''
        if os.path.isfile('env.txt'):
            file_read = open("env.txt", "r")
            key = file_read.read()
            file_read.close()

        if key == '':
            key = getpass('Your Github access token? ')

        oGithub = MyGithub(key)

    if oGithub.my_github:
        iChoice = int(get_choice())

        if iChoice == 1:
            project_name_from_input = input('Your project name? ')
            oGithub.create_project(project_name_from_input)

        elif iChoice == 2:
            oGithub.get_repo_list()

        elif iChoice == 3:
            active = False
            oGithub = False
        elif iChoice == 4:
            print(NUMBER_OF_HEART * '❤')
            logout = input('Are you sure you want to logout? your github access token wil be removed! y/n: ')
            logout = logout.lower()

            if logout == 'y':
                active = False
                oGithub = oGithub.logout()

        else:
            print(f'The choice {iChoice} is not supported!')
    else:
        oGithub = False
