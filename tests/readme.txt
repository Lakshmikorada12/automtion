git config --global user.email v.v.lakshmi.korada@gmail.com
git config --global user.name "Lakshmikorada12"
git init
git add * staging
git commit -m "firstcommit"---local directory commit
git remote add origin https://github.com/Lakshmikorada12/automtion.git======>to remote connection
echo "# automation-project2" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Lakshmikorada12/automation-project2.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/Lakshmikorada12/automation-project2.git
git branch -M main
git push -u origin main

git add *

C:\Users\HP\Desktop\files>git commit -m "added for brancing"
[master 7d4be71] added for brancing
 1 file changed, 34 insertions(+)
 create mode 100644 tests/Brach1.py

C:\Users\HP\Desktop\files>git push origin master
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 315 bytes | 315.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/Lakshmikorada12/automtion.git
   c01ffc2..7d4be71  master -> master

git checkout -b develpoe----new branch creation
Switched to a new branch 'develpoe'
Git branch ----to know the git brances
Git add *--add the files to the stage
Git commit -m “added files”
git push origin develpoe---added to the git


git pull origin develpoe---get the data to the local
git checkout develpoe=to go the created branch
git checkout master
git merge develpoe---it will merge with active branch

