import os
import pty
import subprocess

import gnuscreen_reader as screen

# create virtual tty
master, slave = pty.openpty()

# copy environ and set TERM
env = dict(os.environ)
env["TERM"] = "vt100"

# start child process (with screen)
env = dict(os.environ)
env["TERM"] = "vt100"
p = subprocess.Popen(
    "screen -S example java -Xmx1G -Xms1G -jar paper-1.8.8-445.jar",
    stdin=slave, stdout=slave, stderr=slave, close_fds=True, shell=True, cwd="../",
    env=env,
)
os.close(slave)

# read data
#for line in screen.read(master, cls=screen.LineTermReadParser):  # with beta line reader
for chunk in screen.read(master):
    print(chunk)
