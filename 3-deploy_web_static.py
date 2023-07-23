#!/usr/bin/python3

"""
deploying an archive file to my web server
"""


from fabric.api import run, put, env
import os
from fabric.api import local
from datetime import datetime

env.hosts = ['35.153.18.80', '100.25.167.135']
env.user = 'ubuntu'
env.key_filename = os.path.expanduser('~/.ssh/id_rsa')


def do_pack():
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


def do_deploy(archive_path):

    """
    a function to deploy to web server
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder on the web server
    Delete the archive from the web server
    Delete the symbolic link /data/web_static/current from the web server
    new the symbolic link on the web server,
    linked to the new version of the code
    Args:
         archive_path: a.tgz archive from the contents of the web_static
    """

    if not os.path.exists(archive_path):
        return False

    try:
        archive_name = os.path.basename(archive_path)
        release = "/data/web_static/releases/" + archive_name.split('.')[0]
        put(archive_path, '/tmp/')
        run("sudo mkdir -p {}".format(release))
        run("sudo tar -xzf /tmp/{} -C {}".format(archive_name, release))
        run("sudo rm /tmp/{}".format(archive_name))
        run("sudo mv {}/web_static/* {}".format(release, release))
        run("sudo rm -rf {}/web_static".format(release))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(release))
        print("New version deployed!")
        return True
    except Exception as e:
        return False


def deploy():
    """
    that creates and distributes an archive to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
