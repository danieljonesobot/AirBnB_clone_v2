#!/usr/bin/python3
# this script will uses fabric to create, distribute an archive to a web server
from datetime import datetime
import os.path
from fabric.api import env
from fabric.api import run
from fabric.api import local
from fabric.api import put

env.hosts = ["104.196.168.90", "35.196.46.172"]


def do_pack():
	dt = datetime.utcnow()
	file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
	if os.path.isdir("versions") is False:
