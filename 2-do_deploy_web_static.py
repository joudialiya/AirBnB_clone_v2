#!/usr/bin/python3

""" Fabric file to deploy """

import os
from fabric.api import run, put, env

env.hosts = ['100.26.236.180', '100.25.163.248']
env.user = "ubuntu"


def do_deploy(archive_path):
    """ deploy the zip in the """
    if os.path.exists(archive_path) is False:
        return False
    else:
        try:
            put(archive_path, "/tmp/")
            basename = os.path.basename(archive_path)
            basename_no_ext = basename.split(".")[0]
            target_location = "/data/web_static/releases/"
            + basename_no_ext
            + "/"
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
