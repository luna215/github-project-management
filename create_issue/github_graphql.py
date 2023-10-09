import requests

GITHUB_API_V4 = "https://api.github.com/graphql"
GITHUB_TOKEN = ""


def get_organization_projects(organization_name: str) -> list[dict]:
    """Gets all projects for an organization"""

    # Get all projects query
    body = """
    query {
        organization(login:""" + f'"{organization_name}"' + """) {
        projectsV2(first: 100) {
            totalCount
            nodes {
                title
                id
            }
        }
      }
    }
    """
    response = requests.post(url=GITHUB_API_V4, json={"query": body},
                             headers={"Authorization": f"Bearer {GITHUB_TOKEN}"}).json()
    projects = response["data"]["organization"]["projectsV2"]["nodes"]

    return projects


def add_issue_to_project(issue_id: str, project_id: str) -> None:
    """Adds an issue to a project"""

    body = """
    mutation {
        addProjectV2ItemById(input: { projectId: """ + f'"{project_id}"' + """, contentId: """ + f'"{issue_id}"' + """}) {
            item {
                id
            }
        }
    }
    """
    from pprint import pprint
    pprint(body)
    response = requests.post(url=GITHUB_API_V4, json={"query": body},
                             headers={"Authorization": f"Bearer {GITHUB_TOKEN}"}).json()