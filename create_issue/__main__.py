import pydash as _
from github import Github, GithubException
# Authentication is defined via github.Auth
from github import Auth

from .github_graphql import (
    get_organization_projects,
    add_issue_to_project
)


GITHUB_TOKEN = ""

auth = Auth.Token(GITHUB_TOKEN)
g = Github(auth=auth)

# Get all projects
projects = get_organization_projects(organization_name="QuanMol")

# Choose project
target_project = _.find(projects, lambda x: x["title"] == "Infrastructure")
target_project_id = target_project["id"]
target_project_title = target_project["title"]

repos = [
    # ("QuanMol/Docking-API", "vanadisArya"),
    ("QuanMol/Indigo", "luna215"),
    # ("QuanMol/Parse-PDB-API", "ansatzX"),
    # ("QuanMol/Fix-PDB-API", "zyyyzh"),
    # ("QuanMol/Prepare-Ligand-API", "ansatzX"),
    # ("QuanMol/Fix-Ligand-Bonds-API", "ansatzX"),
    # ("QuanMol/Visualization-API", "zyyyzh"),
    # ("QuanMol/Thinker-Insight-API", "HelloJocelynLu"),
    # ("QuanMol/Copy-Pocket-API", "chen0405"),
    # ("QuanMol/Copy-Task-API", "chen0405"),
    # ("QuanMol/Amber", "Jiangyuliang0813"),
    # ("QuanMol/Find-Pocket-API", "vanadisArya")
]


for (repo_name, assignee) in repos:
    repo = g.get_repo(repo_name)
    print(repo_name, assignee)
    response = repo.create_issue(
        title="This is a test to add issues to projects",
        body="""""",
        labels=[],
        assignee=assignee
    )

    issue_id = response.node_id

    add_issue_to_project(issue_id, target_project_id)
    print(f'Added issue to {target_project_title}')