#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to web servers
"""
from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['52.90.13.53', '52.91.131.227']
env.user = 'ubuntu'


def do_pack():
    """Compress files into a .tgz archive."""
    try:
        if not exists("versions"):
            local("mkdir versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Distribute archive to web servers."""
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_name = archive_path.split("/")[-1]
        folder_name = "/data/web_static/releases/" + archive_name.split(".")[0]
        run("mkdir -p {}".format(folder_name))
        run("tar -xzf /tmp/{} -C {}".format(archive_name, folder_name))
        run("rm /tmp/{}".format(archive_name))
        run("mv {}/web_static/* {}".format(folder_name, folder_name))
        run("rm -rf {}/web_static".format(folder_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_name))
        return True
    except Exception:
        return False


def deploy():
    """Create and distribute archive to web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
