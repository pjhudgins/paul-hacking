import vlc
# import os
# import sys
import ctypes
# os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")
# os.add_dll_directory(r"C:\Program Files (x86)\VideoLAN\VLC")

# ctypes.CDLL(r"C:\Program Files (x86)\VideoLAN\VLC\libvlc.dll")

instance = vlc.Instance()
player = instance.media_player_new()
media = instance.media_new("bluey.mp4")
player.set_media(media)
player.play()

# Control playback
player.pause()
player.stop()