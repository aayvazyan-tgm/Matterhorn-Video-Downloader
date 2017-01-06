import sys
import urllib.request
import webbrowser

id=sys.argv[1][sys.argv[1].find("id=")+3:]
xmlPageWithFlvLink = urllib.request.urlopen("https://mh-engage.ltcc.tuwien.ac.at/search/episode.xml?id="+id).read()

content = xmlPageWithFlvLink.decode('utf-8')
linkEnd = content.find(".flv")+4
linkStart = content[:linkEnd].rfind("https://")

todownload = content[linkStart:linkEnd]

webbrowser.open(todownload)

