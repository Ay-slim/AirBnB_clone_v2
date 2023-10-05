#!/usr/bin/python3
"""
Remove archives that are not up to date
"""
from fabric.api import env, lcd, cd, local, run
import os

env.hosts = ['100.25.15.3', '35.174.205.51']


def do_clean(number=0):
    """
    Remove archives not up to date
    """
    if not int(number):
        number = 1
    else:
        number = int(number)

    archs = sorted(os.listdir('versions'))
    for i in range(number):
        archs.pop()

    with lcd('versions'):
        for j in archs:
            local('rm ./{}'.format(j))

    with cd('/data/web_static/releases'):
        archs = run('ls -tr').split()
        archs_tmp = []
        for k in archs:
            if 'web_static_' in k:
                archs_tmp.append(k)
        archs = archs_tmp
        for m in range(number):
            archs.pop()
        for n in archs:
            run('rm -rf ./{}'.format(n))
