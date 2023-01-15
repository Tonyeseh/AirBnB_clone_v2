#!/usr/bin/python3
"""
Generates a .tgz archive file from web_static folder
"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """
        Generates archive files and stores them in version folder
    """
    try:
        time = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
        arc_name = "versions/web_static_{}.tgz".format(time)

        local("mkdir -p versions")
        arc_result = local(
                "tar -cvzf {} web_static/".format(arc_name),
                capture=True)

        return arc_result
    except Exception:
        return None
