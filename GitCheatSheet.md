### Git Cheat Sheet  

- To keep in sync with remote branch (You may loose your local changes in the branch)
```bash
git fetch --all
```
```bash
git reset --hard origin/BRANCH_NAME
```

 - Git forceful deletion of a branch without merging it
```bash
git branch -D BRANCH_NAME
```
 - Git create a branch from another branch
```bash
git checkout -b NEW_BRANCH_NAME SOURCE_BRANCH_NAME
```
 - Git rename a local branch
 ```bash
 git checkout OLD_BRANCH_NAME
 ```
 ```bash
 git branch -m NEW_BRANCH_NAME
 ```
 `-m, --move            move/rename a branch and its reflog`
 - Git rename a remote branch
 ```
 git push origin -u NEW_BRANCH_NAME
 ```
 ```
 git push origin --delete OLD_BRANCH_NAME
 ```
