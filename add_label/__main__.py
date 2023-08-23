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


# ORGANIZATION="QuanMol"
# TOKEN="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" # Add PAT here

# ORG_REPOS = "https://api.github.com/orgs/{org}/repos"

# headers = {
#     "Authorization": f"token {TOKEN}",
#     "Accept": "application/vnd.github+json"
# }


# print(ORG_REPOS.format(org=ORGANIZATION))
# print(requests.get(ORG_REPOS.format(org=ORGANIZATION)).json())