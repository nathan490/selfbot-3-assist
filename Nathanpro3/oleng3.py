#OLENG OFFICIAL
# sᴄʀɪᴘᴇ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ ᴜᴘᴅᴀᴛᴇ 2-10-2020
# ᴛᴇᴀᴍ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ
#ᴊᴀɴɢᴀɴ sᴏᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ ᴋʟᴏ ɢᴋ ʙɪsᴀ ɴɢᴇᴅɪᴛ
#ᴄʀᴇᴀᴛᴏʀ ʙʏᴇ ᴀʙɪ ᴛᴇᴀᴍ ᴏʟᴇɴɢ
import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
botStart = time.time()
msg_dict = {}
msg_dict1 = {}
#================================================
#LOGIN GMAIL/QR
#MuhazirOLENG ="CHROMEOS\t2.3.8\tChrome OS\t1"
#================================================
#LOGIN TOKEN PRIKERY
MuhazirOLENG ="ANDROIDLITE\t2.16.0\tAndroid OS\t5.1.1"
#================================================
IndOleng = AbiMyYoutube("token/gmail",appName=MuhazirOLENG)
#================================================
AssOleng = AbiMyYoutube("token/gmail",appName=MuhazirOLENG)
#================================================
AntiJsOleng = AbiMyYoutube("token/gmail",appName=MuhazirOLENG)
#================================================
print ("=========== ʟᴏɢɪɴ sᴜᴄᴄᴇs ʙᴏssᴋᴜ ᴀʙɪ ==========")
#================================================
AbiJomblo = IndOleng.profile.mid
AbiJomblo = IndOleng.getProfile().mid
OlengAss = AssOleng.getProfile().mid
AjsAbi = AntiJsOleng.getProfile().mid
#================================================
TeamBotsOleng = [IndOleng,AssOleng]
BotsAbiOlengKiller = [IndOleng,AssOleng]
AbiOleng = [AntiJsOleng]
Bots = [AbiJomblo,OlengAss,AjsAbi]
#================================================
MyAbiBosKu = ["ua2df72c7f7f866dc7be8fbd27ede7ae4"]
MyAbiBossKu = ["ua2df72c7f7f866dc7be8fbd27ede7ae4"]
OlengKiller = MyAbiBosKu + MyAbiBossKu #u + Bots
#================================================
proqr = []
prokick = []
projoin = []
proinv = []
procancel = []
welcome = []
#================================================
PasukanOlengKiller = IndOleng.getProfile().displayName
PasukanOlengKiller = AssOleng.getProfile().displayName
#================================================
OLENGIN = {
    "limit": 1,
    "MyAbiBosKu":{},
    "MyAbiBossKu":{},
    "AbiOlengBackup":{},
    "MyAbiBossKu":False,
    "MyAbiBosKu":False,
    "AddMyAbiBossKu":False,
    "DellMyAbiBossKu":False,
    "kikilbantai":True,
    "bots":{},
    "AddMyBot":False,
    "DellMyBot":False,
    "cancell":True,
    "blacklist":{},
    "contact":False,
    'InviteGrup':True,
    'AddTeman':True,
    'AutoBaper':True,
    'left':True,
    'GrupMole':False,
    "kickoleng":True,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "welcomeOn":True,
    "sticker":False,
    'olenginv':True,
    "OlengPro":True,
    "likeOn":False,
    'autoBlock':False,
    "unsend":True,
    "arespon":True,
    "mention1":True,
    "Sctv":{},
    "Global":{},
    "Indosiar":{},
    "Respontag":"sᴇᴋᴀʟɪ ʟᴀɢɪ ᴛᴀɢ, ᴍᴀᴜ ᴋɪɴɢ ᴅᴇsᴀʜɪɴ",
    "welcome":"Selamat nikung & semoga betah n bahagia",
    "message":"╭──────────────────╮\n├🔹ɴᴜᴍᴘᴀɴɢ ᴘʀᴏᴍᴏ ʏᴀ ᴋᴀᴋᴀᴋ    │\n╰──────────────────╯\n╭──────────────────\n├🔹ʀᴇᴀᴅʏ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ\n├🔹ʀᴏᴏᴍ sᴍᴜʟᴇ / ᴇᴠᴇɴᴛ \n├🔹ʀᴇᴀᴅʏ sʙ ᴏɴʟʏ \n├🔹sʙ ᴏɴʟʏ + ᴀᴊs \n├🔹sʙ + ᴀssɪsᴛ + ᴀᴊs \n├🔹ʟᴏɢɪɴ ᴊs / ʙʏᴘᴀs\n├🔹ɴᴇᴡ ᴘᴇᴍʙᴜᴀᴛᴀɴ sᴄ ʙᴏᴛ \n├🔹ɴᴇᴡ ʙᴇʟᴀᴊᴀʀ ʙᴏᴛ \n├🔹ᴘᴇᴍᴀsᴀɴɢ sʙ ᴋᴇ ᴛᴇᴍᴘʟᴀᴛᴇ\n├🔹ʀᴇᴀᴅʏ ᴀᴋᴜɴ ᴄᴏɪɴ\n├🔹ʀᴇᴀᴅʏ ᴄᴏɪɴ ɢɪғᴛ \n╰────────────────── \n╭─────────────────\n├ line.me/ti/p/~santai82a\n╰─────────────────",
    }
#================================================
with open('AbiBosku.json', 'r') as fp:
    MyAbiBosKu = json.load(fp)
#================================================
TeamBackupJson = codecs.open("TeamOleng.json","r","utf-8")
TeamBotsOLENGKILLER = json.load(TeamBackupJson)
#================================================
OutAssist = "Di Suruh Balik Sama Bossku\nMakasih Ya Undangan Di Grup"
BankOleng ="""╭───────────────────╮
├🔹ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ
├ ɴᴏ ʀᴇᴋ : 481901020711531
├ ᴀᴛᴀs ɴᴀᴍᴀ : ᴍᴜʜᴀᴢɪʀ
├ ʙᴀɴᴋ ʙʀɪ
├🔹ᴠɪᴀ ᴘᴜʟsᴀ
├ 08992906209
├🔹ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ᴘᴀʏᴘᴀʟ
├ ᴍᴜʜᴀᴊɪʀᴀʟᴡɪ123@gmail.ᴄᴏᴍ
╰───────────────────╯"""
#================================================
mulai = time.time()
tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def RebootBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def executeCmd(msg, text, txt, AbiOlengOK, msg_id, receiver, sender, to, setKey):
    if AbiOlengOK.startswith('ex\n'):
      if sender in clientMid:
        try:
            Sial = text.split('\n')
            Abie = text.replace(Sial[0] + '\n','')
            Fefek = open('exec.txt', 'w')
            sys.stdout = Fefek
            print(' ')
            exec(Abie)
            print('\n%s' % str(datetime.now()))
            Fefek.close()
            sys.stdout = sys.__stdout__
            with open('exec.txt','r') as Ngentot:
                Tulisan = Ngentot.read()
            IndOleng.sendMessage(to, Tulisan)
        except Exception as e:
            pass
      else:
        IndOleng.sendMessage(to, 'ᴀᴘᴀʟᴜ !')
    elif AbiOlengOK.startswith('exc\n'):
      if sender in clientMid:
        Jurusan = text.split('\n')
        Abie = text.replace(Jurusan[0] + '\n','')
        if 'print' in Muhazir:
        	Abie = Muhazir.replace('print(','IndOleng.sendExecMessage(to,')
        	exec(Abie)
        else:
        	exec(Abie)
      else:
        IndOleng.sendMessage(to, 'ᴀᴘᴀʟᴜ !')        

def KotakOleng(text):
    OlengKiller.log("[ ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ ] {}".format(str(text)))
    OlengTime = pytz.timezone("Asia/Makassar")
    WaktuBaruOleng = datetime.now(OlengTime=OlengTime)
    timeHours = datetime.strftime(WaktuBaruOleng,"(%H:%M)")
    KalenderEng = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
    KalenderInd = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
    KalenderBulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    OlengSekarang = datetime.now(OlengTime=OlengTime)
    AbiOk = OlengSekarang.strftime('%A')
    AbiOke = OlengSekarang.strftime('%m')
    for Ayam in Bebek(len(KalenderEng)):
        if AbiOk == KalenderEng[Ayam]: Panen = KalenderInd[Ayam]
    for Kambing in Bebek(0, len(KalenderBulan)):
        if AbiOke == str(Kambing): AbiOke = KalenderBulan[Kambing-1]
    Waktu = "{}, {} - {} - {} | {}".format(str(Panen), str(OlengSekarang.strftime('%d')), str(AbiOke), str(OlengSekarang.strftime('%Y')), str(OlengSekarang.strftime('%H:%M:%S')))
    with open("errorLog.txt","a") as OlengMate:
        OlengMate.write("\n[{}] {}".format(str(Waktu), text))
        
def AbiYear():
    if AbieDetik != {}:
        for AbieMuhazir in AbieDetik:
            if AbieDetik[AbieMuhazir]["expire"] == True:
                if time.time() - AbieDetik[AbieMuhazir]["time"] >= 3*10:
                    AbieDetik[AbieMuhazir]["expire"] = False
                    AbieDetik[AbieMuhazir]["time"] = time.time()
                    try:
                        AbieOleng = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        IndOleng.sendMessage(AbieMuhazir, AbieOleng, {'AGENT_LINK': "https://line.me/ti/p/~muhaziroleng", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as oleng:
                        logError(oleng)

def AbiDay():
    if AbieDetik != {}:
        for AbieMuhazir in AbieDetik:
            if AbieDetik[AbieMuhazir]["expire"] == True:
                    AbieDetik[AbieMuhazir]["expire"] = False
                    AbieDetik[AbieMuhazir]["time"] = time.time()
                    try:
                        AbieOleng = "ʙᴏᴛ ᴀᴋᴛɪғ ʙᴏssᴋᴜ"
                        IndOleng.sendMessage(AbieMuhazir, AbieOleng, {'AGENT_LINK': "https://line.me/ti/p/~santai82a", 'AGENT_ICON': "http://klikuntung.com/images/messengers/line-logo.png", 'AGENT_NAME': "Detect Spam "})        
                    except Exception as oleng:
                        logError(oleng)    

def AbiOleNgKiller(to):
    contentMetadata={'previewUrl': "http://dl.profile.line-cdn.net/"+IndOleng.getContact(AbiJomblo).picturePath, 'i-installUrl': 'http://itunes.apple.com/app/linemusic/id966142320', 'type': 'mt', 'subText': IndOleng.getContact(AbiJomblo).statusMessage if IndOleng.getContact(AbiJomblo).statusMessage != '' else 'http://line.me/ti/p/~muhaziroleng', 'a-installUrl': 'market://details?id=jp.linecorp.linemusic.android', 'a-packageName': 'jp.linecorp.linemusic.android', 'countryCode': 'JP', 'a-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'i-linkUri': 'linemusic://open?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1', 'text': IndOleng.getContact(AbiJomblo).displayName, 'id': 'mt000000000d69e2db', 'linkUri': 'https://music.cl.cl/launch?target=track&item=mb00000000016197ea&subitem=mt000000000d69e2db&cc=JP&from=lc&v=1','MSG_SENDER_ICON': "https://os.me.naver.jp/os/p/"+AbiJomblo,'MSG_SENDER_NAME':  IndOleng.getContact(AbiJomblo).displayName,}
    return IndOleng.sendMessage(to, IndOleng.getContact(AbiJomblo).displayName, contentMetadata, 19)

def TeamProtectOlengKiller(text):
    Tulisan = text.lower()
    if Tulisan.startswith(TeamBotsOLENGKILLER["KunciOleng"]):
        AbiOlengOK = Tulisan.replace(TeamBotsOLENGKILLER["KunciOleng"],"")
    else:
        AbiOlengOK = "command"
    return AbiOlengOK

def AbiHelp():
    OLENGBOTS = TeamBotsOLENGKILLER["KunciOleng"]
    OLENGBOTS = OLENGBOTS.title()
    CmdOleng = "╭────────────╮" + "\n" + \
                  "├  🔹ᴄᴏᴍᴍᴇɴᴅ ᴏʟᴇɴɢ" + "\n" + \
                  "╰────────────╯" + "\n" + \
                  "╭────────────╮" + "\n" + \
                  "├🔹" + OLENGBOTS + "ᴍᴇ\n" + \
                  "├🔹" + OLENGBOTS + "ᴍɪᴅ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ɪɴғᴏ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ʀᴇsᴛᴀʀᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ʀᴜɴᴛɪᴍᴇ\n" + \
                  "├🔹" + OLENGBOTS + "kick「@」\n" + \
                  "├🔹" + OLENGBOTS + "sᴘ\n" + \
                  "├🔹" + OLENGBOTS + "sᴀʏᴀɴɢ / ᴘᴇᴀ\n" + \
                  "├🔹" + OLENGBOTS + "ᴀʙɪɢᴏ\n" + \
                  "├🔹" + OLENGBOTS + "ᴀʙɪᴏᴜᴛ\n" + \
                  "├🔹" + OLENGBOTS + "sᴛᴀʏ\n" + \
                  "├🔹" + OLENGBOTS + "ᴊs ɪɴ\n" + \
                  "├🔹" + OLENGBOTS + "ᴘᴀᴘᴀʏ (ʟᴇғᴛ ɢᴄ)\n" + \
                  "├🔹" + OLENGBOTS + "ɢɪɴғᴏ\n" + \
                  "├🔹" + OLENGBOTS + "sᴇʟғ ᴏɴ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ᴏᴘᴇɴ\n" + \
                  "├🔹" + OLENGBOTS + "ᴄʟᴏsᴇ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜʀʟɢʀᴜᴘ\n" + \
                  "├🔹" + OLENGBOTS + "ɪɴғᴏɢʀᴜᴘ「ɴᴏ」\n" + \
                  "├🔹" + OLENGBOTS + "ɪɴғᴏᴍᴇᴍ「ɴᴏ」\n" + \
                  "├🔹" + OLENGBOTS + "ʜᴀᴘᴜsᴄʜᴀᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ғʀɪᴇɴᴅʟɪsᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ɢʀᴏᴜᴘʟɪsᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜᴘᴅᴀᴛᴇғᴏᴛᴏ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜᴘᴅᴀᴛᴇɢʀᴜᴘ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜᴘᴅᴀᴛᴇʙᴏᴛ\n" + \
                  "├🔹" + OLENGBOTS + "sᴇᴛᴋᴇʏ「ɴᴇᴡᴋᴇʏ」\n" + \
                  "├🔹" + OLENGBOTS + "sᴇʟғ 「ᴏɴ/ᴏғғ」\n" + \
                  "├🔹" + OLENGBOTS + "ʙʟᴄ\n" + \
                  "├🔹" + OLENGBOTS + "ʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜɴʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + OLENGBOTS + "ʙᴀɴ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ᴜɴʙᴀɴ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ᴜɴᴛᴀʟᴋʙᴀɴ「@」\n" + \
                  "├🔹" + OLENGBOTS + "ᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + OLENGBOTS + "ᴜɴᴛᴀʟᴋʙᴀɴ:ᴏɴ\n" + \
                  "├🔹" + OLENGBOTS + "ʙᴀɴʟɪsᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ᴛᴀʟᴋʙᴀɴʟɪsᴛ\n" + \
                  "├🔹" + OLENGBOTS + "ᴄʟᴇᴀʀʙᴀɴ\n" + \
                  "├🔹" + OLENGBOTS + "ʀᴇғʀᴇsʜ\n" + \
                  "├🔹" + OLENGBOTS + "myset\n" + \
                  "╰────────────╯"+ "\n" + \
                  "╭─🔹ᴄʀᴇᴀᴛᴏʀ ʙʏᴇ🔹─╮\n          ᴀʙɪ ᴍᴜʜᴀᴊɪʀ\n╰─🔹ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ🔹─╯"
    return CmdOleng
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 11 or op.type == 122:
            if OLENGIN["kikilbantai"] == True:
                try:
                    if IndOleng.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                            IndOleng.reissueGroupTicket(op.param1)
                            OK = IndOleng.getGroup(op.param1)
                            OK.preventedJoinByTicket = True
                            GasOleng = IndOleng.reissueGroupTicket(op.param1)
                            IndOleng.acceptGroupInvitationByTicket(op.param1,GasOleng)
                            IndOleng.kickoutFromGroup(op.param1,[op.param2])
                            IndOleng.updateGroup(OK)                           
                except:
                    pass
                    
        if op.type == 13 or op.type == 124:
            if AbiJomblo in op.param3:
                if OLENGIN["GrupMole"] == True:
                    if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                        IndOleng.acceptGroupInvitation(op.param1)
                        Cadangan = IndOleng.getGroup(op.param1)
                        IndOleng.leaveGroup(op.param1)
                    else:
                        IndOleng.acceptGroupInvitation(op.param1)
                        Cadangan = IndOleng.getGroup(op.param1)
                  
        if op.type == 13 or op.type == 124:
            if AbiJomblo in op.param3:
                if OLENGIN["InviteGrup"] == True:
                    if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                        IndOleng.acceptGroupInvitation(op.param1)
                        Cadangan = IndOleng.getGroup(op.param1)
                        IndOleng.sendMessage(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴅɪ ɢʀᴏᴜᴘ " +str(Cadangan.name))
                    else:
                        IndOleng.acceptGroupInvitation(op.param1)
                        Cadangan = IndOleng.getGroup(op.param1)
                        IndOleng.sendMessage(op.param1,"ʜᴀʏ sᴇᴍᴜᴀ\nᴅɪ ɢʀᴏᴜᴘ " + str(Cadangan.name))
            if OlengAss in op.param3:
                if OLENGIN["InviteGrup"] == True:
                    if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                        AssOleng.acceptGroupInvitation(op.param1)
                        Cadangan = AssOleng.getGroup(op.param1)
                        AssOleng.leaveGroup(op.param1)
                    else:
                        AssOleng.acceptGroupInvitation(op.param1)
                        Cadangan = AssOleng.getGroup(op.param1)
                        
        if op.type == 19 or op.type == 133 or op.type == 32 or op.type == 128:
            if OLENGIN["kickoleng"] == True:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        IndOleng.findAndAddContactsByMid(op.param3)
                        IndOleng.kickoutFromGroup(op.param1,[op.param2])
                        IndOleng.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
                            AssOleng.findAndAddContactsByMid(op.param3)
                            AssOleng.kickoutFromGroup(op.param1,[op.param2])
                            AssOleng.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            try:
                                AntiJsOleng.findAndAddContactsByMid(op.param3)
                                AntiJsOleng.kickoutFromGroup(op.param1,[op.param2])
                                AntiJsOleng.inviteIntoGroup(op.param1,[op.param3])
                            except:
                                pass
                        

        if op.type == 17 or op.type == 130:
            if op.param2 in OLENGIN["blacklist"]:
                IndOleng.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass
                
        if op.type == 5:
            print ("[ 5 ] ɴᴏᴛɪғɪᴇᴅ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴄᴏɴᴛᴀᴄᴛ")
            if OLENGIN["autoBlock"] == True:
                IndOleng.blockContact(op.param1)
                IndOleng.sendMessage(op.param1, OLENGIN["ᴍᴀᴀғ ᴀɪᴍ ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴀɪᴍ ᴀᴋᴛɪғ"])
                
        if op.type == 0:
            return
        if op.type == 5:
            if OLENGIN["AddTeman"] == True:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                    if (OLENGIN["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        IndOleng.sendMessage(op.param1, OLENGIN["message"])
#===========PRO INV=====================================
        if op.type == 13 or op.type == 124 or op.type == 19 or op.type == 133:
            if OLENGIN["olenginv"] == True:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                    try:
                        InvOleng = op.param3.replace('\x1e',',')
                        InvOlengKiller = InvOleng.split(',')
                        for AbiKocak in InvOlengKiller:
                            if AbiKocak not in Bots and AbiKocak not in MyAbiBosKu and AbiKocak not in MyAbiBossKu:
                                IndOleng.cancelGroupInvitation(op.param1,[op.param3])
                                IndOleng.kickoutFromGroup(op.param1,[op.param2])
                                OLENGIN["blacklist"]:[op.param2] = True
                    except:
                        try:
                            InvOleng = op.param3.replace('\x1e',',')
                            InvOlengKiller = InvOleng.split(',')
                            for AbiKocak in InvOlengKiller:
                                if AbiKocak not in Bots and AbiKocak not in MyAbiBosKu and AbiKocak not in MyAbiBossKu:
                                    AssOleng.cancelGroupInvitation(op.param1,[op.param3])
                                    AssOleng.kickoutFromGroup(op.param1,[op.param2])
                                    OLENGIN["blacklist"]:[op.param2] = True
                        except:
                            pass   
#============PRO INV====================================
        if op.type == 13 or op.type == 124 or op.type == 19 or op.type == 133:
            if op.param3 in OLENGIN["blacklist"]:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                    try:
                        InvOleng = AssOleng.getGroup(op.param1)
                        InvOlengKiller = [contact.mid for contact in InvOleng.invitee]
                        for AbiKocak in InvOlengKiller:
                            if AbiKocak in OLENGIN["blacklist"]:
                                IndOleng.cancelGroupInvitation(op.param1,[op.param3])
                                IndOoeng.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            InvOleng = AssOleng.getGroup(op.param1)
                            InvOlengKiller = [contact.mid for contact in InvOleng.invitee]
                            for AbiKocak in InvOlengKiller:
                                if AbiKocak in OLENGIN["blacklist"]:
                                    AssOleng.cancelGroupInvitation(op.param1,[op.param3])
                                    AssOleng.kickoutFromGroup(op.param1,[op.param2])
                        except:
                            pass
                
        if op.type == 19 or op.type == 133 or op.type == 32 or op.type == 126:
            if AbiJomblo in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in MyAbiBosKu:
                    pass
                if op.param2 in MyAbiBossKu:
                    pass
                else:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        AntiJsOleng.acceptGroupInvitation(op.param1)
                        AntiJsOleng.findAndAddContactsByMid(op.param3)
                        AntiJsOleng.kickoutFromGroup(op.param1,[op.param2])
                        AntiJsOleng.inviteIntoGroup(op.param1,[op.param3])
                        OK = AntiJsOleng.getGroup(op.param1)
                        OK.preventedJoinByTicket = False
                        AntiJsOleng.updateGroup(OK)
                        AntiJsOleng.leaveGroup(op.param1)
                        OKB = IndOleng.getGroup(op.param1)
                        OKB.preventedJoinByTicket = True
                        IndOleng.updateGroup(OKB)
                        IndOleng.findAndAddContactsByMid(op.param3)
                        IndOleng.inviteIntoGroup(op.param1,[AjsAbi])
                        AssOleng.findAndAddContactsByMid(op.param3)
                        AssOleng.inviteIntoGroup(op.param1,[MyAbiBossKu])
                    except:
                    	pass
            
        if op.type == 19 or op.type == 133 or op.type == 32 or op.type == 126:
            if AbiJomblo in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in MyAbiBosKu:
                    pass
                if op.param2 in MyAbiBossKu:
                    pass
                else:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        AssOleng.kickoutFromGroup(op.param1,[op.param2])
                        AssOleng.findAndAddContactsByMid(op.param3)
                        AssOleng.inviteIntoGroup(op.param1,[op.param3])
                        IndOleng.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            AntiJsOleng.kickoutFromGroup(op.param1,[op.param2])
                            AntiJsOleng.findAndAddContactsByMid(op.param3)
                            AntiJsOleng.inviteIntoGroup(op.param1,[op.param3])
                            IndOleng.acceptGroupInvitation(op.param1)
                        except:
                            pass
                return
            
        if op.type == 19 or op.type == 133 or op.type == 32 or op.type == 126:
            if OlengAss in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in MyAbiBosKu:
                    pass
                if op.param2 in MyAbiBossKu:
                    pass
                else:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        AntiJsOleng.kickoutFromGroup(op.param1,[op.param2])
                        AntiJsOleng.findAndAddContactsByMid(op.param3)
                        AntiJsOleng.inviteIntoGroup(op.param1,[op.param3])
                        AssOleng.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            IndOleng.kickoutFromGroup(op.param1,[op.param2])
                            IndOleng.findAndAddContactsByMid(op.param3)
                            IndOleng.inviteIntoGroup(op.param1,[op.param3])
                            AssOleng.acceptGroupInvitation(op.param1)
                        except:
                            pass
                return
            
        if op.type == 19 or op.type == 133 or op.type == 32 or op.type == 126:
            if AjsAbi in op.param3:
                if op.param2 in Bots:
                    pass
                if op.param2 in MyAbiBosKu:
                    pass
                if op.param2 in MyAbiBossKu:
                    pass
                else:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        IndOleng.kickoutFromGroup(op.param1,[op.param2])
                        IndOleng.findAndAddContactsByMid(op.param3)
                        IndOleng.inviteIntoGroup(op.param1,[op.param3])
                        AntiJsOleng.acceptGroupInvitation(op.param1)
                    except:
                        try:
                            AssOleng.kickoutFromGroup(op.param1,[op.param2])
                            AssOleng.findAndAddContactsByMid(op.param3)
                            AssOleng.inviteIntoGroup(op.param1,[op.param3])
                            AntiJsOleng.acceptGroupInvitation(op.param1)
                        except:
                            pass
                return
        
        if op.type == 32 or op.type == 126 or op.type == 19 or op.type == 133:
            if OLENGIN["cancell"] == True:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBossKu:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in OLENGIN["blacklist"]:
                            IndOleng.kickoutFromGroup(op.param1,[op.param2])
                            IndOleng.findAndAddContactsByMid(AjsAbi)
                            IndOleng.inviteIntoGroup(op.param1,[AjsAbi])
                    except:
                        pass
            return
        
        if op.type == 32 or op.type == 126 or op.type ==19 or op.type == 133:
            if OLENGIN["cancell"] == True:
                if op.param2 not in Bots and op.param2 not in MyAbiBosKu and op.param2 not in MyAbiBosKu:
                    OLENGIN["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in OLENGIN["blacklist"]:
                            AssOleng.kickoutFromGroup(op.param1,[op.param2])
                            AssOleng.findAndAddContactsByMid(AjsAbi)
                            AssOleng.inviteIntoGroup(op.param1,[AjsAbi])
                    except:
                        pass
            return
        if op.type == 55:
            try:
                if op.param1 in TeamBotsOLENGKILLER["MataAbi"]:
                   if op.param2 in TeamBotsOLENGKILLER["CidukMem"][op.param1]:
                       pass
                   else:
                       TeamBotsOLENGKILLER["CidukMem"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass

        if op.type == 55:
            if op.param2 in OLENGIN["blacklist"]:
                IndOleng.kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

        if op.type == 25 or op.type == 26:
           if OLENGIN["OlengPro"] == True:
               msg = op.message
               if msg.contentType == 13:
                 if OLENGIN["contact"] == True:
                    msg.contentType = 0
                    IndOleng.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = IndOleng.getContact(msg.contentMetadata["mid"])
                        path = IndOleng.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        IndOleng.sendMessage(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        IndOleng.sendImageWithURL(msg.to, image)
                        
        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.contentType == 16:
                        url = msg.contentMetadata["postEndUrl"]
                        IndOleng.likePost(url[25:58], url[66:], likeType=1004)
                        IndOleng.createComment(url[25:58], url[66:], TeamBotsOLENGKILLER["CMDoleng"])
                        print ("ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        IndOleng.sendMessage(msg.to,"👍 ᴀᴜᴛᴏ ʟɪᴋᴇ ᴅᴏɴᴇ")
                        TeamBotsOLENGKILLER["likeOn"] = True
        if op.type == 25 or op.type == 26:	     
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 13:
                 if OLENGIN["contact"] == True:
                    msg.contentType = 0
                    IndOleng.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = IndOleng.getContact(msg.contentMetadata["mid"])
                        path = IndOleng.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        IndOleng.sendMessage(msg.to,"ɴᴀᴍᴀ : " + msg.contentMetadata["displayName"] + "\nᴍɪᴅ : " + msg.contentMetadata["mid"] + "\nsᴛᴀᴛᴜs ᴍsɢ : " + contact.statusMessage + "\nᴘɪᴄᴛᴜʀᴇ ᴜʀʟ: http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        IndOleng.sendImageWithURL(msg.to, image)
#===================================[ ] ADD Bots
               if msg.contentType == 13:
                 if msg._from in MyAbiBossKu:
                  if OLENGIN["AddMyBot"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        IndOleng.sendMessage(msg.to,"🔹sᴜᴅᴀʜ ᴊᴀᴅɪ ʙᴏᴛ")
                        OLENGIN["AddMyBot"] = True
                    else:
                        Bots.append(msg.contentMetadata["mid"])
                        OLENGIN["AddMyBot"] = True
                        IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                 if OLENGIN["DellMyBot"] == True:
                    if msg.contentMetadata["mid"] in Bots:
                        Bots.remove(msg.contentMetadata["mid"])
                        IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")
                    else:
                        OLENGIN["DellMyBot"] = True
                        IndOleng.sendMessage(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀɴɢɢᴏᴛᴀ ʙᴏᴛ")

#===================================[ ]  ADD MyAbiBossKu
                 if msg._from in MyAbiBossKu:
                  if OLENGIN["AddMyAbiBossKu"] == True:
                    if msg.contentMetadata["mid"] in MyAbiBossKu:
                        IndOleng.sendMessage(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
                        OLENGIN["AddMyAbiBossKu"] = True
                    else:
                        MyAbiBossKu.append(msg.contentMetadata["mid"])
                        OLENGIN["AddMyAbiBossKu"] = True
                        IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ")
                 if OLENGIN["DellMyAbiBossKu"] == True:
                    if msg.contentMetadata["mid"] in MyAbiBossKu:
                        MyAbiBossKu.remove(msg.contentMetadata["mid"])
                        IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ")
                    else:
                        OLENGIN["DellMyAbiBossKu"] = True
                        IndOleng.sendMessage(msg.to,"🔹ɪᴛᴜ ʙᴜᴋᴀɴ ᴀᴅᴍɪɴ")
#===================================[ ] UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                    if TeamBotsOLENGKILLER["TambahFoto"] == True:
                        msgid = msg.id
                        fotoo = "https://obs.line-apps.com/talk/m/download.nhn?oid="+msgid
                        headers = IndOleng.Talk.Headers
                        r = requests.get(fotoo, headers=headers, stream=True)
                        if r.status_code == 200:
                            OtongAbi = os.path.join(os.path.dirname(__file__), 'dataPhotos/%s.jpg' % TeamBotsOLENGKILLER["Img"])
                            with open(OtongAbi, 'wb') as fp:
                                shutil.copyfileobj(r.raw, fp)
                            IndOleng.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ɢᴀᴍʙᴀʀ")
                        TeamBotsOLENGKILLER["Img"] = {}
                        TeamBotsOLENGKILLER["TambahFoto"] = False

               if msg.toType == 2:
                 if msg._from in MyAbiBossKu:
                   if TeamBotsOLENGKILLER["Gfoto"] == True:
                     OtongAbi = IndOleng.downloadObjectMsg(msg_id)
                     TeamBotsOLENGKILLER["Gfoto"] = False
                     IndOleng.updateGroupPicture(msg.to, OtongAbi)
                     IndOleng.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜʙᴀʜ ғᴏᴛᴏ ɢʀᴏᴜᴘ")

               if msg.contentType == 1:
                   if msg._from in MyAbiBossKu:
                       if AbiJomblo in TeamBotsOLENGKILLER["Abifoto"]:
                            AbiGanteng = IndOleng.downloadObjectMsg(msg_id)
                            del TeamBotsOLENGKILLER["Abifoto"][AbiJomblo]
                            IndOleng.updateProfilePicture(AbiGanteng)
                            IndOleng.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                        if OlengAss in TeamBotsOLENGKILLER["Abifoto"]:
                            AbiOlenk = AssOleng.downloadObjectMsg(msg_id)
                            del TeamBotsOLENGKILLER["Abifoto"][OlengAss]
                            AssOleng.updateProfilePicture(AbiOlenk)
                            AssOleng.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                        if AjsAbi in TeamBotsOLENGKILLER["Abifoto"]:
                            AbiMuhazirin = AntiJsOleng.downloadObjectMsg(msg_id)
                            del TeamBotsOLENGKILLER["Abifoto"][AjsAbi]
                            AntiJsOleng.updateProfilePicture(AbiMuhazirin)
                            AntiJsOleng.sendMessage(msg.to,"🔹ғᴏᴛᴏ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                   if TeamBotsOLENGKILLER["GantiFoto"] == True:
                     KontolMuhazir = IndOleng.downloadObjectMsg(msg_id)
                     TeamBotsOLENGKILLER["GantiFoto"] = False
                     IndOleng.updateProfilePicture(KontolMuhazir)
                     IndOleng.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                   if TeamBotsOLENGKILLER["GantiFoto"] == True:
                     KontolAbi = AssOleng.downloadObjectMsg(msg_id)
                     TeamBotsOLENGKILLER["GantiFoto"] = False
                     AssOleng.updateProfilePicture(KontolAbi)
                     AssOleng.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")
                     
               if msg.contentType == 1:
                 if msg._from in MyAbiBossKu:
                   if TeamBotsOLENGKILLER["GantiFoto"] == True:
                     KontolOleng = AntiJsOleng.downloadObjectMsg(msg_id)
                     TeamBotsOLENGKILLER["GantiFoto"] = False
                     AntiJsOleng.updateProfilePicture(KontolOleng)
                     AntiJsOleng.sendMessage(msg.to, "🔹ғᴏᴛᴏ ʙᴏᴛ ᴅᴏɴᴇ ᴅɪ ʀᴜʙᴀʜ")

               if msg.contentType == 0:
                    if TeamBotsOLENGKILLER["MataOleng"] == True:
                        IndOleng.sendChatChecked(msg.to, msg_id)
                    if text is None:
                        return
                    else:
                        AbiOlengOK = TeamProtectOlengKiller(text)
                        if AbiOlengOK == "menu":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               CmdOleng = AbiHelp()
                               IndOleng.sendMessage(msg.to, str(CmdOleng))
                                                                                       
                        if AbiOlengOK == "oleng on":
                            if msg._from in MyAbiBossKu:
                                OLENGIN["OlengPro"] = True
                                IndOleng.sendMessage(msg.to, "🔹ᴛᴇᴍᴘʟᴀᴛᴇ ᴀᴋᴛɪғ ʙᴏssᴋᴜ")

                        elif AbiOlengOK == "help":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu or msg._from in MyAbiBossKu:
                               IndOleng.sendMessage(msg.to, "╭──────╮\n├🔹OLenG\n╰──────╯\n╭──────╮\n├🔹ʜᴇʟᴘ\n├🔹ᴍᴇɴᴜ\n╰──────╯\n╭──────╮\n├  Muhazir\n╰──────╯")
 
                        elif AbiOlengOK == "oleng off":
                            if msg._from in MyAbiBossKu:
                                OLENGIN["OlengPro"] = False
                                IndOleng.sendMessage(msg.to, "ᴛᴇᴍᴘʟᴀᴛᴇ ᴏғғ ʙᴏssᴋᴜ")
                        
                        elif AbiOlengOK.startswith("bc "):
                           if msg._from in MyAbiBosKu:
                             sambungan = text.split(" ")
                             OKwifi = text.replace(sambungan[0] + " ","")
                             MuhazirAlwi = IndOleng.getGroupIdsJoined()
                             for GOlengKiller in MuhazirAlwi:
                                abii = IndOleng.getContact(AbiJomblo)
                                OK = ""
                                AOK = ""
                                TOK = []
                                AtasAbi =  "ʙʀᴏᴀᴅᴄᴀsᴛ ʙʏᴇ "
                                Luruskan = "{}".format(str(OKwifi))
                                ry = str(abii.displayName)
                                AbiOrder = ''
                                AbiJalan = AbiOrder+"@x\n"
                                Jos = str(len(AOK)+len(AtasAbi))
                                Joss = str(len(AOK)+len(AbiJalan)+len(AtasAbi)-1)
                                OK = {'S':Jos, 'E':Joss, 'M':abii.mid}
                                TOK.append(OK)
                                AOK += AbiJalan
                                Menurun = AtasAbi + AOK + Luruskan + ""
                                IndOleng.sendMessage(GOlengKiller, Menurun, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(TOK).replace(' ','')+'}')}, contentType=0)
                                
                        elif AbiOlengOK == "asem" or text.lower() == 'asemmm' or text.lower() == 'sem' or text.lower() == 'semm':
                          if OLENGIN["OlengPro"] == True:                            
                               IndOleng.sendMessage(msg.to, "ᴋᴇᴛᴀʜᴜᴀɴ ʟᴜ ᴋᴀᴋ ʙᴇʟᴜᴍ ᴍᴀɴᴅɪ ᴘᴀɴᴛᴇsᴀɴ ʙᴀᴜ ᴀssᴇᴇᴇᴍᴍ😂")

                        elif AbiOlengOK == "pekok" or text.lower() == 'pekokkk':
                          if OLENGIN["OlengPro"] == True:                            
                               IndOleng.sendMessage(msg.to, "sᴇsᴀᴍᴀ ᴘᴇᴋᴏᴋ ᴅɪ ʟᴀʀɪɴɢ ᴄᴏʟʟʏ😃😃")

                        elif AbiOlengOK == "sue":
                          if OLENGIN["OlengPro"] == True:       
                               IndOleng.sendMessage(msg.to, "ᴇᴍᴀɴɢ ᴜᴅᴀʜ sᴜᴇ ᴘᴜɴʏᴀ ᴋᴋ, ᴋᴀʟᴏ ɢᴀᴋ sᴜᴇ, ɢᴀᴋ ʙᴀᴋᴀʟᴀɴ ʙɪsᴀ ᴅɪ ᴛᴜsᴜᴋ ᴀɴᴜ ᴋᴋ😂")
                             
                        elif AbiOlengOK == "dudul" or text.lower() == 'pea':
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, "sᴇsᴀᴍᴀ ᴅᴜᴅᴜʟ ᴊᴀɴɢᴀɴ sᴀʟɪɴɢ ʙᴜʟʟʏ ᴋᴋ😂, ᴅɪ ʙᴀᴡᴀʜ ᴍᴜ ᴊᴜɢᴀ ᴜᴅᴀʜ ɢᴜɴᴅᴜʟ ᴋᴋ 😜")
                        
                        elif AbiOlengOK == "typo" or text.lower() == 'typo':
                          if OLENGIN["OlengPro"] == True:            
                               IndOleng.sendMessage(msg.to, "ᴛʏᴘᴏ ᴍᴜʟᴜ sɪʜ, ᴊᴀʀɪ ᴊᴇᴍᴘᴏʟ sᴇᴍᴜᴀ sᴏᴀʟ ɴʏᴀ😂")
                        
                        elif AbiOlengOK == "aduh" or text.lower() == 'waduh':
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "ᴡᴀᴅᴜʜ ᴋᴇɴᴀᴘᴀ ᴋᴋ\nᴋᴇᴊᴇᴅᴏᴛ ᴘɪɴᴛᴜ ʏᴀ. ᴇᴍᴀɴɢ ᴇɴᴀᴋ😂")
                               
                        elif AbiOlengOK == "hus" or text.lower() == 'huss':
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "ᴅɪ ʟᴀʀᴀɴɢ ʙʀɪsɪᴋ ᴅɪ ʀᴏᴏᴍ ɪɴɪ ʙᴀɴʏᴀᴋ ʏᴀɴɢ ᴏʟᴇɴɢ😂")
                               
                        elif AbiOlengOK == "pm":
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "sᴏʀʀʏ ᴀᴋᴜ ᴛɪᴅᴀᴋ ɴᴇʀɪᴍᴀ ᴘᴍ ᴏʀᴀɴɢ ᴊᴏᴍʙʟᴏ ɴɢᴇɴᴇs😜")

                        elif text.lower() == "midku":
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, msg._from)
                               
                        elif AbiOlengOK == "ngopi" or text.lower() == 'ngopi susu guys':
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ɴɢᴏᴘɪ ʙᴇʟᴜᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴋᴋ ɴʏᴜsᴜ ʙᴀʀᴇɴɢ 😜")
                               
                        elif AbiOlengOK == "nah" or text.lower() == 'nahhh':
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "ɴᴀʜ ɴᴏʜ ɴᴀʜ ɴᴏʜ\nᴘᴀʟᴀᴋ ᴋᴜ ᴍᴜᴍᴇᴛ\nᴋʟᴏ ʟᴜ ʙɪʟᴀɴɢ ɴᴀʜ ɴᴏʜ😂")
                               
                        elif AbiOlengOK == "salken":
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, "sᴀʟᴋᴇɴᴊᴜ ᴋᴋ\nsᴇᴍᴏɢᴀ ᴀᴡᴀʟ ᴋɪᴛᴀ ᴋᴇɴᴀʟ\nʙɪsᴀ ᴊᴀᴅɪ ᴊᴏᴅᴏʜ ʏᴀ ᴋᴋ😍")
                               
                        elif AbiOlengOK == "bomat":
                          if OLENGIN["OlengPro"] == True:        
                               IndOleng.sendMessage(msg.to, "ᴀᴋᴜ ᴍᴀʜ ʙᴏᴅᴏʜ ᴀᴍᴀᴛ\nᴇᴍᴀɴɢ ɴʏᴀ ʟᴜ sɪᴀᴘᴀ😂")
                               
                        elif AbiOlengOK == "cipok":
                          if OLENGIN["OlengPro"] == True:    
                               IndOleng.sendMessage(msg.to, "ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ ᴄɪᴘᴏᴋ\nᴋᴇɴᴄɪɴɢ ʟᴜ ᴀᴊᴀ ᴍᴀsɪʜ ɢᴋ ʟᴜʀᴜs\nᴍᴀᴜ ᴄɪᴘᴏᴋ ᴏʀᴀɴɢ😜")

                        elif AbiOlengOK == "janda":
                          if OLENGIN["OlengPro"] == True:          
                               IndOleng.sendMessage(msg.to, "ᴇᴍᴀɴɢ ᴋᴀᴜ ᴊᴀɴᴅᴀ ᴋᴋ\nᴇᴍᴀɴɢ ᴍᴀᴜ sᴀᴍᴀ ᴊᴀɴᴅᴀ ᴀɴᴀᴋ 3 ᴋᴋ\nᴛᴀᴘɪ sᴀʏᴀɴɢ ᴜᴅᴀʜ ᴀɴᴜ ᴘᴜɴʏᴀ ᴋᴋ 😂")

                        elif AbiOlengOK == "duda":
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, "ᴇᴍᴀɴɢ ᴀᴋᴜ ᴅᴜᴅᴀ ᴋᴋ,,,\nᴋʟᴏ ᴋᴋ ᴍᴀᴜ ᴀᴍᴀ ᴅᴜᴅᴀ\nᴀʏᴜᴋ ᴋɪᴛᴀ ᴊᴀᴅɪᴀɴ😂")

                        elif AbiOlengOK == "salam":
                          if OLENGIN["OlengPro"] == True:                      
                               IndOleng.sendMessage(msg.to, "السَّلاَمُ عَلَيْكُمْ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ")

                        elif AbiOlengOK == "bot":
                          if OLENGIN["OlengPro"] == True: 
                               IndOleng.sendMessage(msg.to, "ʙᴀᴛ ʙᴏᴛ ʙᴀᴛ ʙᴏᴛ ᴍᴀᴛᴀᴍᴜ ɪᴛᴜ ʙᴏᴛ\nᴀᴋᴜ ᴍᴀʜ ʙᴜᴋᴀɴ ʙᴏᴛ\nᴛᴀᴘɪ ʙᴀᴘᴀᴋᴇ ʙᴏᴛ 😜")

                        elif AbiOlengOK == "siang":
                          if OLENGIN["OlengPro"] == True:    
                               IndOleng.sendMessage(msg.to, "sɪᴀɴɢ ᴊᴜɢᴀ ᴋᴋ ᴋᴜ sʏᴀɴᴛɪᴋ, ᴜᴅᴀʜ ᴅᴀᴘᴀᴛ ᴛɪᴋᴜɴɢᴀɴ ʙᴇʟᴜᴍ ᴋᴋ 😅")

                        elif AbiOlengOK == "pagi":
                          if OLENGIN["OlengPro"] == True:       
                               IndOleng.sendMessage(msg.to, "ᴘᴀɢɪ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ sᴀʀᴀᴘᴀɴ ʙᴇʟᴜᴍ 😘")

                        elif AbiOlengOK == "sore":
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "sᴏʀᴇ ᴊᴜɢᴀ ᴋᴋ, ᴜᴅᴀʜ ᴍᴀɴᴅɪ ʙᴇʟᴜᴍ, ᴋᴀʟᴏ ʙᴇʟᴜᴍ sɪɴɪ ᴀᴋᴜ ᴛᴇᴍᴇɴɪ ᴋᴋ ᴍᴀɴᴅɪ 🤗هُ")

                        elif AbiOlengOK == "malam":
                          if OLENGIN["OlengPro"] == True:       
                               IndOleng.sendMessage(msg.to, "ᴍᴀʟᴀᴍ ᴊᴜɢᴀ ᴋᴋ, ᴡᴀᴋᴛᴜ ɴʏᴀ ɴɪᴋᴜɴɢ ᴇɴᴀᴋ ɴʏᴀ ᴍᴀʟᴀᴍ-ᴍᴀʟᴀᴍ ɢɪɴɪ ᴋᴋ 😛")

                        elif AbiOlengOK == "kojom":
                          if OLENGIN["OlengPro"] == True:                
                               IndOleng.sendMessage(msg.to, "ɴᴀʜ ᴋᴀɴ,,,ɴɢᴀᴊᴀᴋɪɴ ᴋᴏᴊᴏᴍ,,,ɴᴛᴀʀ ʙᴏᴊᴏɴᴇ ᴍᴀʀᴀʜ ʙᴀʀᴜ ᴛᴀᴜ ʀᴀsᴀ ᴋᴋ 😜هُ")

                        elif AbiOlengOK == "nikung":
                          if OLENGIN["OlengPro"] == True:              
                               IndOleng.sendMessage(msg.to, "ᴀʏᴜᴋ ᴋᴋ ᴋɪᴛᴀ ɴɪᴋᴜɴɢ, ʟᴀɴɢsᴜɴɢ ᴘᴍ ᴀᴊᴀ ʏᴀ ᴋᴋ😂")

                        elif AbiOlengOK == "assalamualaikum" or text.lower() == 'asalamualaikum':
                          if OLENGIN["OlengPro"] == True:             
                               IndOleng.sendMessage(msg.to, "وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِ وَبَرَكَاتُهُ  ")

                        elif AbiOlengOK == "susu" or text.lower() == 'nyusu':
                          if OLENGIN["OlengPro"] == True:           
                               IndOleng.sendMessage(msg.to, "sᴜsᴜ sᴜsᴜ sᴜsᴜ, ᴅᴀʀɪ ᴋᴇᴄɪʟ ʟᴜ sᴜᴅᴀʜ ᴅɪ ɴʏᴜsᴜɪɴ, ᴍᴀsᴀ ᴍɪɴᴛᴀ ɴʏᴜsᴜ sᴀᴍᴀ ʀᴏɴᴅᴏ ᴋᴋ😂")

                        elif AbiOlengOK == "setan":
                          if OLENGIN["OlengPro"] == True:      
                               IndOleng.sendMessage(msg.to, "sᴇᴛᴀɴ sᴇᴛᴀɴ sᴇᴛᴀɴ, ᴇᴍᴀɴɢ ᴍᴜᴋᴀ ʟᴜ ᴋᴀʏᴀᴋ sᴇᴛᴀɴ ᴋᴋ😂")

                        elif AbiOlengOK == "makan":
                          if OLENGIN["OlengPro"] == True:         
                               IndOleng.sendMessage(msg.to, "ᴜᴅᴀʜ ᴘᴀᴅᴀ ᴍᴀᴋᴀɴ ʙᴇʟᴏᴍ ᴋᴋ, ᴋᴀʟᴏ ʙᴇʟᴏᴍ sɪɴɪ ᴀᴋᴜ sᴜᴀᴘɪɴ ᴋᴋ")

                        elif AbiOlengOK == "minum":
                          if OLENGIN["OlengPro"] == True:   
                               IndOleng.sendMessage(msg.to, "sɪɴɪ ᴋᴋ ᴍɪɴᴜᴍ ʙᴀʀᴇɴɢ ᴋɪᴛᴀ😛")

                        elif AbiOlengOK == "bank":
                          if OLENGIN["OlengPro"] == True:
                               IndOleng.sendMessage(msg.to, "ᴘᴀʏᴍᴇɴᴛ ᴠɪᴀ ʙᴀɴᴋ\nɴᴏ ʀᴇᴋ : 481901020711531\nᴀᴛᴀs ɴᴀᴍᴀ : muhazir\nʙᴀɴᴋ ʙʀɪ\n\nᴠɪᴀ ᴘᴜʟsᴀ\n08992906209 ")

                        elif AbiOlengOK == "wa'alaikumsalam" or text.lower() == 'waalaikumsalam':
                          if OLENGIN["OlengPro"] == True: 
                               IndOleng.sendMessage(msg.to, "ɴᴀʜ ɢɪᴛᴜ ᴊᴀᴡᴀʙ sᴀʟᴀᴍ sᴇsᴀᴍᴀ ᴍᴜsʟɪᴍ😘😍")

                        elif AbiOlengOK == "jande":
                          if OLENGIN["OlengPro"] == True:          
                               IndOleng.sendMessage(msg.to, "nyaman nyaman nyaman nyaman nyaman nyaman    ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.👿.👿.👿 ❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.\n❌.👁️.★.★.★.👁️.❌.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.0.S.1.☆.👿.👿.👿.")

                        elif AbiOlengOK == "aby":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                  AbiOleNgKiller(to)
                                  
                        elif AbiOlengOK == "/me" or text.lower() == '/gue':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                msg.contentType = 13
                                msg.contentMetadata = {'mid': mid}
                                IndOleng.sendContact(to, mid)

                        elif "autoreject " in msg.text.lower():
                            peler = msg.text.lower()
                            pepek = peler.replace("autoreject ","")
                            if pepek == "off":
                                TeamBotsOLENGKILLER['BatalinUndangan'] = False
                                IndOleng.sendMessage(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏғғ ɢᴀᴋ ᴀᴍᴀɴ ᴅᴀᴅɪ sᴘᴀᴍ")
                            elif pepek == "on":
                                TeamBotsOLENGKILLER['BatalinUndangan'] = True
                                IndOleng.sendMessage(msg.to,"ᴀᴜᴛᴏʀᴇᴊᴇᴄᴛ ᴏɴ ᴀᴍᴀɴ ᴅᴀʀɪ sᴘᴀᴍ")
                        
                        elif text.lower() == "mid":
                               IndOleng.sendMessage(msg.to, msg._from)

                        elif ("Mid " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               OlengMin = eval(msg.contentMetadata["MENTION"])
                               OlengFles = OlengMin["MENTIONEES"][0]["M"]
                               OKB = IndOleng.getContact(OlengFles)
                               IndOleng.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(OKB.displayName)+"\nᴍɪᴅ : " +OlengFles)
                               IndOleng.sendMessage(msg.to, None, contentMetadata={'u03addfbbbdb20585381383e5d173d28d': OlengFles}, contentType=13)

                        elif ("Info " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               OlengMin = eval(msg.contentMetadata["MENTION"])
                               OlengFles = OlengMin["MENTIONEES"][0]["M"]
                               OKs = IndOleng.getContact(OlengFles)
                               IndOleng.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(OKs.displayName)+"\nᴍɪᴅ : " +OlengFles+"\nsᴛᴀᴛᴜs ᴍsɢ"+str(OKs.statusMessage))
                               IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': OlengFles}, contentType=13)
                               if "videoProfile='{" in str(IndOleng.getContact(OlengFles)):
                                   IndOleng.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(OKs.picturePath)+'/vp.small')
                               else:
                                   IndOleng.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(OKs.picturePath))

                        elif AbiOlengOK == "mybot":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': AbiJomblo}
                               IndOleng.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': OlengAss}
                               IndOleng.sendMessage1(msg)
                               msg.contentType = 13
                               msg.contentMetadata = {'mid': AjsAbi}
                               IndOleng.sendMessage1(msg)

                        elif text.lower() == "hapuschat":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               try:
                                   IndOleng.removeAllMessages(op.param2)
                                   IndOleng.sendMessage(msg.to,"🔹ʜᴀᴘᴜs ᴄʜᴀᴛ ᴅᴏɴᴇ")
                               except:
                                   pass
                                   
                        elif text.lower() == "mykey":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               IndOleng.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(TeamBotsOLENGKILLER["KunciOleng"]) + " 」")
                               
                        elif AbiOlengOK.startswith("setkey "):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               Colokan = text.split(" ")
                               Memek = text.replace(Colokan[0] + " ","")
                               if Memek in [""," ","\n",None]:
                                   IndOleng.sendMessage(msg.to, "🔹ɢᴀɢᴀʟ ᴍᴇɴɢɢᴀɴᴛɪ ᴋᴇʏ")
                               else:
                                   TeamBotsOLENGKILLER["KunciOleng"] = str(Memek).lower()
                                   IndOleng.sendMessage(msg.to, "🔹sᴇᴛᴋᴇʏ\n🔹ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ「{}」".format(str(Memek).lower()))

                        elif text.lower() == "resetkey":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosku:
                               TeamBotsOLENGKILLER["KunciOleng"] = ""
                               IndOleng.sendMessage(msg.to, "🔹sᴇᴛᴋᴇʏ\n🔹ᴋᴇᴍʙᴀʟɪ ᴋᴇ ᴀᴡᴀʟ")

                        elif AbiOlengOK == "restart":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               IndOleng.sendMessage(msg.to, "🔹ᴡᴀɪᴛ....")
                               TeamBotsOLENGKILLER["Reboot"] = msg.to
                               RebootBot()
                               IndOleng.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ʀᴇsᴛᴀʀᴛ...")
                            
                        elif AbiOlengOK == "time":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               eltime = time.time() - mulai
                               Ngocok = "🔹ʙᴏᴛ ᴀᴋᴛɪғ sᴇʟᴀᴍᴀ\n" +waktu(eltime)
                               IndOleng.sendMessage(msg.to,Ngocok)
                            
                        elif AbiOlengOK == "ginfo":
                          if msg._from in MyAbiBosKu:
                            try:
                                OK = IndOleng.getGroup(msg.to)
                                if OK.invitee is None:
                                    OlengGC = "0"
                                else:
                                    OlengGC = str(len(OK.invitee))
                                if OK.preventedJoinByTicket == True:
                                    GcOleng = "🔹ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    OlengGc = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    GcOleng = "🔹ᴛᴇʀʙᴜᴋᴀ"
                                    OlengGc = "https://line.me/R/ti/g/{}".format(str(IndOleng.reissueGroupTicket(OK.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(OK.createdTime) / 1000)))
                                IndOleng.sendMessage(msg.to, "🔹ᴏʟᴇɴɢ ᴋɪʟʟᴇʀ🔹ɢʀᴜᴘ ɪɴғᴏ\n\n🔹ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(OK.name)+ "\n🔹ɪᴅ ɢʀᴜᴘ : {}".format(OK.id)+ "\n🔹ᴘᴇᴍʙᴜᴀᴛ : {}".format(OK.creator.displayName)+ "\n🔹ᴡᴀᴋᴛᴜ ᴅɪ ʙᴜᴀᴛ : {}".format(str(timeCreated))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(OK.members)))+ "\n🔹ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(OlengGC)+ "\n🔹ɢʀᴜᴘ ǫʀ : {}".format(GcOleng)+ "\n??ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(OlengGc))
                                IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': OK.creator.mid}, contentType=13)
                            except Exception as e:
                                IndOleng.sendMessage(msg.to, str(e))

                        elif AbiOlengOK.startswith("infogrup "):
                          if msg._from in MyAbiBosKu:
                            Puki = text.split(" ")
                            AbyOleng = text.replace(Puki[0] + " ","")
                            JalurMuhazir = IndOleng.getGroupIdsJoined()
                            JalurAbi = ""
                            try:
                                Gila = JalurMuhazir[int(AbyOleng)-1]
                                OK = IndOleng.getGroup(Gila)
                                try:
                                    GColeng = OK.creator.displayName
                                except:
                                    GColeng = "🔹ᴛɪᴅᴀᴋ ᴅɪ ᴛᴇᴍᴜᴋᴀɴ"
                                if OK.invitee is None:
                                    GcOleng = "0"
                                else:
                                    GcOleng = str(len(OK.invitee))
                                if OK.preventedJoinByTicket == True:
                                    OlengGc = "🔹ᴛᴇʀᴛᴜᴛᴜᴘ"
                                    OlengGC = "♦️ᴛɪᴅᴀᴋ ᴀᴅᴀ"
                                else:
                                    OlengGc = "🔹ᴛᴇʀʙᴜᴋᴀ"
                                    OlengGC = "https://line.me/R/ti/g/{}".format(str(IndOleng.reissueGroupTicket(OK.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(OK.createdTime) / 1000)))
                                JalurAbi += "🔹ᴄᴍᴅ ɢʀᴜᴘ ɪɴғᴏ🔹\n"
                                JalurAbi += "\n🔹ɴᴀᴍᴀ ɢʀᴜᴘ : {}".format(OK.name)
                                JalurAbi += "\n🔹ɪᴅ ɢʀᴜᴘ : {}".format(OK.id)
                                JalurAbi += "\n🔹ᴘᴇᴍʙᴜᴀᴛ : {}".format(GColeng)
                                JalurAbi += "\n🔹ᴡᴀᴋᴛᴜ ᴅɪʙᴜᴀᴛ : {}".format(str(timeCreated))
                                JalurAbi += "\n🔹ᴊᴜᴍʟᴀʜ ᴀɴɢɢᴏᴛᴀ : {}".format(str(len(OK.members)))
                                JalurAbi += "\n🔹ᴊᴜᴍʟᴀʜ ᴘᴇɴᴅɪɴɢᴀɴ : {}".format(GcOleng)
                                JalurAbi += "\n🔹ɢʀᴜᴘ ǫʀ : {}".format(OlengGc)
                                JalurAbi += "\n🔹ɢʀᴜᴘ ᴛɪᴄᴋᴇᴛ : {}".format(OlengGC)
                                JalurAbi += ""
                                IndOleng.sendMessage(to, str(JalurAbi))
                            except:
                                pass

                        elif AbiOlengOK.startswith("infomem "):
                          if msg._from in MyAbiBosKu:
                            TEAM = msg.text.split(" ")
                            BOTS = msg.text.replace(TEAM[0] + " ","")
                            OLENGKILLER = IndOleng.getGroupIdsJoined()
                            ABIE = ""
                            try:
                                TEAMOK = OLENGKILLER[int(BOTS)-1]
                                OLENG = IndOleng.getGroup(TEAMOK)
                                KILLER = 0
                                ABIE = ""
                                for MUHAZIR in OLENG.members:
                                    KILLER += 1
                                    ABIE += "\n " "├🔹"+ str(KILLER) + ". " + MUHAZIR.displayName
                                IndOleng.sendMessage(to," 🔹ɢʀᴜᴘ ɴᴀᴍᴇ : [ " + str(OLENG.name) + " ]\n\n   [ʟɪsᴛ ᴀɴɢɢᴏᴛᴀ ]\n" + ABIE + "\n🔹ᴛᴏᴛᴀʟ %i ᴀɴɢɢᴏᴛᴀ🔹" % len(OLENG.members))
                            except: 
                                pass

                        elif AbiOlengOK == "flist":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               ABI = ""
                               MUHAZIR = 0
                               ALWI = IndOleng.getAllContactIds()
                               for BOTOL in ALWI:
                                   TEAM = IndOleng.getContact(BOTOL)
                                   MUHAZIR = MUHAZIR + 1
                                   end = "\n"
                                   ABI += "├🔹" + str(MUHAZIR) + ". " +TEAM.displayName+ "\n"
                               IndOleng.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ABI+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(ALWI))+"ɢʀᴏᴜᴘ🔹")

                        elif AbiOlengOK == "glist":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               ABI = ""
                               MUHAZIR = 0
                               ALWI = IndOleng.getGroupIdsJoined()
                               for BOTOL in ALWI:
                                   TEAM = IndOleng.getGroup(BOTOL)
                                   MUHAZIR = MUHAZIR + 1
                                   end = "\n"
                                   ABI += "├🔹" + str(MUHAZIR) + ". " +TEAM.name+ "\n"
                               IndOleng.sendMessage(msg.to,"╭── 🔹ɢʀᴏᴜᴘ ʟɪsᴛ🔹\n│\n"+ABI+"│\n╰──🔹ᴛᴏᴛᴀʟ"+str(len(ALWI))+"ɢʀᴏᴜᴘ🔹")

                        elif AbiOlengOK == "buka":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                if msg.toType == 2:
                                   Otong = IndOleng.getGroup(msg.to)
                                   Otong.preventedJoinByTicket = False
                                   IndOleng.updateGroup(Otong)
                                   IndOleng.sendMessage(msg.to, "🔹ᴏᴘᴇɴ ᴜʀʟ")

                        elif AbiOlengOK == "tutup":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                if msg.toType == 2:
                                   Otong = IndOleng.getGroup(msg.to)
                                   Otong.preventedJoinByTicket = True
                                   IndOleng.updateGroup(Otong)
                                   IndOleng.sendMessage(msg.to, "🔹ᴄʟᴏsᴇ ᴜʀʟ")

                        elif AbiOlengOK == "url grup":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                if msg.toType == 2:
                                   Puki = IndOleng.getGroup(msg.to)
                                   if Puki.preventedJoinByTicket == True:
                                      Puki.preventedJoinByTicket = False
                                      IndOleng.updateGroup(Puki)
                                   Busuk = IndOleng.reissueGroupTicket(msg.to)
                                   IndOleng.sendMessage(msg.to, "ɴᴀᴍᴀ : "+str(Puki.name)+ "\nᴜʀʟ ɢʀᴜᴘ : http://line.me/R/ti/g/"+Busuk)
#===========BOT UPDATE============#
                        elif AbiOlengOK == "upgrup":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                              if msg.toType == 2:
                                TeamBotsOLENGKILLER["Gfoto"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif AbiOlengOK == "upbot":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                TeamBotsOLENGKILLER["GantiFoto"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif AbiOlengOK == "cp":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                TeamBotsOLENGKILLER["Abifoto"][AbiJomblo] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif AbiOlengOK == "cp1":
                            if msg._from in MyAbiBosKu:
                                TeamBotsOLENGKILLER["Abifoto"][AjsAbi] = True
                                AssOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")
                                
                        elif AbiOlengOK == "cp2":
                            if msg._from in MyAbiBosKu:
                                TeamBotsOLENGKILLER["Abifoto"][AjsAbi] = True
                                AntiJsOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ғᴏᴛᴏɴʏᴀ")

                        elif AbiOlengOK.startswith("cn: "):
                          if msg._from in MyAbiBosKu:
                            CnOleng = msg.text.split(" ")
                            CNOleng = msg.text.replace(CnOleng[0] + " ","")
                            if len(CNOleng) <= 10000000000:
                                Selfi = IndOleng.getProfile()
                                Selfi.displayName = CNOleng
                                IndOleng.updateProfile(Selfi)
                                IndOleng.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + CNOleng + "")

                        elif AbiOlengOK.startswith("cn1: "):
                          if msg._from in MyAbiBosKu:
                            Memek = msg.text.split(" ")
                            Busuk = msg.text.replace(Memek[0] + " ","")
                            if len(Busuk) <= 10000000000:
                                Selfi = AssOleng.getProfile()
                                Selfi.displayName = Busuk
                                AssOleng.updateProfile(Selfi)
                                AssOleng.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + Busuk + "")
                                
                        elif AbiOlengOK.startswith("cn2: "):
                          if msg._from in MyAbiBosKu:
                            Peler = msg.text.split(" ")
                            Colly = msg.text.replace(Peler[0] + " ","")
                            if len(Colly) <= 10000000000:
                                AbiMuhazir = AntiJsOleng.getProfile()
                                AbiMuhazir.displayName = Colly
                                AntiJsOleng.updateProfile(AbiMuhazir)
                                AntiJsOleng.sendMessage(msg.to,"🔹ɴᴀᴍᴀ ᴅɪ ɢᴀɴᴛɪ ᴊᴀᴅɪ " + Colly + "")

#===========BOT UPDATE============#
                        elif AbiOlengOK == "hi" or text.lower() == 'ange':
                           if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                             PasukanAbi = IndOleng.getGroup(msg.to)
                             TeamAbiOleng = [contact.mid for contact in PasukanAbi.members]
                             BotsOleng = len(TeamAbiOleng)//20
                             for TeamProOleng in range(BotsOleng+1):
                                 oke = u''
                                 BOK=0
                                 BosAbi=[]
                                 for Sangek in PasukanAbi.members[TeamProOleng*20 : (TeamProOleng+1)*20]:
                                     BosAbi.append({"S":str(BOK), "E" :str(BOK+6), "M":Sangek.mid})
                                     BOK += 7
                                     oke += u'@AbiOleng \n'
                                 IndOleng.sendMessage(msg.to, text=oke, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':BosAbi})}, contentType=0)

                        elif AbiOlengOK == "listbot":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                Anjay = ""
                                Buronan = 0
                                for Target in Bots:
                                    Buronan = Buronan + 1
                                    end = '\n'
                                    Anjay += str(Buronan) + ". " +IndOleng.getContact(Target).displayName + "\n"
                                IndOleng.sendMessage(msg.to,"🔹ʟɪsᴛ ʙᴏᴛ\n\n"+Anjay+"\n🔹ᴛᴏᴛᴀʟ ʙᴏᴛ ʟᴇᴏ「%s」" %(str(len(Bots))))

                        elif AbiOlengOK == "ladmin":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                ABI = ""
                                MUHAZIR = ""
                                ALWI = ""
                                Aku = 0
                                Cinta = 0
                                Kamu = 0
                                for TeamSolidOleng in owner:
                                    Aku = Aku + 1
                                    end = '\n'
                                    ABI += str(Aku) + ". " +IndOleng.getContact(TeamSolidOleng).displayName + "\n"
                                for TeamSolidOleng in MyAbiBossKu:
                                    Cinta = Cinta + 1
                                    end = '\n'
                                    MUHAZIR += str(Cinta) + ". " +IndOleng.getContact(TeamSolidOleng).displayName + "\n"
                                IndOleng.sendMessage(msg.to,"♦️ᴀᴅᴍɪɴ ᴀʙɪ\n\n♦️sᴜᴘᴇʀ ᴀᴅᴍɪɴ :\n"+ABI+"\n♦️ᴀᴅᴍɪɴ :\n"+MUHAZIR+"\n♦️ᴊᴜᴍʟᴀʜ ᴀᴅᴍɪɴ ᴀʙɪ「%s」♦️" %(str(len(owner)+len(MyAbiBossKu))))
#======TEAM OLENG KILLER============================
                        elif AbiOlengOK == "abigo":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                try:
                                    IndOleng.findAndAddContactsByMid(OlengAss)
                                    IndOleng.findAndAddContactsByMid(AjsAbi)
                                    OlengBotz = [OlengAss,AjsAbi]
                                    IndOleng.inviteIntoGroup(msg.to, OlengBotz)
                                    AssOleng.acceptGroupInvitation(msg.to)
                                    time.sleep(0.3)
                                    IndOleng.sendMessage(msg.to,PasukanOlengKiller)
                                    AssOleng.sendMessage(msg.to,PasukanOlengKiller)
                                except:
                                    pass
#===========KELUARIN ASSIST=====================================
                        elif AbiOlengOK == "abiout":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                abi = IndOleng.getGroup(msg.to)
                                IndOleng.cancelGroupInvitation(msg.to, [AjsAbi])
                                AssOleng.sendMessage(msg.to,OutAssist)
                                AssOleng.leaveGroup(msg.to)
                                time.sleep(0.3)

                        elif AbiOlengOK == "oleng":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                IndOleng.sendMessage(msg.to,PasukanOlengKiller)
                                AssOleng.sendMessage(msg.to,PasukanOlengKiller)
                                AntiJsOleng.sendMessage(msg.to,PasukanOlengKiller)
                                    
                        elif AbiOlengOK == "stay":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                try:
                                    TeamAbiGuys = IndOleng.getGroup(msg.to)
                                    IndOleng.findAndAddContactsByMid(AjsAbi)
                                    IndOleng.inviteIntoGroup(msg.to, [AjsAbi])
                                    IndOleng.sendMessage(msg.to,"[ ɢʀᴏᴜᴘ ] \n🔹"+str(TeamAbiGuys.name)+"\n 🔹sɪᴀᴘ ʙᴀsᴍɪ ᴋɪᴋɪʟ ᴛᴇᴍᴘᴇ")
                                except:
                                    pass 
                                
                        elif AbiOlengOK == "papay":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                Edan = IndOleng.getGroup(msg.to)
                                IndOleng.sendMessage(msg.to, "🔹ɢᴏᴏᴅ ʙʏᴇ ᴄᴀʏᴀɴᴋ🔹\n       "+str(Edan.name))
                                IndOleng.leaveGroup(msg.to)
                                
                        elif msg.text.lower().startswith("teamadd"):
                           if msg._from in MyAbiBosKu:
                                try:
                                    IndOleng.findAndAddContactsByMid(OlengAss)
                                    IndOleng.findAndAddContactsByMid(AjsAbi)
                                    IndOleng.sendMessage(msg.to,"Success!!!")
                                    AssOleng.findAndAddContactsByMid(AbiJomblo)
                                    AssOleng.findAndAddContactsByMid(AjsAbi)
                                    AssOleng.sendMessage(msg.to,"Success!!!")
                                    AntiJsOleng.findAndAddContactsByMid(OlengAss)
                                    AntiJsOleng.findAndAddContactsByMid(AbiJomblo)
                                    AntiJsOleng.sendMessage(msg.to,"Success!!!")
                                except:
                                    pass
                                
                        elif AbiOlengOK == "js in":
                            if msg._from in MyAbiBosKu:
                                Kimak = IndOleng.getGroup(msg.to)
                                Kau = IndOleng.getGroup(msg.to)
                                Kimak.preventedJoinByTicket = False
                                IndOleng.updateGroup(Kimak)
                                invsend = 0
                                TeamOlengBro = IndOleng.reissueGroupTicket(msg.to)
                                AntiJsOleng.acceptGroupInvitationByTicket(msg.to,TeamOlengBro)
                                Kimak = AntiJsOleng.getGroup(msg.to)
                                Kimak.preventedJoinByTicket = True
                                AntiJsOleng.updateGroup(Kimak)

                        elif AbiOlengOK == "js out":
                            if msg._from in MyAbiBossKu:
                                Anjayy = IndOleng.getGroup(msg.to)
                                AntiJsOleng.leaveGroup(msg.to)
                               
                        elif AbiOlengOK == "speed" or AbiOlengOK == "sp":
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                get_profile_time_start = time.time()
                                get_profile = IndOleng.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                IndOleng.sendMessage(msg.to, "ᴡᴀɪᴛ...")
                                IndOleng.sendMessage(msg.to, "╭───────────────────╮\n          %.10f ʟᴇᴏ\n╰───────────────────╯" % (get_profile_time/3))

                        elif AbiOlengOK.startswith("jumlah: "):
                          if OLENGIN["OlengPro"] == True:
                           if msg._from in MyAbiBossKu:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                TeamBotsOLENGKILLER["RAlimit"] = num
                                IndOleng.sendMessage(msg.to,"🔹ᴛᴏᴛᴀʟ sᴛᴀɢ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif AbiOlengOK.startswith("von: "):
                          if OLENGIN["OlengPro"] == True:
                           if msg._from in MyAbiBossKu:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                OLENGIN["limit"] = num
                                IndOleng.sendMessage(msg.to,"🔹ᴛᴏᴛᴀʟ sᴘᴀᴍᴄᴀʟʟ ᴅɪ ʀᴜʙᴀʜ ᴊᴀᴅɪ " +strnum)

                        elif AbiOlengOK == "call":
                          if OLENGIN["OlengPro"] == True:
                           if msg._from in MyAbiBossKu:
                             if msg.toType == 2:
                                group = IndOleng.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(OLENGIN["limit"])
                                IndOleng.sendMessage(msg.to, "🔹ᴅᴏɴᴇ ᴍᴇɴɢᴜɴᴅᴀɴɢ {} ᴘᴀɴɢɢɪʟᴀɴ ɢʀᴏᴜᴘ".format(str(OLENGIN["limit"])))
                                if jmlh <= 1000:
                                  for x in range(jmlh):
                                     try:
                                        IndOleng.acquireGroupCallRoute(to)
                                        IndOleng.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        IndOleng.sendText(msg.to,str(e))
                                else:
                                    IndOleng.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'cek: ' in msg.text:
                          if OLENGIN["OlengPro"] == True:
                           if msg._from in MyAbiBossKu:
                              msgs = msg.text.replace('cek: ','')
                              conn = IndOleng.findContactsByUserid(msgs)
                              if True:
                                  IndOleng.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#======Team Oleng Protection============
#=========== KICKOUT OP.PARAM2 ============
                        elif ("babat " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Bots:
                                       try:
                                           IndOleng.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Kick " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                               Kontol = eval(msg.contentMetadata["MENTION"])
                               Kontol["MENTIONEES"][0]["M"]
                               KikilReceh = []
                               for Memek in Kontol["MENTIONEES"]:
                                    KikilReceh.append(Memek["M"])
                               for Kikil2020 in KikilRecek:
                                   if Kikil2020 not in Bots:
                                       try:
                                           IndOleng.kickoutFromGroup(msg.to, [Kikil2020])
                                       except:
                                           pass
#===========ADMIN ADD============#
                        elif ("Adda " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           MyAbiBossKu.append(target)
                                           IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Bots.append(target)
                                           IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴᴀᴍʙᴀʜ ʙᴏᴛ🔹")
                                       except:
                                           pass

                        elif ("Ha " in msg.text):
                            if msg._from in MyAbiBosKu:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           MyAbiBossKu.remove(target)
                                           IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in MyAbiBossKu:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Saints:
                                       try:
                                           Bots.remove(target)
                                           IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ᴀᴅᴍɪɴ🔹")
                                       except:
                                           pass

                        elif AbiOlengOK == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in MyAbiBosKu:
                                OLENGIN["AddMyAbiBossKu"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif AbiOlengOK == "admin:off" or text.lower() == 'admin:repeat':
                            if msg._from in MyAbiBosKu:
                                OLENGIN["DellMyAbiBossKu"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif AbiOlengOK == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in MyAbiBosKu:
                                OLENGIN["AddMyBot"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif AbiOlengOK == "bot:off" or text.lower() == 'bot:repeat':
                            if msg._from in MyAbiBosKu:
                                OLENGIN["DellMyBot"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴋɪʀɪᴍ ᴄᴏɴᴛᴀᴄᴛ ɴʏᴀ🔹")

                        elif AbiOlengOK == "refresh" or text.lower() == 'refresh':
                            if msg._from in MyAbiBossKu:
                                OLENGIN["AddMyAbiBossKu"] = False
                                OLENGIN["DellMyAbiBossKu"] = False
                                OLENGIN["AddMyBot"] = False
                                OLENGIN["DellMyBot"] = False
                                OLENGIN["blacklist"] = False
                                IndOleng.sendMessage(msg.to,"🔹sᴜᴅᴀʜ sᴇɢᴀʀ ʙᴏssᴋᴜ🔹")

                        elif AbiOlengOK == "kojoman" or text.lower() == 'adm':
                            if msg._from in MyAbiBossKu:
                                Bojoku = ""
                                for Sayang in MyAbiBossKu:
                                    Bojoku = IndOleng.getContact(i)
                                    IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': Sayang}, contentType=13)

                        elif AbiOlengOK == "bosku" or text.lower() == 'own':
                            if msg._from in MyAbiBossKu:
                                Bojoku = ""
                                for Sayang in MyAbiBossKu:
                                    Bojoku = IndOleng.getContact(i)
                                    IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': Sayang}, contentType=13)

                        elif AbiOlengOK == "co" or text.lower() == 'mybotz':
                            if msg._from in MyAbiBossKu:
                                AbiTeam = ""
                                for OlengKiller in Bots:
                                    AbiTeam = IndOleng.getContact(OlengKiller)
                                    IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': OlengKiller}, contentType=13)

                        elif AbiOlengOK == "contact on" or text.lower() == 'contact on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["contact"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "contact off" or text.lower() == 'contact off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["contact"] = False
                                IndOleng.sendMessage(msg.to,"🔹ᴅᴇᴛᴇᴋsɪ ᴄᴏɴᴛᴀᴄᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "respon on" or text.lower() == 'respon on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["detectMention"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "respon off" or text.lower() == 'respon off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["detectMention"] = False
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏʀᴇsᴘᴏɴ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔹")
                                
                        elif AbiOlengOK == "responpm on" or text.lower() == 'responpm on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["arespon"] = True
                                IndOleng.sendMessage(msg.to,"🔹ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "responpm off" or text.lower() == 'responpm off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["arespon"] = False
                                IndOleng.sendMessage(msg.to,"🔹ʀᴇsᴘᴏɴᴘᴍ ᴅɪ ᴍᴀᴛɪᴋᴀɴ🔹")          

                        elif AbiOlengOK == "autojoin on" or text.lower() == 'autojoin on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                OLENGIN["InviteGrup"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "autojoin off" or text.lower() == 'autojoin off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                                OLENGIN["InviteGrup"] = False
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏ ᴊᴏɪɴ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "autoadd on" or text.lower() == 'autoadd on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["AddTeaman"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "autoadd off" or text.lower() == 'autoadd off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["AddTeaman"] = False
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏᴀᴅᴅ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif AbiOlengOK == "left on" or text.lower() == 'left on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["AutoBaper"] = True
                                IndOleng.sendMessage(msg.to,"🔹ʟᴇғᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "left off" or text.lower() == 'left off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["AutoBaper"] = False
                                IndOleng.sendMessage(msg.to,"🔹ʟᴇғᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif AbiOlengOK == "autoblock on" or text.lower() == 'autoblock on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["autoBlock"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")
                                
                        elif AbiOlengOK == "autoblock off" or text.lower() == 'autoblock off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["autoBlock"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴀᴜᴛᴏʙʟᴏᴄᴋ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")          

                        elif AbiOlengOK == "jointicket on" or text.lower() == 'jointicket on':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["MasukUrl"] = True
                                IndOleng.sendMessage(msg.to,"🔹ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ᴀᴋᴛɪғᴋᴀɴ🔹")

                        elif AbiOlengOK == "jointicket off" or text.lower() == 'jointicket off':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                                OLENGIN["MasukUrl"] = False
                                IndOleng.sendMessage(msg.to,"🔹ᴊᴏɪɴᴛɪᴄᴋᴇᴛ ᴅɪ ɴᴏɴᴀᴋᴛɪғᴋᴀɴ🔹")

#===========COMMAND BLACKLIST============
                        elif AbiOlengOK == "banlist" or text.lower() == 'banlist':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                              if OLENGIN["blacklist"] == {}:
                                IndOleng.sendMessage(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                              else:
                                ma = ""
                                a = 0
                                for m_id in OLENGIN["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +IndOleng.getContact(m_id).displayName + "\n"
                                IndOleng.sendMessage(msg.to,"🔹ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹\n\n"+ma+"\n🔹ᴊᴜᴍʟᴀʜ「%s」ʙʟᴀᴄᴋʟɪsᴛ ᴜsᴇʀ🔹" %(str(len(OLENGIN["blacklist"]))))

                        elif AbiOlengOK == "tersangka" or text.lower() == 'blc':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                              if OLENGIN["blacklist"] == {}:
                                    IndOleng.sendMessage(msg.to,"🔹ᴛɪᴅᴀᴋ ᴀᴅᴀ ʙʟᴀᴄᴋʟɪsᴛ🔹")
                              else:
                                    Pukimak = ""
                                    for Kau in OLENGIN["blacklist"]:
                                        Pukimak = IndOleng.getContact(Kau)
                                        IndOleng.sendMessage(msg.to, None, contentMetadata={'mid': Kau}, contentType=13)

                        elif AbiOlengOK == "clearban" or text.lower() == 'cban':
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBossKu:
                              OLENGIN["blacklist"] = {}
                              BuronanLine = IndOleng.getContacts(OLENGIN["blacklist"])
                              DaftarKikil = "「%i」ᴜsᴇʀ ʙʟᴀᴄᴋʟɪsᴛ" % len(BuronanLine)
                              IndOleng.sendMessage(msg.to,"🔹ᴅᴏɴᴇ ᴍᴇɴɢʜᴀᴘᴜs ʙᴜʀᴏɴᴀɴ🔹\n  "    +DaftarKikil)
                              
                        elif text.lower() == 'bank':
                               IndOleng.sendMessage(msg.to, BankOleng)
#===========JOIN LINK============#
                        elif "/ti/g/" in msg.text.lower():
                          if OLENGIN["OlengPro"] == True:
                            if msg._from in MyAbiBosKu:
                              if TeamBotsOLENGKILLER["MasukUrl"] == True:
                                 Otomatis = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 Masuk = Otomatis.findall(text)
                                 Mencret = []
                                 for Crott in Masuk:
                                     if Crott not in Mencret:
                                        Mencret.append(Crott)
                                 for TeamOlengKiller in Mencret:
                                     AbiMuhajir = IndOleng.findGroupByTicket(TeamOlengKiller)
                                     IndOleng.acceptGroupInvitationByTicket(AbiMuhajir.id,TeamOlengKiller)
                                     IndOleng.sendMessage(msg.to, "Masuk : %s" % str(AbiMuhajir.name))
    except Exception as error:
        print (error)

while True:
  try:
      Ops = IndOleng.poll.fetchOperations(IndOleng.revision, 50)
      for op in Ops:
        if op.type != 0:
          IndOleng.revision = max(IndOleng.revision, op.revision)
          bot(op)
  except Exception as AirMani:
    AirMani = str(AirMani)
    if "reason=None" in AirMani:
      print (AirMani)
      time.sleep(60)
      restart_program()
      
