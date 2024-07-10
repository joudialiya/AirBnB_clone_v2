#!/usr/bin/python3
"""
Fabric script based on the file 2-do_deploy_web_static.py that creates and
distributes an archive to the web servers
"""

from fabric.api import env, local, put, run
from datetime import datetime
from os.path import exists, isdir


env.hosts = ['100.26.236.180', '100.25.163.248']


def do_pack():
    """generates a tgz archive"""
    try:
        dt = datetime.utcnow()
        archive_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)
        if not isdir("versions"):
            local("mkdir -p versions")
        local("tar -cvzf {} web_static".format(archive_name))
        return archive_name
    except Exception as e:
        print(e)
        return None


def do_deploy(archive_path):
    """ deploy the zip in the """
    if exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            basename = os.path.basename(archive_path)
            basename_no_ext = basename.split(".")[0]
            target_location = "/data/web_static/releases/"
            target_location += basename_no_ext
            target_location += "/"
            run("mkdir -p " + target_location)
            run("tar -xzf /tmp/" + basename + " -C " + target_location)
            run("rm /tmp/" + basename)
            run("mv " + target_location + "web_static/* " + target_location)
            run("rm -rf " + target_location + "web_static")
            run("rm -rf /data/web_static/current")
            run("ln -s " + target_location + " /data/web_static/current")
            print("New version deployed!")
            return True
        except Exception as e:
            print("Error:", e)
            return False


def deploy():
    """deploy the archive to the servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
