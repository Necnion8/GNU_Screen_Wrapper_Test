### Example
```py
import os
import pty
import subprocess

import gnuscreen_reader as screen

# create virtual tty
master, slave = pty.openpty()

# start child process (with screen)
p = subprocess.Popen(
    "screen -S example java -Xmx1G -Xms1G -jar paper-1.8.8-445.jar",
    stdin=slave, stdout=slave, stderr=slave, close_fds=True, shell=True, cwd="../"
)
os.close(slave)

# read data
#for line in screen.read(master, cls=screen.LineTermReadParser):  # with beta line reader
for chunk in screen.read(master):
    print(chunk)
```