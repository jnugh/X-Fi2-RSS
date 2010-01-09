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
import feedparser
import sys, os, string
'''
@return: tuple(Channelname, RssEnterys(Title, link, description, date)
'''
def getRssFeed(url, full):
    rssitems = []
    f = feedparser.parse(url)
    for entery in f['entries']:
        try:
            newentery = (str(entery.title.encode()), str(entery.link.encode()), str(entery.summary.encode()), str(entery.updated.encode()))
        except:
            try:
                newentery = (str(entery.title.encode()), str(entery.link.encode()), str(entery.subtitle.encode()), str(entery.updated.encode()))
            except:
                continue
        rssitems.append(newentery)
        print(newentery)
    return (f['feed']['title'].encode(), rssitems)

def syncall(config, root):
    valid_chars = "-_.() %s%s" % (string.ascii_letters, string.digits)
    num = config.get('Options', 'RSS Count')
    eof = int(num)
    try:
        os.chdir(root+'/RSS')
    except:
        try:
            os.mkdir(root+'/RSS')
            os.chdir(root+'/RSS')
        except:
            print('Unable to use RSS')
            sys.exit(1)
    for i in range(eof):
#        try:
            title = config.get('RSS_'+str(i), 'Title')
            print('Sync %s' % title)
            folder = config.get('RSS_'+str(i), 'Folder')
            url = config.get('RSS_'+str(i), 'URL')
            fullArticle = config.get('RSS_'+str(i), 'FullArticle')
            if(fullArticle == '0'):
                fullArticle = False
            else:
                fullArticle = True
            feed = getRssFeed(url, bool(fullArticle))
#        except:
#            print("Configfile does not exist or is invalid use fix to get it right (not implemented now)")
#            sys.exit(1)
            try:
                os.chdir(root+"/RSS/"+''.join(c for c in folder if c in valid_chars))
            except:
                try:
                    os.mkdir(root+"/RSS/"+''.join(c for c in folder if c in valid_chars))
                    os.chdir(root+"/RSS/"+''.join(c for c in folder if c in valid_chars))
                except:
                    print('Unable to use %s' % ''.join(c for c in folder if c in valid_chars))
                    sys.exit(1)
            for ent in feed[1]:
                #title, link, description, date
                print(root+"/RSS/"+''.join(c for c in folder if c in valid_chars)+"/"+''.join(c for c in ent[0] if c in valid_chars)+".xml")
                print(root+"/RSS/"+''.join(c for c in folder if c in valid_chars)+"/"+''.join(c for c in ent[0] if c in valid_chars)+".xml")
                f = open(root+"/RSS/"+''.join(c for c in folder if c in valid_chars)+"/"+''.join(c for c in ent[0] if c in valid_chars)+".xml", 'w')
                f.write("""﻿<?xml version='1.0' encoding='utf-8' ?>
<Rss>
<full_text>%s</full_text>
<creative_image count = "0">
</creative_image>
<channel>%s</channel>
<title>%s</title>
<link>%s</link>
<category></category>
<category></category>
<pubdate>%s</pubdate>
<description>
%s
</description>
</Rss>""" % (fullArticle, feed[0], ent[0], ent[1], ent[3], ent[2]))
                f.close()