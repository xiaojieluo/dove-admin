import yaml
import hashlib
import os
# from server.web import CONF_PATH

ROOT_PATH = os.getcwd()
CONF_PATH = os.path.join(ROOT_PATH, 'conf')

def load_conf(filename, subconf=None):
    '''
    load yaml configure
    '''
    if filename[-5:] != '.yaml':
        filename = filename + '.yaml'

    conf_file = os.path.join(CONF_PATH, filename)
    with open(conf_file, 'r') as stream:
        try:
            data = yaml.load(stream)
            return data
        except yaml.YAMLError as exc:
            print(exc)
            return

def dump(string, switch=True):
    if switch is True:
        print(string)


def md5(string, salt=None):
    '''md5 加密'''
    if string is None:
        return
    if salt is not None:
        string = string + salt

    data = hashlib.md5(string.encode('utf-8'))

    return data.hexdigest()
