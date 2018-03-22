# -*- coding: utf-8 -*-
# Thanks For Tuhan YME
# Thanks for My TEAM Hello World
# Support by Alin
# Lib edition 0.9.3/Tanysyz
import HelloWorld
from HelloWorld.lib.Gen.ttypes import *
from datetime import datetime
from Helper.main import qr
from time import sleep
from bs4 import BeautifulSoup
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz
import wikipedia, urllib
from gtts import gTTS
from googletrans import Translator

botStart = time.time() 

cl = HelloWorld.LINE()
cl.login(token="Er4DIdlpVVFWXlle1vJ9.yUnazXTjcZ0bINB6Xni1cq.nAWY/yios0xjszsxrmBkzt6W9HQz+AO5XX1QY/d55Cc=")
cl.loginResult()

#cl = HelloWorld.LINE()
#cl.login("EMAILMU","PASSWORD")
#cl.loginResult()

#cl = HelloWorld.LINE()
#cl.login(token="tokenmu")
#cl.loginResult()

print "[    Login Success    ]"
reload(sys)
sys.setdefaultencoding('utf-8')
mid = cl.getProfile().mid
key = {
    "keyCommand":".",
}

message = {
    "replyPesan":"Jangan tag-tag, tag itu berat. Mending pc mesra aja",
}

settings = {
    "autoJoin":False,
    "autoAdd":False,
    "autoRead":False,
    "autoLeaveRoom":False,
    "checkContact":False,
    "checkPost":False,
    "responMention":True,
    "simiSimi":{},
	"userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
	],
}
    
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}

mimic = {
    "copy":False,
    "status":False,
    "target":{}
    }
    
setTime = {}
setTime = read['readTime']

contact = cl.getProfile()
restoreprofile = cl.getProfile()
restoreprofile.displayName = contact.displayName
restoreprofile.statusMessage = contact.statusMessage                        
restoreprofile.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:   
        import urllib,request   
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                     
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)    
            time.sleep(0.1)   
            page = page[end_content:]
    return items

def mentionMembers(to, name):
    tag = ""
    tag2 = ""
    start = int(0)
    finish = int(0)
    if "u62e340671b490b3d018a76fac4d23509" in name:
        name.remove("u62e340671b490b3d018a76fac4d23509")
    # Example untuk bot
    # for bot in Bots:
    #     if bot in name:
    #         name.remove(bot)
    for md in name:
        finish = finish + 3
        tag += """{"S":"""+json.dumps(str(start))+""","E":"""+json.dumps(str(finish))+""","M":"""+json.dumps(md)+"},"""
        start = start + 4
        finish = finish + 1
        tag2 += "@x \n"
    tag = (tag[:int(len(tag)-1)])
    msg = Message()
    msg.to = to
    msg.from_ = jendralMID
    msg.text = tag2
    msg.contentMetadata = {'MENTION':'{"MENTIONEES"😞'+tag+']}','EMTVER':'4'}
    try:
        jendral.sendMessage(msg)
    except Exception as error:
        print error
    print "[NOTIFIED_MENTION_USER]"
    
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)     

#==============================================================================#
#==============================================================================#
#==============================================================================#
def helpmessage():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpMessage =        "╔══[ H E L P   M E S S A G E ]" + "\n" + \
                         "╠ Self" + "\n" + \
                         "╠ Group" + "\n" + \
                         "╠ Translate" + "\n" + \
                         "╠ TextToSpeech" + "\n" + \
                         "╠ Media" + "\n" + \
                         "╠ Settings" + "\n" + \
                         "╠══[ K E Y    M E S S A G E ]" + "\n" + \
                         "╠ Mykey" + "\n" + \
                         "╠ ChangeKey:" + "\n" + \
                         "╚══[ Jangan Typo ]"
    return helpMessage
    
def myself():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    Myself =           "╔══[ H E L P   S E L F ]" + "\n" + \
                         "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                         "╠ " + mykey + "Crash" + "\n" + \
                         "╠ " + mykey + "Me" + "\n" + \
                         "╠ " + mykey + "ChangeName:" + "\n" + \
                         "╠ " + mykey + "ChangeBio:" + "\n" + \
                         "╠ " + mykey + "MyMid" + "\n" + \
                         "╠ " + mykey + "MyName" + "\n" + \
                         "╠ " + mykey + "MyBio" + "\n" + \
                         "╠ " + mykey + "MyPicture" + "\n" + \
                         "╠ " + mykey + "MyCover" + "\n" + \
                         "╠ " + mykey + "StealMid" + "\n" + \
                         "╠ " + mykey + "StealName" + "\n" + \
                         "╠ " + mykey + "StealBio" + "\n" + \
                         "╠ " + mykey + "StealPicture" + "\n" + \
                         "╠ " + mykey + "StealCover" + "\n" + \
                         "╠ " + mykey + "StealContact" + "\n" + \
                         "╠ " + mykey + "CloneProfile" + "\n" + \
                         "╠ " + mykey + "RestoreProfile" + "\n" + \
                         "╠ " + mykey + "CheckMid:" + "\n" + \
                         "╠ " + mykey + "FriendList" + "\n" + \
                         "╠ " + mykey + "BlockList" + "\n" + \
                         "╠ " + mykey + "Gbroadcast" + "\n" + \
                         "╠ " + mykey + "Fbroadcast" + "\n" + \
                         "╠ " + mykey + "Allbroadcast" + "\n" + \
                         "╚══[ Jangan Typo ]"
    return Myself
    
def helpgroup():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpGroup =          "╔══[ H E L P   G R O U P ]" + "\n" + \
                         "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                         "╠ " + mykey + "ChangeGroupName:" + "\n" + \
                         "╠ " + mykey + "GroupCreator" + "\n" + \
                         "╠ " + mykey + "GroupList" + "\n" + \
                         "╠ " + mykey + "DetailsGroup" + "\n" + \
                         "╠ " + mykey + "MemberList" + "\n" + \
                         "╠ " + mykey + "GroupPicture" + "\n" + \
                         "╠ " + mykey + "GroupName" + "\n" + \
                         "╠ " + mykey + "GroupId" + "\n" + \
                         "╠ " + mykey + "GroupTicket" + "\n" + \
                         "╠ " + mykey + "OpenQR" + "\n" + \
                         "╠ " + mykey + "CloseQR" + "\n" + \
                         "╠══[ S P E C I A L    G R O U P ]" + "\n" + \
                         "╠ " + mykey + "Mention" + "\n" + \
                         "╠ " + mykey + "Lurking On/Off" + "\n" + \
                         "╠ " + mykey + "Lurking Reset" + "\n" + \
                         "╠ " + mykey + "Lurking" + "\n" + \
                         "╠ " + mykey + "Kick" + "\n" + \
                         "╠ " + mykey + "Ulti" + "\n" + \
                         "╠ " + mykey + "Cancel" + "\n" + \
                         "╚══[ Jangan Typo ]"
    return helpGroup
    
def helpsettings():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpSettings =       "╔══[ H E L P   S E T T I N G S ]" + "\n" + \
                         "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                         "╠ " + mykey + "AutoAdd On/Off:" + "\n" + \
                         "╠ " + mykey + "AutoJoin On/Off:" + "\n" + \
                         "╠ " + mykey + "AutoLeaveRoom On/Off:" + "\n" + \
                         "╠ " + mykey + "AutoRead On/Off:" + "\n" + \
                         "╠ " + mykey + "AutoRespon On/Off:" + "\n" + \
                         "╠ " + mykey + "CheckContact On/Off:" + "\n" + \
                         "╠ " + mykey + "CheckPost On/Off:" + "\n" + \
                         "╠ " + mykey + "Simisimi On/Off:" + "\n" + \
                         "╠══[ M E S S A G E ]" + "\n" + \
                         "╠ " + mykey + "AutoRespon" + "\n" + \
                         "╠ " + mykey + "AutoRespon:" + "\n" + \
                         "╠══[ S T A T U S   M E S S A G E ]" + "\n" + \
                         "╠ " + mykey + "Status" + "\n" + \
                         "╠ " + mykey + "Speed" + "\n" + \
                         "╠ " + mykey + "Runtime" + "\n" + \
                         "╠ " + mykey + "Restart" + "\n" + \
                         "╚══[ Jangan Typo ]"
    return helpSettings
    
def helpmedia():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpMedia =          "╔══[ H E L P   M E D I A ]" + "\n" + \
                         "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                         "╠ " + mykey + "Kalender" + "\n" + \
                         "╠ " + mykey + "CheckDate" + "\n" + \
                         "╠ " + mykey + "YoutubeSearch" + "\n" + \
                         "╠ " + mykey + "ImageSearch" + "\n" + \
                         "╠ " + mykey + "Wikipedia" + "\n" + \
                         "╠ " + mykey + "Music" + "\n" + \
                         "╠ " + mykey + "Lyric" + "\n" + \
                         "╠ " + mykey + "ProfileIg" + "\n" + \
                         "╠ " + mykey + "Idline" + "\n" + \
                         "╠ " + mykey + "Prankcall" + "\n" + \
                         "╠ " + mykey + "Snapgram" + "\n" + \
                         "╚══[ Jangan Typo ]"
    return helpMedia
    
def helptexttospeech():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpTextToSpeech =   "╔══[ T E X T   T O   S P E E C H ]" + "\n" + \
                         "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                         "╠ " + mykey + "af : Afrikaans" + "\n" + \
                         "╠ " + mykey + "sq : Albanian" + "\n" + \
                         "╠ " + mykey + "ar : Arabic" + "\n" + \
                         "╠ " + mykey + "hy : Armenian" + "\n" + \
                         "╠ " + mykey + "bn : Bengali" + "\n" + \
                         "╠ " + mykey + "ca : Catalan" + "\n" + \
                         "╠ " + mykey + "zh : Chinese" + "\n" + \
                         "╠ " + mykey + "zh-cn : Chinese (Mandarin/China)" + "\n" + \
                         "╠ " + mykey + "zh-tw : Chinese (Mandarin/Taiwan)" + "\n" + \
                         "╠ " + mykey + "zh-yue : Chinese (Cantonese)" + "\n" + \
                         "╠ " + mykey + "hr : Croatian" + "\n" + \
                         "╠ " + mykey + "cs : Czech" + "\n" + \
                         "╠ " + mykey + "da : Danish" + "\n" + \
                         "╠ " + mykey + "nl : Dutch" + "\n" + \
                         "╠ " + mykey + "en : English" + "\n" + \
                         "╠ " + mykey + "en-au : English (Australia)" + "\n" + \
                         "╠ " + mykey + "en-uk : English (United Kingdom)" + "\n" + \
                         "╠ " + mykey + "en-us : English (United States)" + "\n" + \
                         "╠ " + mykey + "eo : Esperanto" + "\n" + \
                         "╠ " + mykey + "fi : Finnish" + "\n" + \
                         "╠ " + mykey + "fr : French" + "\n" + \
                         "╠ " + mykey + "de : German" + "\n" + \
                         "╠ " + mykey + "el : Greek" + "\n" + \
                         "╠ " + mykey + "hi : Hindi" + "\n" + \
                         "╠ " + mykey + "hu : Hungarian" + "\n" + \
                         "╠ " + mykey + "is : Icelandic" + "\n" + \
                         "╠ " + mykey + "id : Indonesian" + "\n" + \
                         "╠ " + mykey + "it : Italian" + "\n" + \
                         "╠ " + mykey + "ja : Japanese" + "\n" + \
                         "╠ " + mykey + "km : Khmer (Cambodian)" + "\n" + \
                         "╠ " + mykey + "ko : Korean" + "\n" + \
                         "╠ " + mykey + "la : Latin" + "\n" + \
                         "╠ " + mykey + "lv : Latvian" + "\n" + \
                         "╠ " + mykey + "mk : Macedonian" + "\n" + \
                         "╠ " + mykey + "no : Norwegian" + "\n" + \
                         "╠ " + mykey + "pl : Polish" + "\n" + \
                         "╠ " + mykey + "pt : Portuguese" + "\n" + \
                         "╠ " + mykey + "ro : Romanian" + "\n" + \
                         "╠ " + mykey + "ru : Russian" + "\n" + \
                         "╠ " + mykey + "sr : Serbian" + "\n" + \
                         "╠ " + mykey + "si : Sinhala" + "\n" + \
                         "╠ " + mykey + "sk : Slovak" + "\n" + \
                         "╠ " + mykey + "es : Spanish" + "\n" + \
                         "╠ " + mykey + "es-es : Spanish (Spain)" + "\n" + \
                         "╠ " + mykey + "es-us : Spanish (United States)" + "\n" + \
                         "╠ " + mykey + "sw : Swahili" + "\n" + \
                         "╠ " + mykey + "sv : Swedish" + "\n" + \
                         "╠ " + mykey + "ta : Tamil" + "\n" + \
                         "╠ " + mykey + "th : Thai" + "\n" + \
                         "╠ " + mykey + "tr : Turkish" + "\n" + \
                         "╠ " + mykey + "uk : Ukrainian" + "\n" + \
                         "╠ " + mykey + "vi : Vietnamese" + "\n" + \
                         "╠ " + mykey + "cy : Welsh" + "\n" + \
                         "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                          "Contoh : " + mykey + "say-id Alin Jelek"
    return helpTextToSpeech
    
    
def helptranslate():
    mykey = key["keyCommand"]
    mykey = mykey.title()
    helpTranslate =    "╔══[ T R A N S L A T E ]" + "\n" + \
                       "╠ Use [" + mykey + "] for the Prefix" + "\n" + \
                       "╠ " + mykey + "af : afrikaans" + "\n" + \
                       "╠ " + mykey + "sq : albanian" + "\n" + \
                       "╠ " + mykey + "am : amharic" + "\n" + \
                       "╠ " + mykey + "ar : arabic" + "\n" + \
                       "╠ " + mykey + "hy : armenian" + "\n" + \
                       "╠ " + mykey + "az : azerbaijani" + "\n" + \
                       "╠ " + mykey + "eu : basque" + "\n" + \
                       "╠ " + mykey + "be : belarusian" + "\n" + \
                       "╠ " + mykey + "bn : bengali" + "\n" + \
                       "╠ " + mykey + "bs : bosnian" + "\n" + \
                       "╠ " + mykey + "bg : bulgarian" + "\n" + \
                       "╠ " + mykey + "ca : catalan" + "\n" + \
                       "╠ " + mykey + "ceb : cebuano" + "\n" + \
                       "╠ " + mykey + "ny : chichewa" + "\n" + \
                       "╠ " + mykey + "zh-cn : chinese (simplified)" + "\n" + \
                       "╠ " + mykey + "zh-tw : chinese (traditional)" + "\n" + \
                       "╠ " + mykey + "co : corsican" + "\n" + \
                       "╠ " + mykey + "hr : croatian" + "\n" + \
                       "╠ " + mykey + "cs : czech" + "\n" + \
                       "╠ " + mykey + "da : danish" + "\n" + \
                       "╠ " + mykey + "nl : dutch" + "\n" + \
                       "╠ " + mykey + "en : english" + "\n" + \
                       "╠ " + mykey + "eo : esperanto" + "\n" + \
                       "╠ " + mykey + "et : estonian" + "\n" + \
                       "╠ " + mykey + "tl : filipino" + "\n" + \
                       "╠ " + mykey + "fi : finnish" + "\n" + \
                       "╠ " + mykey + "fr : french" + "\n" + \
                       "╠ " + mykey + "fy : frisian" + "\n" + \
                       "╠ " + mykey + "gl : galician" + "\n" + \
                       "╠ " + mykey + "ka : georgian" + "\n" + \
                       "╠ " + mykey + "de : german" + "\n" + \
                       "╠ " + mykey + "el : greek" + "\n" + \
                       "╠ " + mykey + "gu : gujarati" + "\n" + \
                       "╠ " + mykey + "ht : haitian creole" + "\n" + \
                       "╠ " + mykey + "ha : hausa" + "\n" + \
                       "╠ " + mykey + "haw : hawaiian" + "\n" + \
                       "╠ " + mykey + "iw : hebrew" + "\n" + \
                       "╠ " + mykey + "hi : hindi" + "\n" + \
                       "╠ " + mykey + "hmn : hmong" + "\n" + \
                       "╠ " + mykey + "hu : hungarian" + "\n" + \
                       "╠ " + mykey + "is : icelandic" + "\n" + \
                       "╠ " + mykey + "ig : igbo" + "\n" + \
                       "╠ " + mykey + "id : indonesian" + "\n" + \
                       "╠ " + mykey + "ga : irish" + "\n" + \
                       "╠ " + mykey + "it : italian" + "\n" + \
                       "╠ " + mykey + "ja : japanese" + "\n" + \
                       "╠ " + mykey + "jw : javanese" + "\n" + \
                       "╠ " + mykey + "kn : kannada" + "\n" + \
                       "╠ " + mykey + "kk : kazakh" + "\n" + \
                       "╠ " + mykey + "km : khmer" + "\n" + \
                       "╠ " + mykey + "ko : korean" + "\n" + \
                       "╠ " + mykey + "ku : kurdish (kurmanji)" + "\n" + \
                       "╠ " + mykey + "ky : kyrgyz" + "\n" + \
                       "╠ " + mykey + "lo : lao" + "\n" + \
                       "╠ " + mykey + "la : latin" + "\n" + \
                       "╠ " + mykey + "lv : latvian" + "\n" + \
                       "╠ " + mykey + "lt : lithuanian" + "\n" + \
                       "╠ " + mykey + "lb : luxembourgish" + "\n" + \
                       "╠ " + mykey + "mk : macedonian" + "\n" + \
                       "╠ " + mykey + "mg : malagasy" + "\n" + \
                       "╠ " + mykey + "ms : malay" + "\n" + \
                       "╠ " + mykey + "ml : malayalam" + "\n" + \
                       "╠ " + mykey + "mt : maltese" + "\n" + \
                       "╠ " + mykey + "mi : maori" + "\n" + \
                       "╠ " + mykey + "mr : marathi" + "\n" + \
                       "╠ " + mykey + "mn : mongolian" + "\n" + \
                       "╠ " + mykey + "my : myanmar (burmese)" + "\n" + \
                       "╠ " + mykey + "ne : nepali" + "\n" + \
                       "╠ " + mykey + "no : norwegian" + "\n" + \
                       "╠ " + mykey + "ps : pashto" + "\n" + \
                       "╠ " + mykey + "fa : persian" + "\n" + \
                       "╠ " + mykey + "pl : polish" + "\n" + \
                       "╠ " + mykey + "pt : portuguese" + "\n" + \
                       "╠ " + mykey + "pa : punjabi" + "\n" + \
                       "╠ " + mykey + "ro : romanian" + "\n" + \
                       "╠ " + mykey + "ru : russian" + "\n" + \
                       "╠ " + mykey + "sm : samoan" + "\n" + \
                       "╠ " + mykey + "gd : scots gaelic" + "\n" + \
                       "╠ " + mykey + "sr : serbian" + "\n" + \
                       "╠ " + mykey + "st : sesotho" + "\n" + \
                       "╠ " + mykey + "sn : shona" + "\n" + \
                       "╠ " + mykey + "sd : sindhi" + "\n" + \
                       "╠ " + mykey + "si : sinhala" + "\n" + \
                       "╠ " + mykey + "sk : slovak" + "\n" + \
                       "╠ " + mykey + "sl : slovenian" + "\n" + \
                       "╠ " + mykey + "so : somali" + "\n" + \
                       "╠ " + mykey + "es : spanish" + "\n" + \
                       "╠ " + mykey + "su : sundanese" + "\n" + \
                       "╠ " + mykey + "sw : swahili" + "\n" + \
                       "╠ " + mykey + "sv : swedish" + "\n" + \
                       "╠ " + mykey + "tg : tajik" + "\n" + \
                       "╠ " + mykey + "ta : tamil" + "\n" + \
                       "╠ " + mykey + "te : telugu" + "\n" + \
                       "╠ " + mykey + "th : thai" + "\n" + \
                       "╠ " + mykey + "tr : turkish" + "\n" + \
                       "╠ " + mykey + "uk : ukrainian" + "\n" + \
                       "╠ " + mykey + "ur : urdu" + "\n" + \
                       "╠ " + mykey + "uz : uzbek" + "\n" + \
                       "╠ " + mykey + "vi : vietnamese" + "\n" + \
                       "╠ " + mykey + "cy : welsh" + "\n" + \
                       "╠ " + mykey + "xh : xhosa" + "\n" + \
                       "╠ " + mykey + "yi : yiddish" + "\n" + \
                       "╠ " + mykey + "yo : yoruba" + "\n" + \
                       "╠ " + mykey + "zu : zulu" + "\n" + \
                       "╠ " + mykey + "fil : Filipino" + "\n" + \
                       "╠ " + mykey + "he : Hebrew" + "\n" + \
                       "╚══[ Jangan Typo ]" + "\n" + "\n\n" + \
                         "Contoh : " + mykey + "tr-id khie manis"
    return helpTranslate
#==============================================================================#
#==============================================================================#
#==============================================================================#
def bot(op):
    try:
        if op.type == 0:
            return
#==============================================================================#
#==============================================================================#
#==============================================================================# 
        if op.type == 5:
            if settings["autoAdd"] == True: 
                cl.findAndAddContactsByMid(op.param1)
                xname = cl.getContact(op.param1).displayName
                cl.sendText(op.param1, "Halo " + xname + " ,terimakasih telah menambahkan saya sebagai teman :3")
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if settings["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
        if op.type == 22:
            if settings["autoLeaveRoom"] == True:
                cl.sendText(op.param1, "Goblok ngapain invite gw")
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if settings["autoLeaveRoom"] == True:
                cl.sendText(op.param1, "Goblok ngapain invite gw")
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
                if settings["checkContact"] == True:
                    try:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        cover = cl.channel.getCover(msg.contentMetadata["mid"]) 
                        path = "http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        try:
                            cl.sendImageWithURL(msg.to, str(path))
                        except:
                            pass
                        ret_ = "╔══[ Details Contact ]"
                        ret_ += "\n╠ Nama : {}".format(str(contact.displayName))
                        ret_ += "\n╠ MID : {}".format(str(msg.contentMetadata["mid"]))
                        ret_ += "\n╠ Bio : {}".format(str(contact.statusMessage))
                        ret_ += "\n╠ Gambar Profile : http://dl.profile.line-cdn.net/{}".format(str(contact.pictureStatus))
                        ret_ += "\n╠ Gambar Cover : {}".format(str(cover))
                        ret_ += "\n╚══[ Finish ]"
                        cl.sendText(msg.to, str(ret_))
                    except:
                        cl.sendText(msg.to, "Kontak tidak valid")
            if msg.contentType == 16:
                if wait["checkPost"] == True:
                    msg.contentType = 0
                    msg.text = "URL : \n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            if 'MENTION' in msg.contentMetadata.keys()!=None:
                 if settings["responMention"] == True:
                    names = re.findall(r'@(\w+)',msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in mid:
                            xname = cl.getContact(msg.from_).displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            balas = "@" + xname + " " + str(message["replyPesan"])
                            msg.text = balas
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)
            if settings["autoRead"] == True:
                cl.sendChatChecked(to, msg_id)
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, data['result']['response'].encode('utf-8'))
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
#==============================================================================#
#==============================================================================#
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                return            
            if msg.contentType == 16:
                if wait["checkPost"] == True:
                    msg.contentType = 0
                    msg.text = "URL : \n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)


#==============================================================================#
#==============================================================================#
#==============================================================================#
            if msg.contentType == 0:
                if msg.text == None:
                    return
                elif msg.text.lower() == "mykey":
                    cl.sendText(msg.to, "My Set Keyword :「" + str(key["keyCommand"]) + "」")
                    
                elif msg.text.lower() == "changekey:":
                    sep = msg.text.split(" ")
                    key["keyCommand"] = msg.text.replace(sep[0] + " ","")
                    cl.sendText(msg.to,"Set Key changed to :「" + str(key["keyCommand"]) + "」")  
                    
                elif msg.text.lower() == "help":
                    helpMessage = helpmessage()
                    cl.sendText(msg.to, str(helpMessage)) 
                    
                elif msg.text.lower() == "settings":
                    helpSettings = helpsettings()
                    cl.sendText(msg.to, str(helpSettings)) 
                    
                elif msg.text.lower() == "self":
                    Myself = myself()
                    cl.sendText(msg.to, str(Myself))
                    
                elif msg.text.lower() == "group":
                    helpGroup = helpgroup()
                    cl.sendText(msg.to, str(helpGroup))
                    
                elif msg.text.lower() == "media":
                    helpMedia = helpmedia()
                    cl.sendText(msg.to, str(helpMedia))
                    
                elif msg.text.lower() == "translate":
                    helpTranslate = helptranslate()
                    cl.sendText(msg.to, str(helpTranslate))
                    
                elif msg.text.lower() == "texttospeech":
                    helpTextToSpeech = helptexttospeech()
                    cl.sendText(msg.to, str(helpTextToSpeech))
                    
                elif msg.text.lower() == key["keyCommand"]+'speed':
                    start = time.time()
                    cl.sendText(msg.to, "Benchmarking...")
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to, "%sseconds" % (elapsed_time))
                    
                elif msg.text.lower() == key["keyCommand"]+'restart':
                    cl.sendText(msg.to, "Bot Program has been restarted")
                    restart_program()
                        
                elif msg.text.lower() == key["keyCommand"]+'runtime':
                    eltime = time.time() - botStart
                    runtime = "Runtime\nTime: "+ waktu(eltime)
                    cl.sendText(msg.to, runtime)
    #==============================================================================#
    #================================ SELF PROFILE ================================#
    #==============================================================================#
                elif msg.text.lower() == key["keyCommand"]+'me':
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': mid}
                    cl.sendMessage(msg)
                    xname = cl.getProfile().displayName
                    xlen = str(len(xname)+1)
                    msg.contentType = 0
                    msg.text = "@"+xname+ ""
                    msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                    cl.sendMessage(msg)
                elif msg.text.lower().startswith(key["keyCommand"]+"changename:"):
                    sep = msg.text.split(" ")
                    string = msg.text.replace(sep[0] + " ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.displayName = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Changed " + string + "")
                elif msg.text.lower().startswith(key["keyCommand"]+"changebio:"):
                    sep = msg.text.split(" ")
                    string = msg.text.replace(sep[0] + " ","")
                    if len(string.decode('utf-8')) <= 20:
                        profile = cl.getProfile()
                        profile.statusMessage = string
                        cl.updateProfile(profile)
                        cl.sendText(msg.to,"Changed " + string)
                elif msg.text.lower() == key["keyCommand"]+'mymid':
                    cl.sendText(msg.to, mid)
                elif msg.text.lower() == key["keyCommand"]+'myname':
                        me = cl.getContact(mid)
                        cl.sendText(msg.to,"[DisplayName]\n" + me.displayName)
                elif msg.text.lower() == key["keyCommand"]+'mybio':
                        me = cl.getContact(mid)
                        cl.sendText(msg.to,"[StatusMessage]\n" + me.statusMessage)
                elif msg.text.lower() == key["keyCommand"]+'mypicture':
                        me = cl.getContact(mid)
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
                elif msg.text.lower() == key["keyCommand"]+'mycover':
                        me = cl.getContact(mid)
                        cover = cl.channel.getCover(mid)          
                        path = str(cover)
                        cl.sendImageWithURL(msg.to, path)
                elif msg.text.lower().startswith(key["keyCommand"]+"stealmid"):
                    sep = msg.text.split(" ")
                    _name = msg.text.replace(sep[0] + " @","")
                    _nametarget = _name.rstrip(' ')
                    gs = cl.getGroup(msg.to)
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            cl.sendText(msg.to, g.mid)
                elif msg.text.lower().startswith(key["keyCommand"]+"stealname"):
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    try:
                        cl.sendText(msg.to, "[ StatusMessage ]\n" + contact.displayName)
                    except:
                        pass
                elif msg.text.lower().startswith(key["keyCommand"]+"stealbio"):
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    try:
                        cl.sendText(msg.to, "[ StatusMessage ]\n" + contact.statusMessage)
                    except:
                        pass
                elif msg.text.lower().startswith(key["keyCommand"]+"stealpicture"):
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    try:
                        cl.sendImageWithURL(msg.to,image)
                    except:
                        pass
                elif msg.text.lower().startswith(key["keyCommand"]+"stealcover"):
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    cu = cl.channel.getCover(mention1)
                    path = str(cu)
                    try:
                        cl.sendImageWithURL(msg.to,path)
                    except:
                        pass
                elif msg.text.lower().startswith(key["keyCommand"]+"stealcontact"):
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]                
                    mmid = cl.getContact(mention1)
                    msg.contentType = 13
                    msg.contentMetadata = {"mid": mention1}
                    cl.sendMessage(msg)
                elif msg.text.lower().startswith(key["keyCommand"]+"cloneprofile"):
                       sep = msg.text.split(" ")
                       _name = msg.text.replace(sep[0] + " @","")
                       _nametarget = _name.rstrip('  ')
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for g in gs.members:
                           if _nametarget == g.displayName:
                               targets.append(g.mid)
                       if targets == []:
                           cl.sendText(msg.to, "Not Found...")
                       else:
                           for target in targets:
                                try:
                                   cl.CloneContactProfile(target)
                                   cl.sendText(msg.to, "Success Clone Profile")
                                except Exception as e:
                                    print e
                elif msg.text.lower() == key["keyCommand"]+'restoreprofile':
                    try:
                        cl.updateDisplayPicture(restoreprofile.pictureStatus)
                        cl.updateProfile(restoreprofile)
                        cl.sendText(msg.to, "Success Restore Profile")
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
                
                elif msg.text.lower().startswith(key["keyCommand"]+"checkmid:"):
                    separate = msg.text.split(" ")
                    saya = msg.text.replace(separate[0] + " ","")
                    msg.contentType = 13
                    msg.contentMetadata = {"mid":saya}
                    cl.sendMessage(msg)
                    
                elif msg.text.lower() == key["keyCommand"]+'friendlist':
                    contactlist = cl.getAllContactIds()
                    kontak = cl.getContacts(contactlist)
                    num=1
                    msgs="═════════List Friend═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
                elif msg.text.lower() == key["keyCommand"]+'blocklist':
                    blockedlist = cl.getBlockedContactIds()
                    kontak = cl.getContacts(blockedlist)
                    num=1
                    msgs="═════════List Blocked═════════"
                    for ids in kontak:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                    cl.sendText(msg.to, msgs)
                    
                elif msg.text.lower().startswith(key["keyCommand"]+"gbroadcast:"):
                    sep = msg.text.split(" ")
                    txt = msg.text.replace(sep[0] + " ","")
                    groups = cl.getGroupIdsJoined()
                    for group in groups:
                        cl.sendText(group, "[ Broadcast ]\n{}".format(str(txt)))
                    cl.sendText(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                elif msg.text.lower().startswith(key["keyCommand"]+"fbroadcast:"):
                    sep = msg.text.split(" ")
                    txt = msg.text.replace(sep[0] + " ","")
                    friends = cl.getAllContactIds()
                    for friend in friends:
                        cl.sendText(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    cl.sendText(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
                elif msg.text.lower().startswith(key["keyCommand"]+"allbroadcast:"):
                    sep = msg.text.split(" ")
                    txt = msg.text.replace(sep[0] + " ","")
                    friends = cl.getAllContactIds()
                    groups = cl.getGroupIdsJoined()
                    for group in groups:
                        cl.sendText(group, "[ Broadcast ]\n{}".format(str(txt)))
                    cl.sendText(msg.to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                    for friend in friends:
                        cl.sendText(friend, "[ Broadcast ]\n{}".format(str(txt)))
                    cl.sendText(msg.to, "Berhasil broadcast ke {} teman".format(str(len(friends))))
    #==============================================================================#
    #================================ SELF KICKER =================================#
    #==============================================================================#
    
                elif msg.text.lower().startswith(key["keyCommand"]+"kick"):
                       targets = []
                       mention = eval(msg.contentMetadata["MENTION"])
                       mention["MENTIONEES"] [0] ["M"]
                       for x in mention["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               cl.kickoutFromGroup(msg.to,[target])
                           except:
                               cl.sendText(msg.to,"Error")
                
                elif msg.text.lower().startswith(key["keyCommand"]+"ulti"):
                       targets = []
                       mention = eval(msg.contentMetadata["MENTION"])
                       mention["MENTIONEES"] [0] ["M"]
                       for x in mention["MENTIONEES"]:
                           targets.append(x["M"])
                       for target in targets:
                           try:
                               cl.kickoutFromGroup(msg.to,[target])
                               cl.findAndAddContactsByMid(msg.to,[target])
                               cl.inviteIntoGroup(msg.to,[target])
                               cl.cancelGroupInvitation(msg.to,[target])
                           except:
                               cl.sendText(msg.to,"Error")
                               
                elif msg.text.lower() == key["keyCommand"]+'cancel':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        if group.invitee is not None:
                            try:
                                gInviMids = [contact.mid for contact in group.invitee]
                                cl.cancelGroupInvitation(msg.to, gInviMids)
                            except:
                               cl.sendText(msg.to,"Tidak Ada Invitan Yang Pending")
    #==============================================================================#
    #================================= SELF GROUP =================================#
    #==============================================================================#
                elif msg.text.lower() == key["keyCommand"]+'detailsgroup':
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Name Group : {}".format(group.name)
                    ret_ += "\n╠ID Group : {}".format(group.id)
                    ret_ += "\n╠Creator Group : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Group QR : {}".format(gQr)
                    ret_ += "\n╠Group URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                    
                elif msg.text.lower() == key["keyCommand"]+'grouplist':
                    groups = cl.getGroupIdsJoined()
                    ret_ = "╔══[ Group List ]"
                    no = 0
                    for gid in groups:
                        group = cl.getGroup(gid)
                        ret_ += "\n╠ {}. {} | {}".format(str(no), str(group.name), str(len(group.members)))
                        no += 1
                    ret_ += "\n╚══[ Total {} Groups ]".format(str(len(groups)))
                    cl.sendText(msg.to, str(ret_))
                        
                elif msg.text.lower() == key["keyCommand"]+'memberlist':
                    kontak = cl.getGroup(msg.to)
                    group = kontak.members
                    num=1
                    msgs="═════════List Member═════════"
                    for ids in group:
                        msgs+="\n[%i] %s" % (num, ids.displayName)
                        num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                    cl.sendText(msg.to, msgs)
                    
                elif msg.text.lower() == key["keyCommand"]+'grouppicture':
                    group = cl.getGroup(msg.to)
                    path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                    cl.sendImageWithURL(msg.to, path)
                
                elif msg.text.lower() == key["keyCommand"]+'groupname':
                    gid = cl.getGroup(msg.to)
                    cl.sendText(msg.to, "[Nama Group : ]\n" + gid.name)
                
                elif msg.text.lower() == key["keyCommand"]+'groupid':
                    gid = cl.getGroup(msg.to)
                    cl.sendText(msg.to, "[ID Group : ]\n" + gid.id)
                    
                elif msg.text.lower() == key["keyCommand"]+'groupticket':
                    if msg.toType == 2:
                        g = cl.getGroup(msg.to)
                        if g.preventJoinByTicket == True:
                            g.preventJoinByTicket = False
                            cl.updateGroup(g)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"line://ti/g/" + gurl)

                elif msg.text.lower() == key["keyCommand"]+'crash':
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': "Bos,'"}
                        cl.sendMessage(msg)
                
                elif msg.text.lower() == key["keyCommand"]+'openqr':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        group.preventJoinByTicket = False
                        cl.updateGroup(group)
                        gurl = cl.reissueGroupTicket(msg.to)
                        cl.sendText(msg.to,"QR Group open\n\n" + "Link : line://ti/g/" + gurl)
                        
                elif msg.text.lower() == key["keyCommand"]+'closeqr':
                    if msg.toType == 2:
                        group = cl.getGroup(msg.to)
                        group.preventJoinByTicket = True
                        cl.updateGroup(group)
                        cl.sendText(msg.to,"QR Group close")
                
            
                elif msg.text.lower() == key["keyCommand"]+'groupcreator':
                    try:
                        group = cl.getGroup(msg.to)
                        GS = group.creator.mid
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': GS}
                        cl.sendMessage(M)
                    except:
                        pass
                
                elif msg.text.lower().startswith(key["keyCommand"]+"changegroupname"):
                    if msg.toType == 2:
                        X = cl.getGroup(msg.to)
                        sep = msg.text.split(" ")
                        X.name = msg.text.replace(sep[0] + " ","")
                        cl.updateGroup(X)
    #==============================================================================#
    #================================= SELF MIMIC =================================#
    #==============================================================================#
                elif msg.text.lower().startswith(key["keyCommand"]+"mimicadd"):
                    targets = []
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention["MENTIONEES"][0]["M"]
                    for x in mention["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            mimic["target"][target] = True
                            cl.sendText(msg.to,"Target ditambahkan!")
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
                        
                elif msg.text.lower().startswith(key["keyCommand"]+"mimicdel"):
                    targets = []
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention["MENTIONEES"][0]["M"]
                    for x in mention["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            del mimic["target"][target]
                            cl.sendText(msg.to,"Target dihapuskan!")
                            break
                        except:
                            cl.sendText(msg.to,"Fail !")
                            break
                        
                elif msg.text.lower() == key["keyCommand"]+'mimiclist':
                    if mimic["target"] == {}:
                        cl.sendText(msg.to,"Tidak Ada Daftar Mimic")
                    else:
                        mc = "═════════List Member═════════\n"
                        for mi_d in mimic["target"]:
                            mc += "╠ "+cl.getContact(mi_d).displayName + "\n"
                        cl.sendText(msg.to,mc + "\n═════════List Member═════════")
    
                elif msg.text.lower().startswith(key["keyCommand"]+"mimic"):
                    sep = msg.text.split(" ")
                    cmd = msg.text.replace(sep[0] + " ","")
                    if cmd == "on":
                        if mimic["status"] == False:
                            mimic["status"] = True
                            cl.sendText(msg.to,"Reply Message on")
                        else:
                            cl.sendText(msg.to,"Sudah on")
                    elif cmd == "off":
                        if mimic["status"] == True:
                            mimic["status"] = False
                            cl.sendText(msg.to,"Reply Message off")
                        else:
                            cl.sendText(msg.to,"Sudah off")
    #==============================================================================#
    #================================ SELF SPECIAL ================================#
    #==============================================================================#
                elif msg.text.lower() == key["keyCommand"]+'mention':
                     group = cl.getGroup(msg.to)
                     nama = [contact.mid for contact in group.members]
                     nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                     if jml <= 100:
                        summon(msg.to, nama)
                     if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                     if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                     if jml > 500:
                         print "Terlalu Banyak Men 500+"
                     cnt = Message()
                     cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                     cnt.to = msg.to
                     cl.sendMessage(cnt)
                     
                elif msg.text.lower() == key["keyCommand"]+'lurking on':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read['readPoint']:
                            try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                            except:
                                pass
                            read['readPoint'][msg.to] = msg.id
                            read['readMember'][msg.to] = ""
                            read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                            read['ROM'][msg.to] = {}
                            with open('sider.json', 'w') as fp:
                                json.dump(read, fp, sort_keys=True, indent=4)
                                cl.sendText(msg.to,"Lurking already on")
                    else:
                        try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                        except:
                            pass
                        read['readPoint'][msg.to] = msg.id
                        read['readMember'][msg.to] = ""
                        read['readTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        read['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                            json.dump(read, fp, sort_keys=True, indent=4)
                            cl.sendText(msg.to, "Set reading point:\n" + readTime)
                            
                elif msg.text.lower() == key["keyCommand"]+'lurking off':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to not in read['readPoint']:
                        cl.sendText(msg.to,"Lurking already off")
                    else:
                        try:
                                del read['readPoint'][msg.to]
                                del read['readMember'][msg.to]
                                del read['readTime'][msg.to]
                        except:
                              pass
                        cl.sendText(msg.to, "Delete reading point:\n" + readTime)
    
                elif msg.text.lower() == key["keyCommand"]+'lurking reset':
                    tz = pytz.timezone("Asia/Jakarta")
                    timeNow = datetime.now(tz=tz)
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    hr = timeNow.strftime("%A")
                    bln = timeNow.strftime("%m")
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                    if msg.to in read["readPoint"]:
                        try:
                            read["readPoint"][msg.to] = True
                            read["readMember"][msg.to] = {}
                            read["readTime"][msg.to] = readTime
                            read["ROM"][msg.to] = {}
                        except:
                            pass
                        cl.sendText(msg.to, "Reset reading point:\n" + readTime)
                    else:
                        cl.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
                elif msg.text.lower() == key["keyCommand"]+'lurking':
                        tz = pytz.timezone("Asia/Jakarta")
                        timeNow = datetime.now(tz=tz)
                        day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                        hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                        bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                        hr = timeNow.strftime("%A")
                        bln = timeNow.strftime("%m")
                        for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                        for k in range(0, len(bulan)):
                            if bln == str(k): bln = bulan[k-1]
                        readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                        if msg.to in read['readPoint']:
                            if read["ROM"][msg.to].items() == []:
                                 cl.sendText(msg.to, "Lurkers:\nNone")
                            else:
                                chiya = []
                                for rom in read["ROM"][msg.to].items():
                                    chiya.append(rom[1])
                                   
                                cmem = cl.getContacts(chiya)
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan = '[ Reader ]\n'
                            for x in range(len(cmem)):
                                    xname = str(cmem[x].displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@a\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                            msg.text = xpesan+ zxc + "\nLurking time: \n" + readTime
                            lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            msg.contentMetadata = lol
                            try:
                              cl.sendMessage(msg)
                            except Exception as error:
                                  print error
                            pass
                        else:
                            cl.sendText(msg.to, "Lurking has not been set.")
    #==============================================================================#
    #================================ SELF SPECIAL ================================#
    #==============================================================================#
                elif msg.text.lower().startswith(key["keyCommand"]+"youtubesearch"):
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.youtube.com/results", params = params)
                        soup = BeautifulSoup(r.content, "html5lib")
                        ret_ = "╔══[ Youtube Result ]"
                        datas = []
                        for data in soup.select(".yt-lockup-title > a[title]"):
                            if "&lists" not in data["href"]:
                                datas.append(data)
                        for data in datas:
                            ret_ += "\n╠══[ {} ]".format(str(data["title"]))
                            ret_ += "\n╠ https://www.youtube.com{}".format(str(data["href"]))
                        ret_ += "\n╚══[ Total {} ]".format(len(datas))
                        cl.sendText(msg.to, str(ret_))

                elif msg.text.lower().startswith(key["keyCommand"]+"snapgram"):
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {"search_query": search}
                    with requests.session() as s: 
                        s.headers['user-agent'] = 'Mozilla/5.0' 
                        url    = 'https://www.instagram.com/'+user+'/' 
                        params = {'__a': query} 
                        r      = s.get(url, params=params).content 
                        data = json.loads(r)['user'] 
                        user_id   = data['id']  
                        with requests.session() as s: 
                            s.headers['cookie']  = 'mi ayam' 
                            s.headers['user-agent'] = 'Instagram 10.3.2 (iPhone7,2; iPhone OS 9_3_3; en_US; en-US; scale=2.00; 750x1334) AppleWebKit/420+' 
                            s.headers['cache-control'] = 'no-cache' 
                            s.headers['x-ig-capabilities'] = '36oD' 
                            respon = s.get('https://i.instagram.com/api/v1/feed/user/'+user_id+'/story/') 
                            data = json.loads(respon.content)['reel'] 
                            if data == None: 
                                client.sendMessage(receiver, "Not Found") 
                            else: 
                                for i in range(len(data)): 
                                    if 'video_versions' in data['items'][i]: 
                                        video = data['items'][i]['video_versions'][0]['url'] 
                                        client.sendVideoWithURL(receiver, str(video))
                                    else: 
                                        medias = data['items'][i]['image_versions2']['candidates'][0]['url'] 
                                        client.sendImageWithURL(receiver, str(medias))
                                        
                elif msg.text.lower().startswith(key["keyCommand"]+"idline"):
                    conn = cl.findContactsByUserid(msgg)
                    if False:
                 	    cl.sendText(msg.to,"Gaada ID kayak gitu")
                    if True:
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': conn.mid}
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+conn.pictureStatus)
                        cl.sendText(msg.to,"[ Nama Profil ]\n"+conn.displayName+"\n\n[ Status Profil ]\n"+conn.statusMessage+"\n\n[ Mid Profil ]\n"+conn.mid+"\n\nKepoin lebih lanjut?\nKlik kontak dibawah ini~")
                        cl.sendMessage(msg)
                        
                elif msg.text.lower().startswith(key["keyCommand"]+"prankcall "):
                        start = time.time()
                        separate = msg.text.split(" ")
                        search = msg.text.replace(separate[0] + " ","")
                        r = requests.get("http://apisora.herokuapp.com/prank/call/?no="+str(no))
                        data = r.json()
                        result = data["result"].replace('</br>', '\n')
                        tgb = "[ Prank Call ]\n\n"
                        tgb += "Status: "+str(data["status"])+"\n"
                        tgb += "Result: "+str(result)+"\n\n[ Finish ]"
                        cl.sendText(msg.to,str(tgb))
                
                elif msg.text.lower().startswith(key["keyCommand"]+"wikipedia"):
                      try:
                          sep = msg.text.split(" ")
                          wiki = msg.text.replace(sep[0] + " ","")
                          wikipedia.set_lang("id")
                          pesan="Title ("
                          pesan+=wikipedia.page(wiki).title
                          pesan+=")\n\n"
                          pesan+=wikipedia.summary(wiki, sentences=1)
                          pesan+="\n"
                          pesan+=wikipedia.page(wiki).url
                          cl.sendText(msg.to, pesan)
                      except:
                              try:
                                  pesan="Over Text Limit! Please Click link\n"
                                  pesan+=wikipedia.page(wiki).url
                                  cl.sendText(msg.to, pesan)
                              except Exception as e:
                                  cl.sendText(msg.to, str(e))
                                  
                elif msg.text.lower().startswith(key["keyCommand"]+"lyric"):
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[3]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                cl.sendText(msg.to, str(ret_))
                        except:
                            cl.sendText(to, "Lirik tidak ditemukan")
                            
                elif msg.text.lower().startswith(key["keyCommand"]+"music"):
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                ret_ = "╔══[ Music ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[3]))
                                ret_ += "\n╚══[ Waiting Audio ]"
                                cl.sendText(msg.to, str(ret_))
                                cl.sendText(msg.to, "Mohon bersabar musicnya lagi di upload")
                                cl.sendAudioWithURL(msg.to, song[3])
                        except:
                            cl.sendText(to, "Musik tidak ditemukan")
    
                elif msg.text.lower().startswith(key["keyCommand"]+"imagesearch"):
                    start = time.time()
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    url = 'https://www.google.com/search?q=' + search.replace(" ","+") +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    cl.sendImageWithURL(msg.to,path)
                    a = items.index(path)
                    b = len(items)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to,"Image #%s from #%s image\nGot image in %s seconds" %(str(a), str(b), elapsed_time))
                
                elif msg.text.lower() == key["keyCommand"]+'kalender':
                    timeNow = datetime.now()
                    timeHours = datetime.strftime(timeNow,"(%H:%M)")
                    day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                    hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                    bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                    inihari = datetime.today()
                    hr = inihari.strftime('%A')
                    bln = inihari.strftime('%m')
                    for i in range(len(day)):
                        if hr == day[i]: hasil = hari[i]
                    for k in range(0, len(bulan)):
                        if bln == str(k): bln = bulan[k-1]
                    rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                    cl.sendText(msg.to, rst)
                    
                elif msg.text.lower().startswith(key["keyCommand"]+"profileig"):
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(settings["userAgent"])
                        r = web.get("https://www.instagram.com/{}/?__a=1".format(search))
                        try:
                            data = json.loads(r.text)
                            ret_ = "╔══[ Profile Instagram ]"
                            ret_ += "\n╠ Nama : {}".format(str(data["user"]["full_name"]))
                            ret_ += "\n╠ Username : {}".format(str(data["user"]["username"]))
                            ret_ += "\n╠ Bio : {}".format(str(data["user"]["biography"]))
                            ret_ += "\n╠ Pengikut : {}".format(format_number(data["user"]["followed_by"]["count"]))
                            ret_ += "\n╠ Diikuti : {}".format(format_number(data["user"]["follows"]["count"]))
                            if data["user"]["is_verified"] == True:
                                ret_ += "\n╠ Verifikasi : Sudah"
                            else:
                                ret_ += "\n╠ Verifikasi : Belum"
                            if data["user"]["is_private"] == True:
                                ret_ += "\n╠ Akun Pribadi : Iya"
                            else:
                                ret_ += "\n╠ Akun Pribadi : Tidak"
                            ret_ += "\n╠ Total Post : {}".format(format_number(data["user"]["media"]["count"]))
                            ret_ += "\n╚══[ https://www.instagram.com/{} ]".format(search)
                            path = data["user"]["profile_pic_url_hd"]
                            cl.sendText(msg.to, str(ret_))
                        except:
                            cl.sendText(msg.to, "Pengguna tidak ditemukan")
                            
                elif msg.text.lower().startswith(key["keyCommand"]+"checkdate"):
                    sep = msg.text.split(" ")
                    tanggal = msg.text.replace(sep[0] + " ","")
                    r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                    data=r.text
                    data=json.loads(data)
                    lahir = data["data"]["lahir"]
                    usia = data["data"]["usia"]
                    ultah = data["data"]["ultah"]
                    zodiak = data["data"]["zodiak"]
                    cl.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")
            
    #==============================================================================#
                #               T E X T     T O     S P E E C H             #
                
                elif msg.text.lower().startswith(key["keyCommand"]+"say-"):
                    sep = msg.text.split("-")
                    sep = sep[1].split(" ")
                    lang = sep[0]
                    say = msg.text.lower().replace(key["keyCommand"] + "say-" + lang + " ","")
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasil.mp3")
                    cl.sendAudio(msg.to, "hasil.mp3")
    #==============================================================================#
            #                   T R A N S L A T E                   #
                elif msg.text.lower().startswith(key["keyCommand"]+"tr-"):
                    sep = msg.text.split("-")
                    sep = sep[1].split(" ")
                    lang = sep[0]
                    text_ = msg.text.lower().replace(key["keyCommand"] + "tr-" + lang + " ","")
                    translator = Translator()
                    hasil = translator.translate(text_, dest=lang)
                    hasil = hasil.text.encode('utf-8')
                    cl.sendText(msg.to, str(hasil))
    #==============================================================================#
    #==============================================================================#
    #==============================================================================#
                elif msg.text.lower() == key["keyCommand"]+'status':
                    md = ""
                    if settings["autoJoin"] == True: md+="Auto Join → ✔\n"
                    else: md +="Auto Join → ❌\n"
                    if settings["autoLeaveRoom"] == True: md+="Auto Leave Room → ✔\n"
                    else: md +="Auto Leave Room → ❌\n"
                    if settings["autoAdd"] == True: md+="Auto add → ✔\n"
                    else:md+="Auto add → ❌\n"
                    if settings["autoRead"] == True: md+="Auto Read → ✔\n"
                    else: md+="Auto Read → ❌\n"
                    if settings["responMention"] == True: md+="Auto Respon → ✔\n"
                    else:md+="Auto Respon → ❌\n"
                    if settings["checkContact"] == True: md+="CheckContact → ✔\n"
                    else: md+="CheckContact → ❌\n"
                    if settings["checkPost"] == True: md+="CheckPost → ✔\n"
                    else: md+="CheckPost → ❌\n"
                    if settings["simiSimi"] == True: md+=" Simisimi → ✔\n"
                    else:md+="Simisimi → ❌\n"
                    cl.sendText(msg.to,md)
                    
                elif msg.text.lower() == key["keyCommand"]+'autoadd on':
                    settings["autoAdd"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan auto add")
                elif msg.text.lower() == key["keyCommand"]+'autoadd off':
                    settings["autoAdd"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan auto add")
                elif msg.text.lower() == key["keyCommand"]+'autojoin on':
                    settings["autoJoin"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan auto join")
                elif msg.text.lower() == key["keyCommand"]+'autojoin off':
                    settings["autoJoin"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan auto join")
                elif msg.text.lower() == key["keyCommand"]+'autoleaveroom on':
                    settings["autoLeaveRoom"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan auto leave room")
                elif msg.text.lower() == key["keyCommand"]+'autoleaveroom off':
                    settings["autoLeaveRoom"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan auto leave room")
                elif msg.text.lower() == key["keyCommand"]+'autorespon on':
                    settings["responMention"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan auto respon mention")
                elif msg.text.lower() == key["keyCommand"]+'autorespon off':
                    settings["responMention"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan auto respon mention")
                elif msg.text.lower() == key["keyCommand"]+'checkcontact on':
                    settings["checkContact"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan cek detail kontak")
                elif msg.text.lower() == key["keyCommand"]+'checkcontact off':
                    settings["checkContact"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan cek detail kontak")
                elif msg.text.lower() == key["keyCommand"]+'checkpost on':
                    settings["checkPost"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan cek detail post")
                elif msg.text.lower() == key["keyCommand"]+'checkpost off':
                    settings["checkPost"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan cek detail post")
                elif msg.text.lower() == key["keyCommand"]+'autoread on':
                    settings["autoRead"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan auto read")
                elif msg.text.lower() == key["keyCommand"]+'autoread off':
                    settings["autoRead"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan auto read")
                elif msg.text.lower() == key["keyCommand"]+'simisimi on':
                    settings["simiSimi"] = True
                    cl.sendText(msg.to, "Berhasil mengaktifkan simisimi")
                elif msg.text.lower() == key["keyCommand"]+'simisimi off':
                    settings["simisimi"] = False
                    cl.sendText(msg.to, "Berhasil menonaktifkan simisimi")
                    
                elif msg.text.lower() == key["keyCommand"]+'autorespon':
                    if message["replyPesan"] is not None:
                        cl.sendText(msg.to,"My Set AutoRespon : " + str(message["replyPesan"]))
                    else:
                        cl.sendText(msg.to,"My Set AutoRespon : No messages are set")
                elif msg.text.lower().startswith(key["keyCommand"]+"autorespon:"):
                    sep = msg.text.split(" ")
                    text = msg.text.replace(sep[0] + " ","")
                    try:
                        message["replyPesan"] = text
                        cl.sendText(msg.to,"「AutoRespon」Changed to : " + text)
                    except:
                        cl.sendText(msg.to,"「AutoRespon」\nFailed to replace message")

#==============================================================================#
#==============================================================================#
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in read['readPoint']:
           
                    if op.param2 in read['readMember'][op.param1]:
                        pass
                    else:
                        read['readMember'][op.param1] += op.param2
                    read['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        if op.type == 59:
            print op
            
    except Exception as error:
        print error

while True:
	bot(cl.Poll.stream(500000))
