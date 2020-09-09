import os

home_dir = os.system("cd ~")
print("`cd ~` ran with exit code %d" % home_dir)

unknown_dir = os.system("cd doesnotexist")
print("`cd doesnotexis` ran with exit code %d" % unknown_dir)
