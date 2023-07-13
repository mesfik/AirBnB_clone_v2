#!/usr/bin/python3
"""
Packing a web_static to deploy
"""


from fabric.api import local
from datetime import datetime
from fabric import task


def do_pack(ctx):
    """Pack the web static folder in to .tgz file format"""
    try:
        current_time = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        local("chown -hR $USER:$USER versions")
        archive_name = "versions/web_static_" + current_time + ".tgz"
        local("tar -cvzf {} web_static".format(archive_name))
        return (archive_name)
    except Exception as e:
        return None
