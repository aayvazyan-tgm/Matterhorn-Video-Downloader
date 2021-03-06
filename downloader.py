#Author: Ari Ayvazyan
#Github: https://github.com/aayvazyan-tgm
#Downloads the raw video files from matterhorn for TU Wien. 
#You need to be connected via vpn or in the intranet to download a video.
import sys
import urllib.request
import webbrowser

if(len(sys.argv)!=2):
    inp= input("URL zum Vortrag eingeben: ")
else:
    inp=sys.argv[1]
id=inp[inp.find("id=")+3:]
xmlPageWithFlvLink = urllib.request.urlopen("https://mh-engage.ltcc.tuwien.ac.at/search/episode.xml?id="+id).read()

content = xmlPageWithFlvLink.decode('utf-8')
linkEnd = content.find(".flv")+4
linkStart = content[:linkEnd].rfind("http://")
linkStart2 = content[:linkEnd].rfind("https://")
if(linkStart<linkStart2):
    linkStart=linkStart2

todownload = content[linkStart:linkEnd]
print(todownload)
webbrowser.open(todownload)

