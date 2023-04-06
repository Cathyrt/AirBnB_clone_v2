#!/usr/bin/python3
""" 
Generate a .tgz archive from the contents of the web_static folder.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """Create a compressed archive of the web_static folder"""
    try:
        local("mkdir -p versions")
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)
        local("tar -czvf {} web_static".format(archive_path))

        return "versions/versions/web_static_{}.tgz".format (archive_path)

    except Exception:
        return None
