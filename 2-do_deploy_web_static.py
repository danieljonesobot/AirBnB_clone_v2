#!/usr/bin/python3
"""
this script uses Fabric package to distribute an archive to your web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["18.209.179.241", "35.153.33.57"]
env.user = "ubuntu"


def do_pack():
	"""
	this function i will return the archive path
	"""

	local("mkdir -p versions")
	lcl = datetime.now().strftime("%Y%m%d%H%M%S")
	a_f_p = "versions/web_static_{}.tgz".format(lcl)
	tgz_archive = local("tar -cvzf {} web_static".format(a_f_p))

	if tgz_archive.succeeded:
		return a_f_p
	else:
		return None


def do_deploy(archive_path):
	"""
	this function will distribute archive
	"""
	if os.path.exists(archive_path):
		a_f_n = archive_path[9:]
		n_v_p = "/data/web_static/releases/" + a_f_n[:-4]
		a_f_p = "/tmp/" + a_f_n
		put(archive_path, "/tmp/")
		run("sudo mkdir -p {}".format(n_v_p))
		run("sudo tar -xzf {} -C {}/".format(a_f_p, n_v_p))
		run("sudo rm {}".format(a_f_p))
		run("sudo mv {}/web_static/* {}".format(n_v_p, n_v_p))
		run("sudo rm -rf {}/web_static".format(n_v_p))
		run("sudo rm -rf /data/web_static/current")
		run("sudo ln -s {} /data/web_static/current".format(n_v_p))

		print("New version deployed!")
		return True

	return False
