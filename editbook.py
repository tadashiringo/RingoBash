import os


print("1.Tạo File  \"truyen.txt\"")
print("2.Xóa File \"truyen.txt\"")
player = input("Lựa chọn:")

if player == "1":
    os.system("vim /sdcard/Download/truyen.txt")
elif player == "2":
    os.system("rm /sdcard/Download/truyen.txt")
