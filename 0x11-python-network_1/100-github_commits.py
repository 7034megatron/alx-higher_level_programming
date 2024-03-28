import requests
import sys
***Solve challenge that takes twwo arguements***
def fetch_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error fetching commits:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python 100-github_commits.py <repository_name> <owner_name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    fetch_commits(repo_name, owner_name)
