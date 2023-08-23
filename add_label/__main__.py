import requests
import json

from github import Github
# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("")

# First create a Github instance:

# Public Web Github
g = Github(auth=auth)

# Github Enterprise with custom hostname
g = Github(auth=auth)

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    if "QuanMol" in repo.full_name:
        try:
            print(f"Adding label to {repo.full_name}....", repo.create_label("epic: test", "BFDADC", "test label"))
        except:
            continue