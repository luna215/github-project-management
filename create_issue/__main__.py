from github import Github, GithubException
# Authentication is defined via github.Auth
from github import Auth

auth = Auth.Token("")
g = Github(auth=auth)

repos = [
    ("QuanMol/Indigo", "luna215"),
    ("QuanMol/Parse-PDB-API", "ansatzX"),
    ("QuanMol/Fix-PDB-API", "zyyyzh"),
    ("QuanMol/Prepare-Ligand-API", "ansatzX"),
    ("QuanMol/Fix-Ligand-Bonds-API", "ansatzX"),
    ("QuanMol/Visualization-API", "zyyyzh"),
    ("QuanMol/Thinker-Insight-API", "HelloJocelynLu"),
    ("QuanMol/Copy-Pocket-API", "chen0405"),
    ("QuanMol/Copy-Task-API", "chen0405"),
    ("QuanMol/Amber", "Jiangyuliang0813"),
    ("QuanMol/Find-Pocket-API", "vanadisArya")
    ("QuanMol/Docking-API", "vanadisArya")
]

for (repo_name, assignee) in repos:
    # print('name', repo_name)
    repo = g.get_repo(repo_name)
    print(repo_name, assignee)
    response = repo.create_issue(
        title="Update `terraform/production/helm/deploy/deployment.yam` to be similar to `terraform/staging/helm/deploy/deployment.yaml`", 
        body="title explains the gist of it. Ask @MinzhenYi121 or @luna215 for details/help", 
        labels=["redefine-production"],
        assignee=assignee
    )

    print(response)