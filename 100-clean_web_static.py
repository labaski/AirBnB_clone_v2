#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ['44.210.150.159', '35.173.47.15']
env.user = "ubuntu"


def wzqdo_clean(wzqnumber=0):
    """ CLEANS """

    wzqnumber = int(wzqnumber)

    if wzqnumber == 0:
        wzqnumber = 2
    else:
        wzqnumber += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(wzqnumber))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, wzqnumber))
