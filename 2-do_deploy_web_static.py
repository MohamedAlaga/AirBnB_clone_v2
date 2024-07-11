#!/usr/bin/python3
""" This module contains the function do_pack that generates a .tgz archive
  from the contents of the web_static folder (fabric script) """


from fabric.api import *
from fabric.operations import run, put
from datetime import datetime
import os


env.hosts = ['ubuntu@35.175.132.56']


def do_deploy(archive_path):

    if not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_name = os.path.basename(archive_path)
        dir_name = '/data/web_static/releases/' + os.path.splitext(archive_name)[0]
        run("mkdir -p {}".format(dir_name))
        run("tar -xzf {} -C {}".format(archive_name, dir_name))
        run("rm /tmp/{}".format(archive_name))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dir_name))
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
