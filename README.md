# repo_replicator

Script automates cloning multiple repos from github or gitlab. It reads a list of repo URLs from a .txt file and clones them into the current working directory. 

There are 2 steps:

1. Place all the repo URLs in a text file, one URL per line. If there's a line you don't want the script to read, start the line with `#`. 

2. do this:

   ``` bash 
   python clone_repos.py
   ```

