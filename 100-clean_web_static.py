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


def do_clean(number=0):
    """Delete out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    with cd("/data/web_static/releases/"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))

    with cd("/data/web_static/releases/versions"):
        local("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
        run("ls -t | tail -n +{} | xargs -I {{}} rm -rf {{}}".format(number + 1))
