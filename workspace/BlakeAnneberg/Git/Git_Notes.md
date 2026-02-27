# Git notes

## git log --oneline --graph --all
- makes nice ASCII art of commit history

## git switch
- moves brach

## git switch -c
- create new branch off man 

## git branch
- shows what branch your on

## git switch main AND git merge vimchadsonly
- mergeing two branches, switch to main and them merge the other branch, enter message in nano and save

## git switch -c update_dune COMMITHASH
- create and switch to a new branch called update_dune, but branch off of the D commit. You can supply the commit hash directly to the git switch command:

## git commit --amend -m "F: Merge branch 'add_classics'"
- change commit message

## git rebase main
- git rebase main takes the commits unique to your current branch and replays them on top of main, creating a linear history as if you had branched from main's latest commit.
-  rebase is a preparation step that makes the eventual merge cleaner.after a rebase, the merge into main becomes a fast-forward merge — Git just moves the main pointer forward to your latest commit since there's no divergence. No merge commit needed, and the history stays perfectly linear.
- Rebase to update your feature branch with changes from main
1. On your feature branch: git rebase main
2. Switch to main: git checkout main
3. Merge your feature branch (fast-forward): git merge update_dune
- Merge (with a merge commit) when bringing the feature into main to mark "this feature was completed here"
