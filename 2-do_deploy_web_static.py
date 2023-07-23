#!/usr/bin/python3

"""
destributing an archive file to my web server
"""


from fabric.api import run, put, env
import os

env.hosts = ['35.153.18.80', '100.25.167.135']
env.user = 'ubuntu'
env.key_filename = os.path.expanduser('~/.ssh/id_rsa')


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
