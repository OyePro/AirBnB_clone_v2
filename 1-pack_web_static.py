#!/usr/bin/python3
"""
A Fabric script that generates a `.tgz` archive from the
contents of the web_static folder
"""
import os
from datetime import datetime
from fabric.api import runs_once, local


@runs_once
def do_pack():
    """function do_pack"""
    if not os.path.exists("versions"):
        os.makedirs("versions")
    time = datetime.now().strftime('%Y%m%d%H%M%S')
    archive = f"web_static_{time}.tgz"
    archive_path = f"versions/{archive}"

    try:
        print("Packing web_static to {}".format(archive_path))
        local(f"tar -cvzf {archive_path} web_static")
        size = os.stat(archive_path).st_size
        print(f"web_static packed: {archive_path} -> {size} Bytes")
    except Exception:
        archive_path = None
    return archive_path
