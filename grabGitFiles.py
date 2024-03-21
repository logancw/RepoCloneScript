import os
import requests
from dotenv import load_dotenv
from git import Repo 


# Load .env 
load_dotenv();

# GitHub API Token & Username
token = os.getenv('GITHUB_API_TOKEN'); 
username = os.getenv('GITHUB_USERNAME'); 

userSelection = input('Enter the name of the repo you want to clone: **TYPE ALL TO CLONE ALL REPOS**\n')

   

headers = {'Authorization': f'token {token}'}
url = f'https://api.github.com/users/{username}/repos'
Surl = f'https://api.github.com/repos/{username}/{userSelection}'

#GET Requests
response = requests.get(url,headers=headers)
response1 = requests.get(Surl,headers=headers)


if userSelection == 'ALL':
    if response.status_code == 200:
        repos = response.json()
        for repo in repos:
            print(repo['name'])
            # Clone the repo
            Repo.clone_from(repo['clone_url'], f'./repos/{repo['name']}')
    else:
        print('Failed to fetch repos')
else:
    if response1.status_code == 200:
        repo1 = response1.json()
        print(f'Cloning {repo1['name']}')
        Repo.clone_from(repo1['clone_url'], f'./repos/{repo1['name']}')
    else:
        print(f'Error: {response1.status_code}')