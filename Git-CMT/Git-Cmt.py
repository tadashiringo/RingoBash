import os

# Khai báo lệnh
git_rm = "git rm"
git_add = "git add"
git_commit = "git commit -m"
git_status = "git status"
git_restore = "git restore"



print("1. Chi Nhánh")
print("2.Thêm file")
player = input("Lựa chọn: :")


if player == "1":
    print("1.Chuyển chi nhánh\n2.Tạo chi nhánh\n3.Xóa chi nhánh(Chưa tạo)")
    player = input("Nhập(Mặc định =1):")
    if player == "1" or player =="":
        os.system("git branch")
        player = input("Nhập tên chi nhánh: ")
        os.system("git checkout %s"%player)
    elif player == "2":
        player = input("Nhập tên chi nhánh muốn tạo ra: ")
        os.system(F"git branch %s"%player)
    elif player == "3":
        player == input("Tên chi nhánh muốn xóa: ")
        os.system("git branch -d %s"%player)
elif player == "2":
    os.system(git_status)
    print("1. Thêm\n2.Xóa\3.Khôi phục")
    player = input("Nhập: ")
    if player == "1" :
        player = input("File muốn thêm vào: ")
        os.system("%s %s"%(git_add,player))
        player = input("Bạn có muốn nhập Commit không?(y/n)")
        if player == "y" or player == "Y" or "1":
            player = input("Commit: ")
            os.system("%s \"%s\""%(git_commit,player))
    elif player == "2" :
        player = input("File muốn xóa: ")
        os.system("%s %s"%(git_rm,player))
    elif player == "3":
        player = input("File muốn khôi phục: ")
        os.system("%s %s"%(git_restore,player))
