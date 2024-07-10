#!/usr/bin/python3
"""this module is a fabric config"""

import os
import datetime
from fabric.api import local


def do_pack():
    """We pack the web_static content"""
    dt = datetime.datetime.utcnow()
    archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_name)).failed is True:
        return None
    return archive_name
