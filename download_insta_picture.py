# WRITTEN BY MR.DIPTO
# FOLLOW MY PAGE : PING WORLD 
import os
try:
    import instaloader
except:
    os.system('pip install instaloader')
loader=instaloader.Instaloader()
insta_user=input(' ENTER INSTAGRAM USER NAME : ')
save_path=input(' ENTER THE DIRECTORY  : ')
if not os.path.exists(save_path):
    os.makedirs(save_path)
os.chdir(save_path)
try:
    download=loader.download_profile(insta_user,profile_pic_only=True)
    print(f' Profile picture downloaded successfuly to {save_path}')
except Exception as e:
    print(f' Error : {e}')