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
git checout -b BRANCH_NAME origin/BRANCH_NAME 
```
