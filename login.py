import os
admin_user = "Tadashi Ringo"
admin_pass = "tadashiringo123"
print("-------")
print("Nhập vào tài khoản của bạn!!!")
print("-------")
player_user = input("Tên: ")
player_pass = input("Mật Khẩu:  ")
while True:
    if player_user == admin_user and player_pass == admin_pass:
        os.system("echo Đăng nhập thành công")
        break
    else:
        os.system("echo tên hoặc mật khẩu không đúng,vui lòng nhập lại")
        player_user = input("Nhập tên  ngừi dùng: ")
        player_pass = input("Nhập mật khẩu người dùng: ")
