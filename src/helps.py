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

def help():
    print("""Parameters for X-Fi2-RSS:
    
Common:
    -h    --help      |print this page
    -d    --debug     |Starts debugoutput
    -c    --config    |Set up configfile (uses file in playerroot instead)
    
Functions:
    -s    --sync      |Syncs rss feeds with the player (standard)
    -a    --add       |Add a new RSS feed
e.g: -a="http://ikhaya.ubuntuusers.de/feeds/full/20/,http://planet.ubuntuusers.de/feeds/full/20/"
Adds Ubuntuusers feed and planet feed.
    -r    --remove    |Removes one or more RSS Feed
e.g: -r="http://ikhaya.ubuntuusers.de/feeds/full/20/,http://planet.ubuntuusers.de/feeds/full/20/"
Deletes Ubuntuusers feed and planet feed.

Config:
    -t    --time      |Set timestamp format for new synced feeds
    -o    --old       |Use =delete to delete or store to store old entrys""")

def usage():
    print("""This is free software licensed under GnuGPLv3

This program was tested with Creative ZEN X-Fi2 Touch.
It should sync RSS feeds with it. Because **** Creative only provides Windows software.
Please use help to get more information about usage.
Use the README file, too.

I (Jonas Schwabe) would be happy if you like this software. :)

If you found bugs: jonas.schwabe@gmail.com
If you just want to ask me something use this address, too.
If you want to contribute, use it or fork on github.com""")
