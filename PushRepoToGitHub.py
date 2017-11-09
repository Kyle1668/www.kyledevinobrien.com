import os

print("Enter Commit Message: ")

message = raw_input("Enter Message: ")
commit_command = "git commit -m " + str(message)

os.system("git status")
os.system("git add .")
os.system(commit_command)
