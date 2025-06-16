#to switch between commits you can checkout to main then
" git log "   # and choose the idea of the commit you want



#This will add a new commit that undoes what was done in commit a1b2c3d.
"git revert a1b2c3d"


#This will move your branch to commit a1b2c3d and delete all commits and changes after it.
" git reset --hard a1b2c3d "


#to create a new branch and switch to it in the same command
" git checkout -b new-branch-name "


#after making changes in the new branch, you can merge it back to the main branch,first switch to the main branch then
" git merge new-branch-name "

