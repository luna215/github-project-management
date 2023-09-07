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
            print(f"Adding label to {repo.full_name}....", repo.create_label("redefine-production", "E9BE95", "Issue pertaining to redefine-production eks cluster"))
        except GithubException as e:
            print('Label already exists', e)