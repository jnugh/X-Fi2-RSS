#!/usr/bin/env python3
'''
* This file is part of X-Fi2-RSS.
* X-Fi2-RSS is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
 
* X-Fi2-RSS is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
* GNU General Public License for more details.
 
* You should have received a copy of the GNU General Public License
* along with X-Fi2-RSS. If not, see <http://www.gnu.org/licenses/>.
*
* For further information check out the README file.

author: Jonas Schwabe
'''

from getopt import getopt, GetoptError
from helps import *
from rss import *
from _pyio import open
import os


debug = False
config = None
root = False
try:
    lastsave = open(os.environ['HOME']+'/.X-Fi2-RSS/last', 'r')
    root = lastsave.read().strip()
    lastsave.close()
    configfile = root+"/websync.ini"
except:
    pass

def main(args=None):
    global root
    global configfile
    global config
    global debug
    if args == None:
        args = sys.argv[1:]
    try:
        opts, args = getopt(args[0:], 'hdc:', ['help', 'debug', 'config='])
    
    except GetoptError as err:
        print(err)
        print()
        usage()
        sys.exit(2)
    
    try:
        if args[0] not in opts:
            root = args[0]
            config = root + "/websync.ini"
    except:
        pass
    
    try:
        if root:
            os.chdir(root)
    except:
        print("Root directory %s does not exists." % root)
        sys.exit(1)
    
    lastsave = open(os.environ['HOME']+'/.X-Fi2-RSS/last', 'w')
    lastsave.write(root)
    lastsave.close()
    
    try:
        #check if config already exists
        cfgf = open(configfile, 'r')
        config = cfgf.read()
        cfgf.close()
    except:
        print('Config file does not exists! Create one.')
        open(configfile, 'w').close()
        config = ''
        
    for a, o in opts:
        if a in ('-h', '--help'):
            help()
        elif a in ('-d', '--debug'):
            debug = True
        elif a in ('-c', '--config'):
            print('Used config %s, I recommend to use the websync.ini in the root directory of the player, to get Windows compatibility. If you hate Windows forget about :)' % o)
            config = o
#        elif a in ()
if __name__ == '__main__':
    main()
pass