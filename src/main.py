#!/usr/bin/env python2
# -*- coding: utf-8 -*- 
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
import os
import ConfigParser
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
    global cfg
    global sync
    sync = False
    if args == None:
        args = sys.argv[1:]
    try:
        opts, args = getopt(args[0:], 'hdc:sa:r:t:o:', ['help', 'debug', 'config=', 'sync', 'add=', 'remove=', 'time=', 'old='])
        if opts == []:
            opts, args = getopt(args[1:], 'hdc:sa:r:t:o:', ['help', 'debug', 'config=', 'sync', 'add=', 'remove=', 'time=', 'old='])
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
        try:
            open(configfile, 'w').close()
            config = ''
        except:
            print('Could not write configfile %s.' % configfile)
            sys.exit(1)
        
    for a, o in opts:
        print(a)
        if a in ('-h', '--help'):
            help()
        elif a in ('-d', '--debug'):
            debug = True
        elif a in ('-c', '--config'):
            print('Used config %s, I recommend to use the websync.ini in the root directory of the player, to get Windows compatibility. If you hate Windows forget about :)' % o)
            config = o
        elif a in ('-a', '--add'):
            pass
        elif a in ('-r', '--remove'):
            pass
        elif a in ('-t', '--time'):
            pass
        elif a in ('-o', '--old'):
            if not o == 'delete' and not o == 'store':
                print("Delte or store was expected for --old")
                sys.exit(1)
            else:
                print('Not implemented yet! TODO')
                #TODO What to do with old enterys?
        elif a in ('-s', '--sync'):
            print('sync')
            sync = True
    cfg = ConfigParser.ConfigParser()
    cfg.read(configfile)
    try:
        print("Last update: %s" % cfg.get('Options', 'UpdateTime'))
        print("%s RSS Feeds is/are available" % cfg.get('Options', 'RSS Count'))
    except:
        print("Configfile does not exist or is invalid use fix to get it right (not implemented now)")
        sys.exit(1)
    if sync:
        syncall(cfg, root)
        
if __name__ == '__main__':
    main()
pass