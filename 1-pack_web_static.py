#!/usr/bin/python3

"""
contains function that  generates an archive
"""
from fabric.api import *

def do_pack():
    local("mkdir -p versions")

    local("tar -cvzf versions/web_static.tgz web_static")
