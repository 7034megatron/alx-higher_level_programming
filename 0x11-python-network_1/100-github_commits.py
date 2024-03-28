#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository"""
import sys
import requests

def list_recent_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4XX or 5XX status codes
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print(f"Error fetching commits: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Malformed response from GitHub API")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <repository owner>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
