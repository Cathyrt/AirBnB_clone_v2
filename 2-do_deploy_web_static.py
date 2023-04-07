#!/usr/bin/python3
"""
Fabric script that compress web static package
"""
from fabric.api import *
import os
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['52.90.13.53', '52.91.131.227']
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ Distributes an archive to web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        archive_filename = os.path.basename(archive_path)
        archive_folder = "/data/web_static/releases/{}".format(
            archive_filename.split(".")[0])
        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".
            format(archive_filename, archive_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
        run("rm -rf {}/web_static".format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_folder))
        return True
    except Exception:
        return False
