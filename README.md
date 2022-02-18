# Snippets of Code

## Setup Shell
Install zshell, oh-my-zshell, powerline10k


## Clean setup of Conda environment

```bash
conda create -n test_poly
conda activate test_poly
conda install pip
pip install ipykernel
python -m ipykernel install --user --name test_poly --display-name "test_poly"
```


## Access the position of the module, e.g. to find relative folder
```python
from pathlib import Path
source_path = Path(__file__).resolve().parent.parent
```

## API
```bash
pip install -r flask_app/requirements.txt
python flask_app/app.py
# do this in another window
curl localhost:5000
curl localhost:5000/favorite_number # here we see the allowed return types
curl localhost:5000/personalized_greeting
curl -X POST -d name=lukas localhost:5000/personalized_greeting
curl -X POST -d a=1 -d b=3 localhost:5000/add_numbers
```


## GIT 
#### Session 1: Basics
* add, commit, push
* Pull requests
* merge, rebase, rebase vs merge
* git squash
* git cherry-pick
* git log
    
* HEAD

#### Session 2: Advanced
* branch naming und jira integration
* git shelves
* git blame and git history
* git tag, versioning, releases
* branch protection rules
  git patch
* commit hooks (example in commit_hooks folder)
* add a remote repository, if you have a client repo:
How to remote push a repo to our beloved Ginkgo Gitlab:
Setup new (empty) Ginkgo Repo
```bash
cd in local repo
git add remote ginkgo {{url vom ginkgo repo}}.git
git push
```

```bash
git init
# the commit-msg file needs to be moved into the .git/hooks folder
# the file needs to be executable
chmod 755 .git/hooks/commit-msg
# to test
.git/hooks/commit-msg commit_hooks/valid_message
.git/hooks/commit-msg commit_hooks/invalid_message
```
  
* how to make your team mates hate you with 5 simple commands
* git bisect 
*  squash or no squash


## Regex

Very good tutorial: https://regexone.com/

Test: Change the date format from DD.MM.YYYY to YYYY-MM-DD.
01.09.1992
Find: (\d+).(\d+).(\d+)
Solution$3-$2-$1