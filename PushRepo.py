import os

message = raw_input("Enter Commit Message: ")
commit_command = "git commit -m " + str(message)

os.system("git status")
os.system("git add .")
os.system(commit_command)

print("Script Completed")
