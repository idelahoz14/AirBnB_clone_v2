#!/usr/bin/python3
"""Fabric script that generates a .tgz
archive from the contents of the web_static
folder of your AirBnB Clone repo"""

from fabric.api import *
from datetime import datetime


def do_pack():
    """Return the archive path if the archive
    has been correctly generated.
    Otherwise, it should return None"""

    file_name = "web_static_" + \
    datetime.now().strftime("%Y%m%d%H%M%S") + \
    ".tgz"
    directorio = "versions/"
    local("mkdir -p " + directorio)
    check = local("tar -cvzf {}{} web_static".format(directorio, file_name))
    if check.succeeded:
        return (directorio + file_name)
    return (None)
