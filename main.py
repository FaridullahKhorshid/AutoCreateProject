import os
from github import Github
from getpass import getpass

# Eerste versie eindopdracht
# in this project i manged to automate the whole process of creating a project
# and used github to get some data from github, for example al repos from your github account
# with this code you can create an project with a local dir and a github repo, and yor repo list
# module PyGithub is required, if don't install PyGithub you cant use github

iNumberOfHeart = 30


class MyGithub:
    def __init__(self):
        self.my_github = False

        github_user_name = input('Your Github username? ')
        github_password = getpass('Your Github Password? ')

        try:
            github = Github(github_user_name, github_password)
            if github.get_user().login:
                self.my_github = github
        except:
            print('')
            print(f'Wrong password or username! Please tray again! ')

    def create_project(self):
        project_name = input('Your project name? ')
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


# get standard choices for the user
def get_choice():
    print('')
    print(iNumberOfHeart * '❤')
    print(f'Welcome {oGithub.my_github.get_user().name} what can i do for you? ')
    print(iNumberOfHeart * '❤')
    print('')

    choices = [
        '1: Create automatic project! ',
        '2: Get my repo list!',
        '3: Login with another account! ',
        '4: Logout! ',
    ]

    for choice in choices:
        print(choice)

    return input('Choose a number: ')


oGithub = MyGithub()
while not oGithub.my_github:
    oGithub = MyGithub()
else:
    iChoice = int(get_choice())

    if iChoice == 1:
        oGithub.create_project()
    elif iChoice == 2:
        oGithub.get_repo_list()
    elif iChoice == 3:
        print(iNumberOfHeart * '❤')
        print('You can now log in with another account! ')
        print(iNumberOfHeart * '❤')
        oGithub = MyGithub()
    elif iChoice == 4:
        print(iNumberOfHeart * '❤')
        print('You are now logged out, please login again! ')
        print(iNumberOfHeart * '❤')
        oGithub = MyGithub()
    else:
        print('')
        print(f'The choice {iChoice} is not supported!')
        iChoice = int(get_choice())