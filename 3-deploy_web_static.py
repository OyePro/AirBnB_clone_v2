#!/usr/bin/python3
"""
A fabric script that create and distributes an archive to web servers
"""
do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy


def deploy():
    """Funtion to deploy for create and distributing archive to web servers"""

    archive_path = do_pack()
    print(archive_path)
    if archive_path is None:
        return False
    else:
        return do_deploy(archive_path)


deploy()
