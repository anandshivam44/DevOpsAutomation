## Git Cheat Sheet  

#### To keep in sync with remote branch (You may loose your local changes in the branch)
```bash
git fetch --all
```
```bash
git reset --hard origin/BRANCH_NAME
```

 #### Git forceful deletion of a branch without merging it
```bash
git branch -D BRANCH_NAME
```
 #### Git create a branch from another branch
```bash
git checkout -b NEW_BRANCH_NAME SOURCE_BRANCH_NAME
```
 #### Git rename a local branch
 ```bash
 git checkout OLD_BRANCH_NAME
 ```
 ```bash
 git branch -m NEW_BRANCH_NAME
 ```
 `-m, --move            move/rename a branch and its reflog`
 #### Git rename a remote branch
 ```
 git push origin -u NEW_BRANCH_NAME
 ```
 ```
 git push origin --delete OLD_BRANCH_NAME
 ```
 #### Modify previous commit message
```bash
#remote: Use this command to change commit message (one commit at a time):
git rebase --interactive 985f75c0e537c357414b2a60f38a07dfe941f91b^
# remote: In the default editor, modify 'pick' to 'edit' in the line whose commit you want to modify
git commit --amend
# remote: modify the commit message
run: git rebase --continue
```
 #### Mistakenly did a git add. To remove a file from staging area use
```bash
git reset filename
```
To unstag all changes use
```bash
git reset
```
#### Get `git diff` after it was staged using `git add`
```bash
git diff --staged
```
#### Remove a file from staging if it was added using `git add` / Undo `git add`
```bash
git restore --staged <file>
```
#### git checkout remote branch
```bash
git checkout -b BRANCH_NAME origin/BRANCH_NAME 
```
#### git stash changes. By stashing changes you can change your current branch without having to worry about commiting changes in branch.
```bash
git stash
git checkout BRANCH
git stash pop
```
#### git stash changes including untracked files. By stashing changes you can change your current branch without having to worry about commiting changes in branch.
```bash
git stash --include-untracked
git checkout BRANCH
git stash pop
```
#### Clear git stash
```bash
git stash clear
```
#### git goto to a particular commit
```bash
git reflog # check commits; you can also use git log
git reset --hard commit_SHA
```
#### git undo previous commit. This will undo the commit and remove changes from staging, but your previous commit file changes will not be lost
```bash
git reset HEAD~1
```
#### git goback to previous commit (IMPORTANT: All changes will be discarded)
```bash
git reset --hard HEAD
```
#### git goback to (previous - 1 commit) (IMPORTANT: All changes will be discarded)
```bash
git reset --hard HEAD~1
```
#### git check history of a file
```bash
git log -p -- filepath
```
#### git bring changes from a specific commit from a specific repository into working repository
use git log to get commit hash from the branch you branch you want to bring changes, then 
```bash
git checkout WORKING_BRANCH
git cherry-pick <commit-hash>
```
Note: The new changes will be commited into the working branch
