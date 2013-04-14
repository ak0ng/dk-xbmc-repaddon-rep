import httplib
import urllib,urllib2,re,sys
import cookielib,os,string,cookielib,StringIO,gzip
import os,time,base64,logging
import xbmcaddon,xbmcplugin,xbmcgui
#from t0mm0.common.net import Net
import hashlib,random
import json
from t0mm0.common.addon import Addon

addon = Addon("plugin.video.MyDooTv")
datapath = addon.get_profile()
cookie_path = os.path.join(datapath, 'cookies')
strdomain ='www.mydootv.com'
strServerUrl=""
settingfilename= os.path.join(cookie_path, "setting.txt")
cookiefile= os.path.join(cookie_path, "cookiejar.lwp")
cj=None
def HOME():

    addDir('Search','/videos/categories',4,'')
    addLink('Login','/videos/categories',8,'','')
    addDir('Live Tv','/videos/categories',13,'')
    addDir('Cartoons ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=90',2,'')
    addDir('all thai drama ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=38,10,193,194,200,206,210,212',2,'')
    addDir('---thai on air ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=10',2,'')
    addDir('---thai drama 2013 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=215',2,'')
    addDir('---thai drama 2012 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=212',2,'')
    addDir('---thai drama 2011 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=210',2,'')
    addDir('---thai drama 2010 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=206',2,'')
    addDir('---thai drama 2009 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=193',2,'')
    addDir('---thai drama 2008 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=194',2,'')
    addDir('---thai drama classic ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=200',2,'')
    addDir('K-j series ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=40,213',2,'')
    addDir('chinese ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=121',2,'')
    addDir('all news ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=131,151,27',2,'')
    addDir('---breaking news  ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=131',2,'')
    addDir('---entertainment news ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=151',2,'')
    addDir('---news analysis ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=27',2,'')
    addDir('tv programs ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=125,126,127,132,185,152,129',2,'')
    addDir('---talk show ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=125',2,'')
    addDir('---variety show ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=126',2,'')
    addDir('---game shows ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=127',2,'')
    addDir('---food & health ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=132',2,'')
    addDir('---sports ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=185',2,'')
    addDir('---travel ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=152',2,'')
    addDir('---documentary ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=129',2,'')
    addDir('films ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=143,144',2,'')
    addDir('Music ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=146,147,148,149,202',2,'')
    addDir('Sitcom ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=16,97',2,'')
    addDir('Advertising ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=214',2,'')
    addDir('Contest ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=204',2,'')
    addDir('Study Language ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=136',2,'')
    addDir('Kids ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=139',2,'')
    addDir('Dhamma ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=203',2,'')
    addDir('Special Shows ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=159',2,'')
    addDir('Adult +18 ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=209',2,'')
    addDir('Coming soon ', 'http://www.mydootv.com/assets/services/newest_program_full_json.php?method=newest_program_expand&ch=&first=1&limit=260&cat=156',2,'')

  
def ShowLiveTV():
    addLink('TV 3 US Server','rtmp://02-live-12.dootvserver.com:80/uslive3/mp4:live3stream99 swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    #addLink('TV 3 UK Server','rtmp://01-live-01.dootvserver.com:80/uklive3/mp4:uklive3stream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('Sabaidee2 tv','rtmp://202.142.207.150/live/livesabaidee2 swfUrl=http://www.tv-tube.tv/tvchannels/watch/3364/sabaidee-tv swfVfy=true live=true http:http://www.tv-tube.tv/tvchannels/watch/3364/sabaidee-tv',14,'','')
    addLink('Sabaidee tv','rtmp://203.146.170.102:1935/live/livestream3 swfUrl=http://www.r-siam.com/player.swf/ swfVfy=true live=true',14,'','')
    addLink('Oho','rtmp://flash.login.in.th/ohochannel/ohochannel swfUrl=http://www.tv-tube.tv/players/jwflashplayer/player-5.9-licensed.swf swfVfy=true live=true pageUrl=http://www.tv-tube.tv/tvchannels/watch/3300/oho-channel',14,'','')
    addLink('MTV5','rtmp://203.146.170.102:1935/live/livestream2 swfUrl=http://fpdownload.adobe.com/strobe/FlashMediaPlayback.swf/[[DYNAMIC]]/1 swfVfy=true live=true pageUrl=http://mvtv.co.th/wp/tv.php?channel=mv5',14,'','')
    addLink('TV 5','rtmp://02-live-11.dootvserver.com:80/uslive5test/mp4:live5stream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('TV 7 ','rtmp://02-live-11.dootvserver.com:80/uslive7/mp4:live7stream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    #addLink('TV 7 UK Server','rtmp://01-live-01.dootvserver.com:80/uklive7/mp4:uklive7stream9 swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('TV 9 US Server','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_2SNwp7ygQ8cnXqsglDXw48_640_360_696 live=true',14,'','')
    addLink('NBT','rtmp://02-live-11.dootvserver.com:80/usliveNBT/mp4:usliveNBTstream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('TPBS','rtmp://02-live-11.dootvserver.com:80/usliveTPBS/mp4:usliveTPBSstream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('FAN TV','rtmp://02-live-12.dootvserver.com:80/usliveFanTV/mp4:usliveFanTVstream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
    addLink('Green Channel','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38__Scd02cLT7UgTueLpbeerY_640_360_700 live=true',14,'','')
    addLink('Acts Channel','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_08W_urLlRWAsogFHrCzJsw_640_360_700 live=true',14,'','')
    addLink('Bang Channel','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_ysf1M8xySnYonbbVTtF0oY_640_360_700 live=true',14,'','')
    addLink('Keera Channel','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_ghJ73vaoSgAhHoGi7IZ_uk_640_360_696 live=true',14,'','')
    addLink('Nation Channel','rtmp://llnwvps348.fc.llnwd.net:1935/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_UIpYjsh1QPAqASF_Lxww3I_640_360_700 live=true',14,'','')
    addLink('Miracle Channels','rtmpte://llnwvps348.fc.llnwd.net:80/llnwvps348/_definst_/Hmv0CG7hRxokmH9xKend38_hc9F6XfTTvcpokzyz8SUUY_640_360_700 live=true',14,'','')
    addLink('WorkPoint TV','rtmp://02-live-11.dootvserver.com:80/usliveWorkpoint/mp4:liveWorkpointstream swfUrl=http://www.mydootv.com/player_beta/flowplayer/flowplayer.commercial-3.2.15.swf?0.796194690678332 live=true',14,'','')
	

def SEARCH(url):
        keyb = xbmc.Keyboard('', 'Enter search text')
        keyb.doModal()
        searchText = ''
        if (keyb.isConfirmed()):
                searchText = urllib.quote_plus(keyb.getText())
        url = 'http://'+strdomain+'/assets/services/search_json.php?method=search&q='+urllib.quote_plus(searchText.encode('tis-620'))+'&first=1&limit=260'
        INDEX(url,"1")
        
def INDEX(url,name):
        data = GetJSON(url,"","",cj)
        imgsrc="http://cdn2.dootvimage.com/images/medium/"
        seriessrc="http://"+strdomain+"/assets/services/chapter_list_json.php?method=chapter_list&first=1&limit=350&pid="
        for product in data:
                urlfull=str(product["products_id"])
                fullimg=imgsrc+product["products_image"]
                addDir(product["products_name"],urlfull,3,fullimg)
				
def Episodesold(serverurl,pid):
    #try:
        link = GetContent("/products_list_option.php?pID="+pid+"&selectTab=first#first")
        link=''.join(link.splitlines()).replace('\'','"')
        partlist=re.compile('<a href="javascript\:playVideo\("(.+?)"\)">(.+?)</a>').findall(link)
        cnt = 0
        for (chid,vname) in partlist:
                cnt=cnt+1
                addLink(vname.decode("tis-620"),pid+"_"+str(cnt),3,"",serverurl.decode("tis-620"))
    #except: pass
                
def Episodes(pid):
        seriessrc="http://"+strdomain+"/assets/services/chapter_list_json.php?method=chapter_list&first=1&limit=350&pid="+pid
        try:
                data = GetJSON(seriessrc,"","",cj)
        except:
                data = GetJSON(seriessrc,"","",AutoLogin(cj))
        imgsrc="http://cdn2.dootvimage.com/images/medium/"
        for product in data:
                urlfull=str(product["chapters_id"])+"_"+str(product["products_id"])
                fullimg=imgsrc+product["products_image"]
                addDir(product["chapters_alter_name"],urlfull,7,fullimg)

            
    #except: pass
def GetJSON(url,data,referr,cj):
    if cj==None:
        cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #opener = urllib2.build_opener()
    opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Accept-Encoding','gzip, deflate'),
                         ('Referer', referr),
                         ('Content-Type', 'application/x-www-form-urlencoded'),
                         ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0'),
                         ('Connection','keep-alive'),
                         ('Accept-Language','en-us,en;q=0.5'),
                         ('Pragma','no-cache')]
    usock=opener.open(url,data)
    data = json.load(usock)
    usock.close()
    return data

def postContent(url,data,referr,cj):
    if cj==None:
        cj = cookielib.LWPCookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    #opener = urllib2.build_opener()
    opener.addheaders = [('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'),
                         ('Accept-Encoding','gzip, deflate'),
                         ('Referer', referr),
                         ('Content-Type', 'application/x-www-form-urlencoded'),
                         ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:13.0) Gecko/20100101 Firefox/13.0'),
                         ('Connection','keep-alive'),
                         ('Accept-Language','en-us,en;q=0.5'),
                         ('Pragma','no-cache')]
    usock=opener.open(url,data)
    if usock.info().get('Content-Encoding') == 'gzip':
           buf = StringIO.StringIO(usock.read())
           f = gzip.GzipFile(fileobj=buf)
           response= f.read()
    else:
           response= usock.read()
    usock.close()
    return (cj,response)

def GetVideoUrl(pid,cid):
        videourl="http://"+strdomain+"/assets/services/player_json.php?method=getVideoData&pid="+pid+"&cid="+cid+"&country=US"
        data = GetJSON(videourl,"","",cj)
        imgsrc="http://cdn2.dootvimage.com/images/medium/"
        for product in data:
                urlfull="http://"+product["hostname"]+".dootvserver.com"+product["uri_prefix"]
                fullimg=imgsrc+product["products_image"]
                addLink(product["chapters_alter_name"]+" SD",product["path"],14,fullimg,urlfull)
                if product["path_hd"]!=None and product["path_hd"]!="":
                        addLink(product["chapters_alter_name"]+" HD",product["path_hd"],14,fullimg,urlfull) 
						
def GetVideoFileName(chapterid,region):
        filecontent = GetContent("/player_flash_for_free.php?chapters_id="+chapterid+"&products_id=&ctLB="+region+"&is_hd=1&startVideo=false")
        nowhtsp= ''.join(filecontent.splitlines()).replace('\'','"')
        servname=re.compile('var serverName = "(.+?)"').findall(nowhtsp)[0]
        serurl="http://"+servname+".dootvserver.com"
        filenames=re.compile('if \(isHD == 0\) {        filepath = "(.+?)";    } else {        filepath = "(.+?)";        }').findall(nowhtsp)
        try:
            vidurl = filenames[0][0]
            addLink("Standard Quality",GenerateVideUrl(vidurl,serurl),14,"",serurl)
        except: pass
        try:
            vidurl = filenames[0][1]
            addLink("HD Quality",GenerateVideUrl(vidurl,serurl),14,"",serurl)
        except: pass
		
def GenerateVideUrl(url,serverurl):
    try:
        tempts=GetContent2(serverurl+"/flowplayer/sectimestamp.php").strip()
        tempkey="dootv-secret"
        m = hashlib.md5()
        m.update((((tempkey + "/") + url) + tempts))
        urlcode= serverurl+"/streaming/"+m.hexdigest() + "/" + tempts+"/"+url
        return urlcode
    except:
        d = xbmcgui.Dialog()
        d.ok('NO VIDEO FOUND', "Can't Play video",'Try a different Server Region')

def ChooseServerReg(pid):
        addDir("UK Servers","UK",pid,"")
        addDir("US Servers","US",pid,"")
		
def GetServerList(CountryFile,pid):
        listcontent = GetContent(CountryFile)
        servelist = listcontent.split()
        resul= "http://"+servelist[random.randint(1,len(servelist)-1)].split(":")[0]
        addDir("default Server",resul,pid,"")
        cnt = 0
        for servername in servelist:
                cnt=cnt+1
                addDir("Server " + str(cnt),"http://"+servername.split(":")[0]+"_1",pid,"")
		

def GetContent(url):
    conn = httplib.HTTPConnection(host=strdomain,timeout=30)
    req = url.replace('http://'+strdomain,'')
    try:
        conn.request('GET',req)
    except:
        print 'echec de connexion'
    content = conn.getresponse().read()
    conn.close()
    return content
	
def GetContent2(url):
  req = urllib2.Request(url)
  req.add_header('User-Agent','Mozilla/5.0 (Windows NT 5.1; rv:8.0) Gecko/20100101 Firefox/8.0')
  response = urllib2.urlopen(req)
  html=response.read()
  response.close()
  return html


def playVideo(serverurl,videourl):
    if serverurl!=None and serverurl!="": 
         newsecid = "http://"+strdomain+"/assets/services/get_new_secure_json.php?method=getNewSecure&path="+urllib.quote_plus(videourl)
         data = GetJSON(newsecid,"","",cj)
         fullurl = serverurl+data["md5"] +"/"+ data["t_hex"]+"/"+videourl
    else:
         fullurl=videourl

    xbmcPlayer = xbmc.Player()
    xbmcPlayer.play(fullurl)
def GetInput(strMessage,headtxt,ishidden):
    keyboard = xbmc.Keyboard("",strMessage,ishidden)
    keyboard.setHeading(headtxt) # optional
    keyboard.doModal()
    inputText=""
    if (keyboard.isConfirmed()):
        inputText = keyboard.getText()
    del keyboard
    return inputText

def getSettings(name,isencrypted):
    rtnvalue=None
    if os.path.isfile(settingfilename)!=False:
         f = open(settingfilename, "r")
         text = f.read()
         rtnvalue=re.compile('<'+name+'>(.+?)</'+name+'>', re.IGNORECASE).findall(text)
         if(len(rtnvalue) >0):
              rtnvalue=rtnvalue[0]
         else:
              rtnvalue=""
         if(isencrypted==True):
              rtnvalue=rtnvalue.decode('base-64')
    return rtnvalue
	
def setSettings(username,password,isencrypted):
    if(isencrypted==True):
         username=username.encode('base-64')
         password=password.encode('base-64')
    vfilecontent="<username>"+username.strip()+"</username><password>"+password.strip()+"</password>"
    f = open(settingfilename, 'w');f.write(vfilecontent);f.close()
	
def AutoLogin(cj):
      if not os.path.exists(datapath): os.makedirs(datapath)
      if not os.path.exists(cookie_path): os.makedirs(cookie_path)
      if cj==None:
           cj = cookielib.LWPCookieJar()
      strUsername=getSettings('username',True)
      strpwd=getSettings('password',True)
      if strUsername != None and strUsername !="" and strpwd != None and strpwd !="":
           (cj,respon)=postContent("http://"+strdomain+"/","EMail="+strUsername+"&Password="+strpwd+"&Rememberme=on","http://www.mydootv.com/",cj)
           cj.save(cookiefile, ignore_discard=True)
      cj.load(cookiefile,ignore_discard=True)
      return cj

def GetLoginCookie(cj,cookiefile):
      if not os.path.exists(datapath): os.makedirs(datapath)
      if not os.path.exists(cookie_path): os.makedirs(cookie_path)
      if cj==None:
           cj = cookielib.LWPCookieJar()
      strUsername=urllib.quote_plus(GetInput("Please enter your username","Username",False))
      if strUsername != None and strUsername !="":
           strpwd=urllib.quote_plus(GetInput("Please enter your password","Password",True))
           (cj,respon)=postContent("http://"+strdomain+"/","EMail="+strUsername+"&Password="+strpwd+"&Rememberme=on","http://www.mydootv.com/",cj)
           setSettings(strUsername,strpwd,True)
      cj.save(cookiefile, ignore_discard=True)
      cj=None
      cj = cookielib.LWPCookieJar()
      cj.load(cookiefile,ignore_discard=True)
      (cj,respon)=postContent("http://www.mydootv.com/video.php","","",cj)
      if (respon.find("player_content") == -1):
                d = xbmcgui.Dialog()
                d.ok("Incorrect Login","Login failed",'Try logging in again')
tmpUser=getSettings('username',False)
tmpPwd=getSettings('password',False)
if cj==None:
      cj = cookielib.LWPCookieJar()
if (tmpUser == None or tmpUser =="") and (tmpPwd == None or tmpPwd ==""):
      if os.path.isfile(cookiefile)==False:
                   GetLoginCookie(cj,cookiefile)
elif (tmpUser != None and tmpUser !="") and (tmpPwd != None and tmpPwd !="") and os.path.isfile(cookiefile)==False:
      AutoLogin(cj)

cj.load(cookiefile,ignore_discard=True)
                 #GetLoginCookie(cj,cookiefile)

def addLink(name,url,mode,iconimage,serverurl):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name.encode('tis-620'))+"&serverurl="+urllib.quote_plus(serverurl)
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        contextMenuItems = []
        liz.addContextMenuItems(contextMenuItems, replaceItems=True)
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz)
        return ok

def addDir(name,url,mode,iconimage):
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name.encode('tis-620'))
        ok=True
        liz=xbmcgui.ListItem(name, iconImage="DefaultVideo.png", thumbnailImage=iconimage)
        liz.setInfo( type="Video", infoLabels={ "Title": name } )
        ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]),url=u,listitem=liz,isFolder=True)
        return ok

def get_params():
        param=[]
        paramstring=sys.argv[2]
        if len(paramstring)>=2:
                params=sys.argv[2]
                cleanedparams=params.replace('?','')
                if (params[len(params)-1]=='/'):
                        params=params[0:len(params)-2]
                pairsofparams=cleanedparams.split('&')
                param={}
                for i in range(len(pairsofparams)):
                        splitparams={}
                        splitparams=pairsofparams[i].split('=')
                        if (len(splitparams))==2:
                                param[splitparams[0]]=splitparams[1]
                                
        return param    



params=get_params()
url=None
name=None
mode=None
serverurl=None
try:
        url=urllib.unquote_plus(params["url"])
except:
        pass
try:
        name=urllib.unquote_plus(params["name"])
except:
        pass
try:
        mode=int(params["mode"])
except:
        pass
try:
        serverurl=urllib.unquote_plus(params["serverurl"])
except:
        pass
		
sysarg=str(sys.argv[1]) 		
if mode==None or url==None or len(url)<1:
        #OtherContent()
        HOME()
       
elif mode==2:
        #d = xbmcgui.Dialog()
        #d.ok('mode 2',str(url),' ingore errors lol')
        INDEX(url,name)
elif mode==3:
        #chid,strRegion=url.split("_")
        #GetVideoFileName(chid,strRegion)
        Episodes(url)
elif mode==4:
        SEARCH(url)     
elif mode==6:
        ChooseServerReg(url)
elif mode==7:
        cid,pid=url.split("_")
        GetVideoUrl(pid,cid)
elif mode==8:
        GetLoginCookie(cj,cookiefile)
elif mode==9:
        GetServerList("/sorted_01_0111.txt",url)
elif mode==10:
        GetServerList("/sorted_01_0110.txt",url)
elif mode==11:
        GetServerList("/sorted_02_0112.txt",url)
elif mode==12:
        GetServerList("/sorted_01_0711.txt",url)
elif mode==13:
        ShowLiveTV()
elif mode==14:
        playVideo(serverurl,url)

	   
xbmcplugin.endOfDirectory(int(sysarg))
