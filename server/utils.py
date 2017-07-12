import yaml
import os

ROOT_PATH = os.getcwd()
CONF_PATH = os.path.join(ROOT_PATH, 'conf')

def load_conf(filename):
    '''
    load yaml configure
    '''
    if filename[-5:] != '.yaml':
        filename = filename + '.yaml'

    with open(os.path.join(CONF_PATH, filename), 'r') as stream:
        try:
            # print(yaml.load(stream))
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
