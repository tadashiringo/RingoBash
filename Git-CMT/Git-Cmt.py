import os

ringo_login = "login.py"

print("1. ringo-login.py")
player = input("Nhập: ")

if player == "1":
    player_commit = input("Nhập vào Commit của %s: "%ringo_login)
    os.system("git add %s && git commit -m \"%s\""%( ringo_login , player_commit))
        
