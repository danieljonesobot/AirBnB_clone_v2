#!/usr/bin/python3
# using fabfile to generates .tgz archive from contents of the web_static.
import os.path
from datetime import datetime
from fabric.api import local

def do_pack():
	"""This function ouses fabric to generate .tgz"""
	date_time = datetime.utcnow()
	files = "versions/web_static_{}{}{}{}{}{}.tgz".format(date_time.year,
                                                         date_time.month,
                                                         date_time.day,
                                                         date_time.hour,
                                                         date_time.minute,
                                                         date_time.second)
	if os.path.isdir("versions") is False:
		if local("mkdir -p versions").failed is True:
			return None
	if local("tar -cvzf {} web_static".format(files)).failed is True:
		return (None)
	return (files)
