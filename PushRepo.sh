echo "Enter Commit Message: "
read message

git status
git add .
git commit -m "$message"
git push -u origin master

