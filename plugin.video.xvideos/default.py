#!/usr/bin/python
# -*- coding: latin-1 -*-


import xbmc,xbmcplugin
import xbmcgui
import sys
import urllib, urllib2
import time
import re
from htmlentitydefs import name2codepoint as n2cp
import httplib
import urlparse
from os import path, system
import socket
from urllib2 import Request, URLError, urlopen
from urlparse import parse_qs
from urllib import unquote_plus

pass#print  "Here in default-py sys.argv =", sys.argv

thisPlugin = int(sys.argv[1])
addonId = "plugin.video.xvideos"
dataPath = xbmc.translatePath('special://profile/addon_data/%s' % (addonId))
if not path.exists(dataPath):
       cmd = "mkdir -p " + dataPath
       system(cmd)
       
#Host = "http://www.sirina.tv/gallery/"
Host = "http://www.xvideos.com"

def getUrl(url):
        pass#print  "Here in getUrl url =", url
	req = urllib2.Request(url)
	req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3')
	response = urllib2.urlopen(req)
	link=response.read()
	response.close()
	return link
	

def showContent():
                names = []
                urls = []
                names.append("New Videos")
                names.append("Best Videos")
                urls.append("http://www.xvideos.com/new/")
                urls.append("http://www.xvideos.com/best/")
                i = 0
                pic = " "
                addDirectoryItem("Search", {"name":"Search", "url":Host, "mode":8}, pic)

                for name in names:
                        url1 = urls[i]
                        pic = " "
                        pass#print  "Here in Showcontent url1 =", url1
                        i = i+1
                        addDirectoryItem(name, {"name":name, "url":url1, "mode":1}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)

def getPage(name1, url):
                pages = [1, 2, 3, 4, 5, 6, 7, 8]
                for page in pages:
                        url1 = url + str(page) +"/"
                        name = "Page " + str(page)
                        pic = " "
                        if "Pornstars" in name1:
                                addDirectoryItem(name, {"name":name, "url":url1, "mode":4}, pic)
                        else:        
                                addDirectoryItem(name, {"name":name, "url":url1, "mode":2}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)

def getVideos(name1, urlmain):
	content = getUrl(urlmain)
	pass#print  "content B =", content
	regexvideo = 'div class="thumbBlock".*?a href="(.*?)".*?title="(.*?)"'
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print  "match =", match
        for url, name in match:
                 url1 = "http://www.xvideos.com" + url
                 name = name.replace('"', '')
                 pic = " "
                 #pass#print  "Here in getVideos url =", url
	         addDirectoryItem(name, {"name":name, "url":url1, "mode":3}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	         

def getVideos2(name1, urlmain):
	content = getUrl(urlmain)
	pass#print  "content C =", content
	regexvideo = 'flv_url=(.*?)&amp;'
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print  "match =", match
        for url in match:
               url = url.replace("%3A", ":")
               url = url.replace("%2F", "/")
               url = url.replace("%3F", "?")
               url = url.replace("%3D", "=")
               url = url.replace("%26", "&")
               pass#print  "Here in getvideos2 url =", url
               player = xbmc.Player()
               player.play(url)
               break	         

def getVideos3(name1, urlmain):
	content = getUrl(urlmain)
	pass#print  "content D =", content
	regexvideo = 'div class="thumbProfile".*?a href="(.*?)".*?a href=.*?>(.*?)<'
	match = re.compile(regexvideo,re.DOTALL).findall(content)
        pass#print  "match =", match
        for url, name in match:
                 url1 = "http://www.xvideos.com" + url
                 name = name.replace('"', '')
                 pic = " "
                 #pass#print  "Here in getVideos url =", url
	         addDirectoryItem(name, {"name":name, "url":url1, "mode":3}, pic)
        xbmcplugin.endOfDirectory(thisPlugin)	         	         

def search(name, url):
                      myfile = file(r"/tmp/xbmc_search.txt")       
                      icount = 0
                      for line in myfile.readlines(): 
                            stext = line
                            icount = icount+1
                            if icount > 0:
                                 break
                      stext = stext.replace(" ", "+")
                      pic = " "
                      name = stext
                      url = "http://www.xvideos.com/?k=" + stext
                      addDirectoryItem(name, {"name":name, "url":url, "mode":2}, pic)
                      xbmcplugin.endOfDirectory(thisPlugin)          
                                 
def getPageS(name, url):
                myfile = file(r"/tmp/xbmc_search.txt")       
                icount = 0
                for line in myfile.readlines(): 
                            stext = line
                            icount = icount+1
                            if icount > 0:
                                 break
                stext = stext.replace(" ", "+")
#                      pic = " "
#                      name = stext

                pages = [1, 2, 3, 4, 5, 6, 7, 8]
                for page in pages:
#                        url1 = url + "&page=" + str(page)
                        url1 = "http://www.xvideos.com/?k=" + stext + "&p=" + str(page)
                        name = "Page " + str(page) + " " + stext
                        pic = " "
                        addDirectoryItem(name, {"name":name, "url":url1, "mode":2}, pic)
                xbmcplugin.endOfDirectory(thisPlugin)

        
def playVideo(name, url):
           pass#print  "Here in playVideo Test url =", url
           content = getUrl(url)
	   pass#print  "content C =", content
	   regexvideo = 'div id="interstitialBtn.*?a href="(.*?)"'
	   match = re.compile(regexvideo,re.DOTALL).findall(content)
           pass#print  "match =", match[0]
           url1 = match[0] 
           pic = "DefaultFolder.png"
           #pass#print  "Here in playVideo Test url B=", url
           li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
           player = xbmc.Player()
           player.play(url1, li)

std_headers = {
	'User-Agent': 'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.6) Gecko/20100627 Firefox/3.6.6',
	'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-us,en;q=0.5',
}  

def addDirectoryItem(name, parameters={},pic=""):
    li = xbmcgui.ListItem(name,iconImage="DefaultFolder.png", thumbnailImage=pic)
    url = sys.argv[0] + '?' + urllib.urlencode(parameters)
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=url, listitem=li, isFolder=True)


def parameters_string_to_dict(parameters):
    ''' Convert parameters encoded in a URL to a dict. '''
    paramDict = {}
    if parameters:
        paramPairs = parameters[1:].split("&")
        for paramsPair in paramPairs:
            paramSplits = paramsPair.split('=')
            if (len(paramSplits)) == 2:
                paramDict[paramSplits[0]] = paramSplits[1]
    return paramDict

params = parameters_string_to_dict(sys.argv[2])
name =  str(params.get("name", ""))
url =  str(params.get("url", ""))
url = urllib.unquote(url)
mode =  str(params.get("mode", ""))

if not sys.argv[2]:
        pass#print  "Here in default-py going in showContent"
	ok = showContent()
else:
        if mode == str(1):
		ok = getPage(name, url)
	elif mode == str(2):
		ok = getVideos(name, url)                	
	elif mode == str(3):
		ok = getVideos2(name, url)	
	elif mode == str(4):
		ok = getVideos3(name, url)
	elif mode == str(6):
		ok = getVideos4(name, url)
	elif mode == str(7):
		ok = getVideos5(name, url)
#	elif mode == str(8):
#		ok = search(name, url)
	elif mode == str(8):
		ok = getPageS(name, url)	































