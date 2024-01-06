#!/usr/bin/python3
"""
A a Fabric script that distributes an archive to your web servers
"""
import os
from fabric.api import put, run, env

env.user = 'ubuntu'
env.hosts = ['54.159.1.148', '3.85.33.34']


def do_deploy(archive_path):
    """
    function do_deploy for distributing achives to servers
    """

    if os.path.exists(archive_path) is False:
        return False

    """ archive_path = versions/web_static_20240104.tgz """
    archive_name = archive_path.split("/")[1]
    name_ext = archive_name.split(".")[0]
    folder = f"/data/web_static/releases/{name_ext}"

    try:
        put(archive_path, "/tmp")
        run(f"sudo mkdir -p {folder}")
        run(f"sudo tar -xzf /tmp/{archive_name} -C {folder}")
        run(f"sudo rm -f /tmp/{archive_name}")
        run(f"sudo mv {folder}/web_static/* {folder}/")
        run(f"sudo rm -rf {folder}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s {folder} /data/web_static/current")
        print("New version deployed!")
        return True
    except Exception:
        return False
