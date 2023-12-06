#!/usr/bin/python3
""" Web Server """
import time
from fabric.api import local

file_path = "versions/web_static_{}.tgz".format(time.strftime("%Y%m%d%H%M%S"))


def do_pack():
    """
    generates a .tgz archive from the
    contents of the web_static folder
    """

    local("mkdir -p versions")
    arch = local("tar -cvzf {} web_static/".format(file_path))

    if arch.succeeded:
        return file_path
    else:
        return None
