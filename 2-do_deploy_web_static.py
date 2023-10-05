#!/usr/bin/python3
"""
Deploy the webstatic archive to nginx web servers
"""
from fabric.api import env, put, run
import os.path

env.hosts = ['100.25.15.3', '35.174.205.51']


def do_deploy(archive_path):
    """
    Deploy compressed web static arvhive to servers with a
    fab command
    """
    dest = '/data/web_static/releases/'
    if not os.path.isfile(archive_path):
        return False
    try:
        aext = archive_path.split('/')[-1]
        aname = aext.split('.')[0]
        put(archive_path, '/tmp/')
        run('mkdir -p {}{}/'.format(dest, aname))
        run('tar -xzf /tmp/{} -C {}{}/'.format(aext, dest, aname))
        run('rm /tmp/{}'.format(aext))
        run('mv {0}{1}/web_static/* {0}{1}/'.format(dest, aname))
        run('rm -rf {}{}/web_static'.format(dest, aname))
        run('rm -rf /data/web_static/current')
        run('ln -s {}{}/ /data/web_static/current'.format(dest, aname))
        return True
    except Exception as e:
        print('DEPLOYMENT ERROR: {}'.format(str(e)))
        return False
