#!/usr/bin/python3
# Fabfile to compress web_static content into a .tgz archive

from fabric.api import local
from datetime import datetime
import os.path


def do_pack():
    """
    A fuction to compress web_static content into a .tgz archive
    """
    now = datetime.utcnow()
    filename = "versions/web_static_{}.tgz".format(
            now.strftime('%Y%m%d%H%M%S'))
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(filename)).failed:
        return None
    return filename
