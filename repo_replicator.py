import subprocess
import os

repo_list = "./repos.txt"


def get_repos_to_clone(filepath: str) -> list:
    """
    Reads file line by line, ignoring blanks and those starting with "#".
    It then appends them to a list.

    Args:
        filepath (str): path to txt file.

    Returns:
        list: except for blanks and comments, all lines from the file.
    """
    repos_to_clone = []
    with open(filepath, "r") as f:
        for line in f:
            each_line = line.strip()
            # ignore blank lines and comments
            if each_line and not each_line.startswith("#"):
                repos_to_clone.append(each_line)
                print(f"Found repo: {each_line}")
    return repos_to_clone


def convert_https_to_ssh(https_url: str) -> str:
    """
    Convert Github and Gitlab https urls to ssh urls.

    Args:
        https_url (str): https url. e.g. https://github.com/garthmortensen/testing_cloud

    Returns:
        str: ssh url. e.g. git@github.com:garthmortensen/testing_cloud.git

    Raises:
        ValueError: If url is not Github or Gitlab.
    """
    if "https://github.com/" in https_url:
        repo = https_url.replace("https://github.com/", "")
        ssh_url = f"git@github.com:{repo}.git"
    elif "https://gitlab.com/" in https_url:
        repo = https_url.replace("https://gitlab.com/", "")
        ssh_url = f"git@gitlab.com:{repo}.git"
    else:
        raise ValueError(f"unexpected repo url for {https_url}")
    return ssh_url


def clone_repo(ssh_git: str, clone_destination: str=None) -> None:
    """
    Given an ssh_url, clone the repo.
    
    NB: if you have an ssh passphrase, this throws error with exit status 128.

    Args:
        ssh_git (str): git repo's ssh url.
        clone_destination (str): path to clone the repo into. Default = current dir.

    Returns:
        None
    """
    if clone_destination is None:
        clone_destination = os.getcwd()
    
    print(f"cloning: {ssh_git}")
    subprocess.run(["git", "clone", ssh_git, clone_destination], check=True)
    print(f"cloned:  {ssh_git}")


# all your repos are belong to us
repos_to_clone = get_repos_to_clone(repo_list)
for repo in repos_to_clone:
    ssh_git = convert_https_to_ssh(repo)
    clone_repo(ssh_git)
