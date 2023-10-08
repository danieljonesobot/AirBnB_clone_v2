#!/usr/bin/python3
"""
A Fabric script, which builds upon the 2-do_deploy_web_static.py file, is designed to generate and transfer an archive to the web servers.
"""
from datetime import datetime
from fabric.api import env, local, put, run
from os.path import exists, isdir
env.hosts = ['34.232.65.63', '52.201.163.252']


def do_pack():
    """this function will generates a tgz archive"""
    try:
        dt = datetime.now().strftime("%Y%m%d%H%M%S")
        if isdir("versions") is False:
            local("mkdir versions")
        name_file = "versions/web_static_{}.tgz".format(dt)
        local("tar -cvzf {} web_static".format(name_file))
        return name_file
    except:
        return None


def do_deploy(archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        name_file = archive_path.split("/")[-1]
        ext = file_n.split(".")[0]
        path = "/data/web_static/releases/"
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(path, ext))
        run('tar -xzf /tmp/{} -C {}{}/'.format(name_file, path, ext))
        run('rm /tmp/{}'.format(name_file))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(path, ext))
        run('rm -rf {}{}/web_static'.format(path, ext))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(path, ext))
        return True
    except:
        return False


def deploy():
    """creates and distributes an archive to the web servers"""
    path_of_archive = do_pack()
    if path_of_archive is None:
        return False
    return do_deploy(path_of_archive)
