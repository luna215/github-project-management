from github import Github, GithubException
# Authentication is defined via github.Auth
from github import Auth

# using an access token
auth = Auth.Token("")

# First create a Github instance:
g = Github(auth=auth)


for repo in g.get_user().get_repos():
    if "QuanMol" in repo.full_name:
        try:
            # print(f"Adding label to {repo.full_name}....", repo.create_label("P0 - Critical", "B60205", "Priority: Release blocker or regression"))
            # print(f"Adding label to {repo.full_name}....", repo.create_label("P1 - Important", "FD7B09", "Priority: High Impact"))
            # print(f"Adding label to {repo.full_name}....", repo.create_label("P2 - Normal", "FBCA04", "Priority: Nice to Have"))
            print(f"Adding label to {repo.full_name}....", repo.create_label("P3 - Low", "498415", "Priority: Stretch Goal"))
        except GithubException as e:
            print('Label already exists', e)