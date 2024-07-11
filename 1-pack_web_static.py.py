#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
import os

def do_pack():
    try:
        if not os.path.exists('versions'):
            os.makedirs('versions')
        now = datetime.now()
        archive_name = 'versions/web_static_{}.tgz'.format(now.strftime("%Y%m%d%H%M%S"))
        local('tar -czvf {} web_static'.format(archive_name))
        return archive_name
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

###connection = Connection(host="35.175.132.56",user="ubuntu",connect_kwargs={"key_filename":[r"/root/.ssh/id_rsa"]})
###connection.run("whoami")
