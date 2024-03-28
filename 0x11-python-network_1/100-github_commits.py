#!/usr/bin/python3
"""Lists the 10 most recent commits of a GitHub repository by a specific user.

Usage: ./100-github_commits.py <repository name> <owner name>
"""
import sys
import requests

def list_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for unsuccessful responses (4XX or 5XX status codes)
        
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']  # Get the commit's SHA hash
            author_name = commit['commit']['author']['name']  # Get the author's name from the commit data
            print(f"{sha}: {author_name}")  # Print the SHA hash and author's name
    except requests.RequestException as e:
        print(f"Error fetching commits: {e}")
        sys.exit(1)
    except KeyError:
        print("Error: Malformed response from GitHub API")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)
    
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
