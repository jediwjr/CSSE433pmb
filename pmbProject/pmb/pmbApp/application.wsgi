import os, sys

PROJECT_DIR = '/home/csse/CSSE433pmb/pmbProject/pmb'

activate_this = os.path.join(PROJECT_DIR, 'bin', 'activate_this.py')
execfile(activate_this, dict(__file__=activate_this))
sys.path.append(PROJECT_DIR)

sys.path.append('/home/csse/CSSE433pmb/pmbProject/pmb/pmbApp')

from pmbApp import app as application
