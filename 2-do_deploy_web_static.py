#!/usr/bin/python3
# Deploy the webstatic archive to nginx web servers
from fabric.api import env, put, run
import os.path


def do_deploy(archive_path):
    """
    Deploy compressed web static arvhive to servers with a
    fab command
    """
    env.hosts = ['100.25.15.3', '35.174.205.51']
    dest = '/data/web_static/releases/'
    if not os.path.isfile(archive_path):
        return False
    aext = archive_path.split('/')[-1]
    aname = aext.split('.')[0]
    if put(archive_path, '/tmp/{}'.format(aext)).failed:
        return False
    if run('mkdir -p {}{}'.format(dest, aname)).failed:
        return False
    if run('tar -xzf /tmp/{} -C {}{}/'.format(aext, dest, aname)).failed:
        return False
    if run('rm /tmp/{}'.format(aext)).failed:
        return False
    if run('mv {0}{1}/web_static/* {0}{1}/'.format(dest, aname)).failed:
        return False
    if run('rm -rf {}{}/web_static'.format(dest, aname)).failed:
        return False
    if run('rm -rf /data/web_static/current').failed:
        return False
    if run('ln -s {}{}/ /data/web_static/current'.format(dest, aname)).failed:
        return False
    return True
