#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers"""

from fabric.contrib import files
from fabric.api import env, put, run
from os import path


env.hosts = ['34.74.119.103', '34.73.124.222']


def do_deploy(archive_path):
    """Function for deploy"""
    if not path.exists(archive_path):
        return False

    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dst = data_path + name

    try:
        put(archive_path, '/tmp')
        run('mkdir -p {}'.format(dst))
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dst))
        run('rm -f /tmp/{}.tgz'.format(name))
        run('mv {}/web_static/* {}/'.format(dst, dst))
        run('rm -rf {}/web_static'.format(dst))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(dst))
        return True
    except:
        return False
