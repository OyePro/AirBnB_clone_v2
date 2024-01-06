#!/usr/bin/python3
"""
A fabric script that deletes out-of-dates archives
"""
import os
from fabric.api import *

env.user = 'ubuntu'
env.hosts = ['54.159.1.148', '3.85.33.34']


def do_clean(number=0):
    """method do_clean for deleting archives"""

    if int(number) == 0:
        number = 1
    else:
        number = int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for newest in range(number)]
    with lcd("versions"):
        [local(f"rm ./{oldest}") for oldest in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [name for name in archives if "web_static_" in name]
        [archives.pop() for newest in range(number)]
        [run(f"sudo rm -rf ./{oldest}") for oldest in archives]
