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
git checkout -b NEW_BRANCH_NAME SOURCE_BRANCH_NAME
