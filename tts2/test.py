import os

# path = os.path.exists('user.py')
music_name = ".\\music\\"+"apple" + ".mp3"
if not os.path.exists(music_name):
    print(os.path.exists(music_name))
else:
    print("存在")
