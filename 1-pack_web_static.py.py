#!/usr/bin/python3
from fabric.api import *
from datetime import datetime


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
###connection = Connection(host="35.175.132.56",user="ubuntu",connect_kwargs={"key_filename":[r"/root/.ssh/id_rsa"]})
###connection.run("whoami")
