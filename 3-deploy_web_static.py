#!/usr/bin/python3
"""
fab file to deploy web static files to server
"""

from fabric.api import *
from fabric.operations import run, put
from datetime import datetime
import os

env.hosts = ['ubuntu@35.175.132.56','ubuntu@54.157.130.43']

def do_pack():
    """ Fabric script that generates a .tgz archive from the contents of the...
    ...web_static folder """
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("sudo tar -cvzf {} web_static".format(filename))
    if result.succeeded:
        return filename
    else:
        return None

def do_deploy(archive_path):
    """ distributes an archive to my web servers
    """
    if not os.path.exists(archive_path):
        return False
    filename = archive_path.split('/')[-1]
    no_tgz = '/data/web_static/releases/' + "{}".format(filename.split('.')[0])
    tmp = "/tmp/" + filename
    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}/".format(no_tgz))
        run("tar -xzf {} -C {}/".format(tmp, no_tgz))
        run("rm {}".format(tmp))
        run("mv -f {}/web_static/* {}/".format(no_tgz, no_tgz))
        run("rm -rf {}/web_static".format(no_tgz))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(no_tgz))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False

def deploy():
    """
    execute both do_pack and do_deploy
    """
    archive = do_pack()
    if os.path.exists(archive) is False:
        return False
    dep = do_deploy(archive)
    return dep
