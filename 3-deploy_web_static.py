#!/usr/bin/python3
""" Web Server """
import os
import time
from fabric.api import local, run, put, env

env.hosts = ['100.26.239.247', '54.236.33.38']
env.user = "ubuntu"


def do_pack():
    """
    generates a .tgz archive from the
    contents of the web_static folder
    """

    file_path = "versions/web_static_{}.tgz".format(
            time.strftime("%Y%m%d%H%M%S"))
    local("mkdir -p versions")
    arch = local("tar -cvzf {} web_static/".format(file_path))

    if arch.succeeded:
        return file_path
    else:
        return None


def do_deploy(archive_path):
    """ distributes an archive to web servers """
    if not os.path.exists(archive_path):
        return False

    try:
        arch_filename = os.path.basename(archive_path)
        new_path = '/data/web_static/releases/{}/'.format(
                    arch_filename[:-4])
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(new_path))
        run("tar -xzf /tmp/{} -C {}".format(arch_filename,
                                            new_path))

        run("rm /tmp/{}".format(arch_filename))

        run("mv {}web_static/* {}/".format(new_path, new_path))
        run("rm -rf {}web_static".format(new_path))

        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(new_path))
        print("New version deployed!")
        return True
    except Exception:
        return False


def deploy():
    """  creates and distributes an archive to web server """
    try:
        file_path = do_pack()
        return do_deploy(file_path)
    except Exception:
        return False
