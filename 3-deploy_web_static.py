from fabric.api import env, local, put, run, execute
from datetime import datetime
from os.path import exists, isdir

env.hosts = ["35.175.132.56", "54.157.130.43"]

def do_pack():
    """Generates a tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except Exception as e:
        print(f"Error while creating archive: {e}")
        return None

def do_deploy(archive_path):
    """Distributes an archive to the web servers"""
    if not exists(archive_path):
        print(f"Archive {archive_path} does not exist on the local machine.")
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        execute(run, 'mkdir -p {}{}/'.format(path, no_ext), hosts=env.hosts)
        execute(run, 'tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext), hosts=env.hosts)
        execute(run, 'rm /tmp/{}'.format(file_name), hosts=env.hosts)
        execute(run, 'mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext), hosts=env.hosts)
        execute(run, 'rm -rf {}{}/web_static'.format(path, no_ext), hosts=env.hosts)
        execute(run, 'rm -rf /data/web_static/current', hosts=env.hosts)
        execute(run, 'ln -s {}{}/ /data/web_static/current'.format(path, no_ext), hosts=env.hosts)
        return True
    except Exception as e:
        print(f"Error while deploying: {e}")
        return False

def deploy():
    """Creates and distributes an archive to the web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    execute(do_deploy, archive_path, hosts=env.hosts)
    return True