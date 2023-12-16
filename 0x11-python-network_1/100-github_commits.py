#!/usr/bin/python3
"""
Script to list 10 commits (from the most recent to oldest)
of a given repository by a specified user using GitHub API.
"""
import sys
import requests


def get_commits(repo, owner):
    """
    Get the list of commits from the GitHub API
    """
    url = f'https://api.github.com/repos/{owner}/{repo}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Unable to fetch. Status code: {response.status_code}")
        return None


def print_commits(commit_list):
    """
    Print the commits, up to 10 commits
    """
    for i, commit in enumerate(commit_list[:10]):
        sha = commit.get('sha')
        au_name = commit.get('commit', {}).get('author', {}).get('name', 'UA')
        print(f'{sha}: {au_name}')


def main(argv):
    """
    Main function to list 10 commits for a given repository and owner
    """
    repo = argv[1]
    owner = argv[2]

    commit_list = get_commits(repo, owner)
    if commit_list is not None:
        print_commits(commit_list)


if __name__ == "__main__":
    main(sys.argv)
