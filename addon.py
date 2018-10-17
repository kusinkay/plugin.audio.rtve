import urlparse
import xbmcaddon, xbmcgui, xbmcplugin, xbmc
import sys
from Rtve import *

def set_args():
    global handle
    global action
    global arg_id
    
    handle = int(sys.argv[1])
    if len(sys.argv)>2:
        auth_code =sys.argv[2]
    if len(sys.argv)>3:
        action =sys.argv[3]
    if len(sys.argv)>4:
        arg_id =sys.argv[4]


def log(msg, level=xbmc.LOGDEBUG):
    if REMOTE_DBG:
        xbmc.log("|| " + addonid + ": " + msg, level)

def channels():
    rtve = Rtve(Media.RADIO, base_url)

    for node in rtve.get_channels():
        xbmcplugin.addDirectoryItem(handle, node.url, node.listItem, True)
    
    xbmcplugin.endOfDirectory(handle)
    
def channel(chid):
    listItem = ListItem()
    listItem.setLabel("A - Z")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': Branch.PROGRAMS.value, 'arg_id': chid}, base_url), listItem, True)
    
    listItem = ListItem()
    listItem.setLabel("Popular")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': Branch.CHANNELS.value + '.' + Ranking.POPULAR.value, 'arg_id': chid}, base_url), listItem, True)
    
    listItem = ListItem()
    listItem.setLabel("Most seen")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': Branch.CHANNELS.value + '.' + Ranking.MOREVISITED.value, 'arg_id': chid}, base_url), listItem, True)
    
    xbmcplugin.endOfDirectory(handle)

def program(prid):
    listItem = ListItem()
    listItem.setLabel("A - Z")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': 'program.' + Ranking.RECENT.value , 'arg_id': prid}, base_url), listItem, True)
    
    listItem = ListItem()
    listItem.setLabel("Popular")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': Branch.PROGRAMS.value + '.' + Ranking.POPULAR.value, 'arg_id': prid}, base_url), listItem, True)
    
    listItem = ListItem()
    listItem.setLabel("Most seen")
    xbmcplugin.addDirectoryItem(handle, buildUrl({'action': Branch.PROGRAMS.value + '.' + Ranking.MOREVISITED.value, 'arg_id': prid}, base_url), listItem, True)
    
    xbmcplugin.endOfDirectory(handle)

def azprograms(chid):
    rtve = Rtve(Media.RADIO, base_url)
    for node in rtve.get_a_to_z(chid):
        xbmcplugin.addDirectoryItem(handle, node.url, node.listItem, True)
    
    xbmcplugin.endOfDirectory(handle)
    

def programs(channel, start = None, page = 1):
    rtve = Rtve(Media.RADIO, base_url)
    rtve.set_page(page)
    for node in rtve.get_programs(channel, start):
        xbmcplugin.addDirectoryItem(handle, node.url, node.listItem, True)
    
    xbmcplugin.endOfDirectory(handle)

def ranking(arg_id, branch, ranking, page):
    rtve = Rtve(Media.RADIO, base_url)
    rtve.set_page(page)
    args = {
        'id' : arg_id,
        'action': branch.value + '.' + ranking.value,
        'branch': branch,
        'ranking': ranking
    }
    log("ranking handle: " + str(handle))
    for node in rtve.get_audios(args):
        xbmcplugin.addDirectoryItem(handle, node.url, node.listItem, False)
    xbmcplugin.endOfDirectory(handle)

def play(handle, stream):
    listitem = ListItem(path=stream)
    return xbmcplugin.setResolvedUrl(handle=handle, succeeded=True, listitem=listitem) 
    
    
def test(program):
    
    line1 = "Hola, mon!"
    line2 = "Podriem escriure el que volguem, aqu&iacute;" + str(channel)
    line3 = "Usant python"
    
    xbmcgui.Dialog().ok(addonname, line1, line2, line3)

'''
B O D Y
B O D Y
B O D Y
'''

REMOTE_DBG = True
handle = None
action = None
arg_id = None
stream = None
page = 1
base_url = sys.argv[0]
args = urlparse.parse_qs(sys.argv[2][1:])

set_args()#from contextual menu

if len(args)>0:
    #handle = int(args.get('handle', None))
    action= args.get('action', None)
    if action <> None:
        action = str(action[0])
    arg_id = args.get('arg_id', None)
    if arg_id <> None:
        arg_id = str(arg_id[0])
    start = args.get('start', None)
    if start <> None:
        start = str(start[0])
    stream = args.get('stream', None)
    if stream <> None:
        stream = str(stream[0])
    page = args.get('page', None)
    if page <> None:
        page = str(page[0])
    else:
        page = 1

addon       = xbmcaddon.Addon()
addonpath   = addon.getAddonInfo('path')
addonpath   = xbmc.translatePath(addonpath).decode('utf-8')
addonname   = addon.getAddonInfo('name')
addonid     = addon.getAddonInfo('id')

if action==None:
    channels()
elif action=='channel':
    channel(arg_id)
elif action=='azprograms':
    azprograms(arg_id)
elif action==Branch.PROGRAMS.value:
    programs(arg_id, start, page)
elif action==Branch.CHANNELS.value + '.' + Ranking.POPULAR.value:
    ranking(arg_id, Branch.CHANNELS, Ranking.POPULAR, page)
elif action==Branch.CHANNELS.value + '.' + Ranking.MOREVISITED.value:
    ranking(arg_id, Branch.CHANNELS, Ranking.MOREVISITED, page)
elif action==Branch.PROGRAMS.value + '.' + Ranking.POPULAR.value:
    ranking(arg_id, Branch.PROGRAMS, Ranking.POPULAR, page)
elif action==Branch.PROGRAMS.value + '.' + Ranking.MOREVISITED.value:
    ranking(arg_id, Branch.PROGRAMS, Ranking.MOREVISITED, page)
elif action=='program':
    program(arg_id)
elif action=='program.' + Ranking.RECENT.value:
    ranking(arg_id, Branch.PROGRAMS, Ranking.RECENT, page)
elif action=='play':
    play(handle=handle, stream=stream)
else:
    test(program)



