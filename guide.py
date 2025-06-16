# to use your account on GitHub, you need to set your username and email
" git config --global user.name 'Your Name' "
" git config --global user.email 'your email'"


#to clone a repository from GitHub (make sure you are granted a collaborator access to be able to push to it)
" git clone (URL) name of the folder it  will be cloned to"


#you could also FORK a repository on GitHub, which will create a copy of the repository under your account, then you can clone it to your local machine
 

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

# to connecto the remote repository
" git remote add origin (URL)"


# break down of the push command, what comes after the git push is the name of the local branch, and then the remote branch
" git push origin main" #here origin is the local branch and main is the remote branch


# to pull the changes from the remote repository
" git pull origin main " 