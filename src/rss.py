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
from xml.dom import minidom
import urllib.request
import sys

'''
@return: tuple(Channelname, RssEnterys(Title, link, description, date)
'''
def getRssFeed(url):
    rssitems = []
    handler = urllib.request.urlopen(url)
    xmlfile = ""
    for i in handler:
        xmlfile += str(i.decode('iso-8859-1').encode().decode())
    print(xmlfile)
    xml = minidom.parseString(xmlfile.encode("iso-8859-1"))
    try:
        feed = xml.getElementsByTagName('feed')[0]
    except IndexError:
        try:
            feed = xml.getElementsByTagName('rdf:RDF')[0]
        except IndexError:
            print('Feed seems to be invalid or is not suported. Plase fill a bug report.')
            sys.exit(1)
    
    channel = feed.getElementsByTagName('title')[0].firstChild.data
    try:
        enterys = feed.getElementsByTagName('entry')
        enterys[0]
    except IndexError:
        try:
            enterys = feed.getElementsByTagName('item')
            enterys[0]
        except IndexError:
            print("Fatal: %s only does not contain entery OR iteam tags. If it is a valid RSS feed fill a bug report please.")
            sys.exit(1)
    for entery in enterys:
        try:
            title = entery.getElementsByTagName('title')[0].firstChild.data
        except AttributeError:
            title = ''
        except IndexError:
            title = ''
        try:
            link = entery.getElementsByTagName('link')[0].firstChild.data
        except AttributeError:
            link = ''
        except IndexError:
            link = ''
        try:
            description = entery.getElementsByTagName('description')[0].firstChild.data
        except AttributeError:
            description = ''
        except IndexError:
            description = ''
        try:
            date = entery.getElementsByTagName('pubdate')[0].firstChild.data
        except AttributeError:
            try:
                date = entery.getElementsByTagName('dc:date')[0].firstChild.data
            except AttributeError:
                date = ''
            except IndexError:
                date = ''
            date = ''
        except IndexError:
            try:
                date = entery.getElementsByTagName('dc:date')[0].firstChild.data
            except AttributeError:
                date = ''
            except IndexError:
                date = ''
            date = ''
        newentery = (title, link, description, date)
        rssitems.append(newentery)
    return (channel, rssitems)