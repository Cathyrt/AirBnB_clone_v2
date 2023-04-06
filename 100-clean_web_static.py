#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of your AirBnB Clone repo, using the
function do_pack.
"""

from fabric.api import *
from datetime import datetime
import os

env.hosts = ['52.90.13.53', '52.91.131.227']


def do_deploy(archive_path):
    """Distribute an archive to a remote server"""
    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = archive_path.split("/")[-1]
        put(archive_path, "/tmp/{}".format(archive_name))
        archive_dir = archive_name.split(".")[0]
        run("mkdir -p /data/web_static/releases/{}/".format(archive_dir))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(archive_name, archive_dir))
        run("rm /tmp/{}".format(archive_name))
        run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(archive_dir, archive_dir))
        run("rm -rf /data/web_static/releases/{}/web_static".format(archive_dir))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(archive_dir))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Deploy the web static"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = int(number)
    if number < 1:
        number = 1
    elif number == 1:
        number = 2

    with cd("/data/web_static/releases/"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))

    with cd("/data/web_static/releases/versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
