import os

ringo_login = "login.py"
print("1. Chi Nhánh")
player = input("Lựa chọn: ")
if player == "1":
    print("1.Chuyển chi nhánh\n2.Tạo chi nhánh\n3.Xóa chi nhánh(Chưa tạo)")
    player = input("Nhập(Mặc định =1):")
    if player == "1" or player =="":
        os.system("git branch")
        player = input("Nhập tên chi nhánh: ")
        os.system("git checkout %s"%player)
'''
print("1. ringo-login.py")
player = input("Nhập: ")

if player == "1":
    player_commit = input("Nhập vào Commit của %s: "%ringo_login)
    os.system("git add %s && git commit -m \"%s\""%( ringo_login , player_commit))

'''
