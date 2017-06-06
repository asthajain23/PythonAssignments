#Write a python script which will display system name ,node name and release details of current system

import socket
import platform
print(socket.gethostname())
print(platform.platform())
print(platform.release())

#Output
'''
python second.py
demo1
Linux-3.10.0-514.21.1.el7.x86_64-x86_64-with-centos-7.3.1611-Core
3.10.0-514.21.1.el7.x86_64 '''
