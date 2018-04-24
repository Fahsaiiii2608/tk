# -*- coding: utf-8 -*-
#SELFBOT_MAN_PC
import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator
from gtts import gTTS
import time,random,sys,json,codecs,threading,glob,urllib,urllib2,urllib3,re,string,ast,os,subprocess,six,ast,pytz,requests,tempfile

ka = LINETCR.LINE()
ka.login(token='Esi6ZiwdDw5gpjEU9Cv9.Um990fn/eZ7CJP/I34GAIq./PwWHpfnEuZGLqzlrLpgHw0ThH0QploYuYq6xQKUdZc=')
ka.loginResult()

#kb = LINETCR.LINE()
#kb.login(token='MAN')
#kb.loginResult()

#kc = LINETCR.LINE()
#kc.login(token='MAN')
#kc.loginResult()

#kd = LINETCR.LINE()
#kd.login(token='MAN')
#kd.loginResult()

#ke = LINETCR.LINE()
#ke.login(token='MAN')
#ke.loginResult()

#kf = LINETCR.LINE()
#kf.login(token='MAN')
#kf.loginResult()

#kg = LINETCR.LINE()
#kg.login(token='MAN')
#kg.loginResult()

#kh = LINETCR.LINE()
#kh.login(token='MAN')
#kh.loginResult()

#ki = LINETCR.LINE()
#ki.login(token='MAN')
#ki.loginResult()

#kj = LINETCR.LINE()
#kj.login(token='MAN')
#kj.loginResult()

backup = LINETCR.LINE()
backup.login(token='Esi6ZiwdDw5gpjEU9Cv9.Um990fn/eZ7CJP/I34GAIq./PwWHpfnEuZGLqzlrLpgHw0ThH0QploYuYq6xQKUdZc=')
backup.loginResult()

print "Login.. SELFBOT_MAN_PROTECT"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""Thailand : SELFBOT_MAN_PC

 ╭══════════════════╮
 ║ ♨️ SELFBOT_MAN_PC_HELP ♨️
 ║͜͡☆➣ คำสั่ง-> 「Tome1」
 ║͜͡☆➣ คำสั่ง-> 「Tome2」
 ║͜͡☆➣ คำสั่ง-> 「Tome3」
 ║͜͡☆➣ คำสั่ง-> 「Tome4」
 ╰══════════════════╯
 ╭══════════════════╮
 ║ ♨️ติดตั้งชุดระบบป้องกัน[Protect]♨️
 ║ ลงคำสั่ง ครั้งเดียว ระบบทำงานยกเชุด
 ║•คำสั่ง..  Allprotect on
 ║•คำสั่ง..  Allprotect off
 ║•คำสั่ง..  เปิดระบบป้องกัน
 ║•คำสั่ง..  ปิดระบบป้องกัน
 ╰══════════════════╯
 ╭══════════════════╮
 ║ ♨️รับทำเชลบอท [SELFBOT] กันรัน
 ║•รับทำ..[ชุดบอทป้องกัน+Protect+]
 ║•รับทำ..[ชุดบอทส่วนตัว+Kicker+]
 ║•รับทำ..[บอทแท๊ก,ทั้งกลุ่ม+Mention]
 ║•รับทำ..[ชุดบอทบิน] ☞มีครบทุกฟังชั่น
 ╰══════════════════╯
──────┅═ই۝ई═┅──────
 สอบถามรายละเอียดเพิ่มเติม..  Link⤵️
http://line.me/ti/p/~1ove..neverdie
──────┅═ই۝ई═┅────── 
"""

creatorMessage ="""HELP_creator
 ╭══════════════════╮
 ║ ♨️ SELFBOT_MAN_PC_HELP ♨️
 ╰══════════════════╯
 ╭══════════════════╮
 ║͜͡☆➣ steal
 ║͜͡☆➣ /invitemeto:
 ║͜͡☆➣ Clear/Cancel
 ║͜͡☆➣ Ourl/Curl
 ║͜͡☆➣ Link on/off
 ║͜͡☆➣ Status/Set
 ║͜͡☆➣ Lurking
 ║͜͡☆➣ Gurl/URL/ลิงก์กลุ่ม
 ║͜͡☆➣ เข้า = Staff in
 ║͜͡☆➣ ออก = Staff bye
 ║͜͡☆➣ ตัวหลักออก = @bye
 ║͜͡☆➣ Leave all group
 ║͜͡☆➣ Banlist/บัญชีดำ
 ║͜͡☆➣ Clear ban/Cb/ล้างดำ
 ║͜͡☆➣ Bot restart
 ║͜͡☆➣ Glist
 ║͜͡☆➣ Glistmid
 ║͜͡☆➣ 
 ║͜͡☆➣ Tagall/Mention all
 ╰══════════════════╯
"""

setMessage ="""HELP_settings
 ╭══════════════════╮
 ║ ♨️ SELFBOT_MAN_PC_HELP ♨️
 ╰══════════════════╯
 ╭══════════════════╮
 ║͜͡☆➣ Purge on/off
 ║͜͡☆➣ Cancel on/off
 ║͜͡☆➣ Qr on/off
 ║͜͡☆➣ Contact on/off
 ║͜͡☆➣ Join on/off
 ║͜͡☆➣ Leave on/off
 ║͜͡☆➣ Share on/off
 ║͜͡☆➣ Simisimi on/off
 ║͜͡☆➣ Sider on/off
 ║͜͡☆➣ Lurking on/off
 ║͜͡☆➣ Lurking reset
 ║͜͡☆➣ Admin add @
 ║͜͡☆➣ Admin remove @
 ║͜͡☆➣ Sambutan on/off
 ║͜͡☆➣ Cancelinvite on/off
 ╰══════╬💀╬══════╯
"""

publikMessage ="""HELP_selfbot
 ╭══════════════════╮
 ║ ♨️ SELFBOT_MAN_PC_HELP ♨️
 ╰══════════════════╯
 ╭══════════════════╮
 ║͜͡☆➣ Me
 ║͜͡☆➣ Creator
 ║͜͡☆➣ Ginfo
 ║͜͡☆➣ Adminlist
 ║͜͡☆➣ List group
 ║͜͡☆➣ Absen
 ║͜͡☆➣ Respon
 ╰══════════════════╯
"""

mediaMessage ="""HELP_media
 ╭══════════════════╮
 ║ ♨️ SELFBOT_MAN_PC_HELP ♨️
 ╰══════════════════╯
 ╭══════════════════╮
 ║͜͡☆➣ /music
 ║͜͡☆➣ /lirik
 ║͜͡☆➣ /ig  Instagrams
 ║͜͡☆➣ /yt: Youtubelink:
 ║͜͡☆➣ Say-id
 ║͜͡☆➣ Say-en
 ║͜͡☆➣ Say welcome
 ║͜͡☆➣ Playstore
 ║͜͡☆➣ /apakah
 ║͜͡☆➣ /hari
 ║͜͡☆➣ /berapa
 ║͜͡☆➣ /berapakah
 ║͜͡☆➣ /kapan
 ║͜͡☆➣ Image
 ║͜͡☆➣ Runtime
 ║͜͡☆➣ Tr-en  แปลภาษา
 ║͜͡☆➣ Tr-id  แปลภาษา
 ║͜͡☆➣ En@id อังกฤษ-อินโด
 ║͜͡☆➣ Id@en อินโด-อังกฤษ
 ║͜͡☆➣ SearchID:ใส่ใอดีไลน์
 ║͜͡☆➣ LineID:ใส่ใอดีไลน์
 ║͜͡☆➣ /เพลสโตร์:
 ║͜͡☆➣ /รูปภาพ:
 ║͜͡☆➣ /เช็คเวลาบอท
 ╰═════════════════╯
 🔴✦เปิด/ปิดข้อความต้อนรับ✦🔴
╭══════════════════╮
║͜͡☆🔴➣ Hhx1 on ➠เปิดต้อนรับ
║͜͡☆🔴➣ Hhx1 off ➠ปิดต้อนรับ
║͜͡☆🔴➣ Hhx2 on ➠เปิดออกกลุ่ม
║͜͡☆🔴➣ Hhx2 off ➠ปิดออกกลุ่ม
║͜͡☆🔴➣ Hhx3 on ➠เปิดพูดถึงคนลบ
║͜͡☆🔴➣ Hhx3 off ➠ปิดพูดถึงคนลบ
║͜͡☆🔴➣ Mbot on ➠เปิดเเจ้งเตือน
║͜͡☆🔴➣ Mbot off ➠ปิดเเจ้งเตือน
║͜͡☆🔴➣ M on ➠เปิดเเจ้งเตือนตนเอง
║͜͡☆🔴➣ M off ➠ปิดเเจ้งเตือนตนเอง
║͜͡☆🔴➣ Tag on ➠เปิดกล่าวถึงเเท็ค
║͜͡☆🔴➣ Tag off ➠ปิดกล่าวถึงเเท็ค
║͜͡☆🔴➣ Kicktag on ➠เปิดเตะคนเเท็ค
║͜͡☆🔴➣ Kicktag off ➠ปิดเตะคนเเท็ค
╰═════════════════╯
  🔴✦โหมดตั้งค่าข้อความ✦🔴
╭═════════════════╮
║͜͡☆🔴➣Hhx1˓: ➠ไส่ข้อความต้อนรับ
║͜͡☆🔴➣Hhx2˓: ➠ไส่ข้อความออกจากกลุ่ม
║͜͡☆🔴➣Hhx3˓: ➠ไส่ข้อความเมื่อมีคนลบ
║͜͡☆🔴➣Tag1:   ➠ใส่ข้อความแทค
║͜͡☆🔴➣Tag2:   ➠ ใส่ข้อความแทค
╰═════════════════╯
  🔴✦โหมดเช็คตั้งค่าข้อความ✦🔴
╭═════════════════╮
║͜͡☆🔴➣Hhx1 ➠เช็คข้อความต้อนรับ
║͜͡☆🔴➣Hhx2 ➠เช็คข้อความคนออก
║͜͡☆🔴➣Hhx3 ➠เช็คข้อความคนลบ
║͜͡☆🔴➣Tag1 ➠เช็ตข้อความแทค
║͜͡☆🔴➣Tag2 ➠เช็คข้อความแทค
╰═════════════════╯
╭═════════════════╮
║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅
║•─✯͜͡✯TOME★BOTLINE✯͜͡✯─• 
╰═════════════════╯
ลิ้ง:http://line.me/ti/p/~tomebotline
──┅═✥===========✥═┅──
"""

KAC = [ka]#,kb,kc,kd,ke,kf,kg,kh,ki,kj]
mid = ka.getProfile().mid
#Amid = kb.getProfile().mid
#Bmid = kc.getProfile().mid
#Cmid = kd.getProfile().mid
#Dmid = ke.getProfile().mid
#Emid = kf.getProfile().mid
#Fmid = kg.getProfile().mid
#Gmid = kh.getProfile().mid
#Hmid = ki.getProfile().mid
#Imid = kj.getProfile().mid
#Jmid = backup.getProfile().mid
Bots=["ub8cf7dd0537e133edc8e9fa2df881a89",mid]#,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid]
self = ["ub8cf7dd0537e133edc8e9fa2df881a89",mid]
admin = "ub8cf7dd0537e133edc8e9fa2df881a89"
admsa = "ub8cf7dd0537e133edc8e9fa2df881a89"
owner = "ub8cf7dd0537e133edc8e9fa2df881a89"
adminMID = "ub8cf7dd0537e133edc8e9fa2df881a89"
Creator="ub8cf7dd0537e133edc8e9fa2df881a89"
owner=["ub8cf7dd0537e133edc8e9fa2df881a89"]
admin=["ub8cf7dd0537e133edc8e9fa2df881a89"]

#=========BACKUP========#
contact = ka.getProfile()
backup1 = ka.getProfile()
backup1.displayName = contact.displayName
backup1.statusMessage = contact.statusMessage                        
backup1.pictureStatus = contact.pictureStatus

#contact = kb.getProfile()
#backup2 = kb.getProfile()
#backup2.displayName = contact.displayName
#backup2.statusMessage = contact.statusMessage                        
#backup2.pictureStatus = contact.pictureStatus

#contact = kc.getProfile()
#backup3 = kc.getProfile()
#backup3.displayName = contact.displayName
#backup3.statusMessage = contact.statusMessage                        
#backup3.pictureStatus = contact.pictureStatus

#contact = kd.getProfile()
#backup4 = kd.getProfile()
#backup4.displayName = contact.displayName
#backup4.statusMessage = contact.statusMessage                        
#backup4.pictureStatus = contact.pictureStatus

#contact = ke.getProfile()
#backup5 = ke.getProfile()
#backup5.displayName = contact.displayName
#backup5.statusMessage = contact.statusMessage                        
#backup5.pictureStatus = contact.pictureStatus

#contact = kf.getProfile()
#backup6 = kf.getProfile()
#backup6.displayName = contact.displayName
#backup6.statusMessage = contact.statusMessage                        
#backup6.pictureStatus = contact.pictureStatus

#contact = kg.getProfile()
#backup7 = kg.getProfile()
#backup7.displayName = contact.displayName
#backup7.statusMessage = contact.statusMessage                        
#backup7.pictureStatus = contact.pictureStatus

#contact = kh.getProfile()
#backup8 = kh.getProfile()
#backup8.displayName = contact.displayName
#backup8.statusMessage = contact.statusMessage                        
#backup8.pictureStatus = contact.pictureStatus

#contact = ki.getProfile()
#backup9 = ki.getProfile()
#backup9.displayName = contact.displayName
#backup9.statusMessage = contact.statusMessage                        
#backup9.pictureStatus = contact.pictureStatus

#contact = kj.getProfile()
#backup10 = kj.getProfile()
#backup10.displayName = contact.displayName
#backup10.statusMessage = contact.statusMessage                        
#backup10.pictureStatus = contact.pictureStatus
#===========================================#
responsename = ka.getProfile().displayName
#responsename2 = kb.getProfile().displayName
#responsename3 = kc.getProfile().displayName
#responsename4 = kd.getProfile().displayName
#responsename5 = ke.getProfile().displayName
#responsename6 = kf.getProfile().displayName
#responsename7 = kg.getProfile().displayName
#responsename8 = kh.getProfile().displayName
#responsename9 = ki.getProfile().displayName
#responsename10 = kj.getProfile().displayName

wait = {
    "contact":False,
    "Bot":{}, 
    'autoAdd':False,
    "autoJoin":True,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    "autoCancel":{"on":True,"members":1},
    "leaveRoom":True,
    "timeline":True,
    "likeOn":True,
    "Timeline":True,
    "autoAdd":False,
    "lang":"JP",
      "commentOn":True,
    "comment1":"""
                [ AOTO  LIKE  ]
                  [ SELF BOT ]
  [ รับติดตั้ง เชลบอท ราคาประหยัด ]
─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─
     •─✯͜͡✯TOME★BOTLINE✯͜͡✯─• 
   http://line.me/ti/p/~tomebotline
   ▀██──▄███▄─▀██─██▀██▀▀▀█
   ─██─███─███─██─██─██▄█
   ─██─▀██▄██▀─▀█▄█▀─██▀█
   ▄██▄▄█▀▀▀─────▀──▄██▄▄▄█
              📲 โทรศัพท์ 0928081567
""",
     "comment1":"""
_________มีเซลบอท________จำหน่าย
________88888888________8888888
______888888888888____88888888888
__888888822222222222888882222888888
_888888822222222222222882222222228888
▀██▀─▄███▄─▀██─██▀██▀▀█
▒██─███─███─██─██─██▄█
▒██─▀██▄██▀─▀█▄█▀─██▀█
▄██▄▄█▀▀▀─────▀──▄██▄▄█
_888882222222222222222_____88888888
___8888888882222______88888888888
______88888_TOMEBOTLINE_8888888
________88_TEAMBOTTHAILAND_88
__________88888888888888888
______________88888888888
________________8888
      ╔•═•-⊰⊱•══•⊰⊱•═•⊰⊱•══•⊰⊱•═•╗
            〘•สนใจติดต่อที่ลิ้งด้านล่าง•〙
                   👇👇👇👇
       ™〖Ĵắ¢ҝҝїě〗🌷TOME🎀BOTLINE🌷
       ™〖Ĵắ¢ҝҝїě〗☞ᵀËÄMBOTTHAILAND
       http://line.me/ti/p/~tomebotline
      ╚•══•-⊰⊱•═•⊰⊱•═•⊰⊱•══•⊰ ⊱•═•╝
""",
  #  "comment3":"👍Auto Like By SELFBOT_MAN_PC",
   # "comment4":"👍Auto Like By SELFBOT_MAN_PC",
#    "comment6":"👍Auto Like By SELFBOT_MAN_PC",
 #   "comment7":"👍Auto Like By SELFBOT_MAN_PC",
  #  "comment8":"👍Auto Like By SELFBOT_MAN_PC",
   # "comment9":"👍Auto Like By SELFBOT_MAN_PC",
#    "comment10":"👍Auto Like By SELFBOT_MAN_PC",
 #   "comment5":"👍Auto Like By SELFBOT_MAN_PC \n(รับทำเชลบอทกันรัน) บอทป้องกัน บอทแท๊ก",
    "commentOn":True,
    "acommentOn":False,
    "bcommentOn":False,
    "ccommentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "Protectcancel":False,
    "protectionOn":False,
    "atjointicket":True,
    "blacklist":{},
    "steal":{},
    "Hhx1":False,
    "Hhx2":False,
    "Hhx3":False,
    "Notifed":False,
    "Notifedbot":False,
    "atjointicket":False,
    "pnharfbot":{},
    "pname":{},
    "pro_name":{},
    "tag1":"\n[🔯ยังไม่มีข้อความ ตอบกลับ🔯]",
    "tag2":"\n[🔯ยังไม่มีข้อความ ตอบกลับ🔯]",
	"posts":False,
    "message":"Thank For Add Me.. \n\n คุยเรื่องบอทปรึกษาได้ครับ มีครบทุกฟังชั่น\nhttp://line.me/ti/p/~tomebotline \n(รับติดตั้งบอทSiri V10 และ รับทำเชลบอทกันรัน) \nเปิดสอนเขียนโปรแกรมบอท ชุดบอทป้องกัน บอทแท๊ก บอทแจ้งเตือนและต้อนรับสมาชิกเข้ากลุ่ม \n\nสนใจทักมาสอบถามได้ครับ \nLine ID. 1ove..neverdie",
    "Sambutan":True,
    "Sider":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}    

read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{}
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
}

settings = {
    "simiSimi":{}
}

setTime = {}
setTime = read['readTime']
mulai = time.time() 

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
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)      
    
def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False    

def upload_tempimage(client):
     '''
         Upload a picture of a kitten. We don't ship one, so get creative!
     '''
     config = {
         'album': album,
         'name':  'bot auto upload',
         'title': 'bot auto upload',
         'description': 'bot auto upload'
     }

     print("Uploading image... ")
     image = client.upload_from_path(image_path, config=config, anon=False)
     print("Done")
     print()

     return image

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
    print "[Command] Tag All"
    try:
       ka.sendMessage(msg)
    except Exception as error:
       print error
     
def sendAudio(self, to_, path):
       M = Message()
       M.text = None
       M.to = to_
       M.contentMetadata = None
       M.contentPreview = None
       M.contentType = 3
       M_id = self._client.sendMessage(0,M).id
       files = {
             'file': open(path,  'rb'),
       }
    
def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def sendImage(self, to_, path):
      M = Message(to=to_, text=None, contentType = 1)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self._client.sendMessage(0,M)
      M_id = M2.id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload image failure.')
      return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except:
         try:
            self.sendImage(to_, path)
         except Exception as e:
            raise e

def sendAudio(self, to_, path):
        M = Message()
        M.text = None
        M.to = to_
        M.contentMetadata = None
        M.contentPreview = None
        M.contentType = 3
        M_id = self._client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e

def sendVideo(self, to_, path):
        M = Message(to=to_,contentType = 2)
        M.contentMetadata = {
              'VIDLEN' : '0',
              'DURATION' : '0'
        }
        M.contentPreview = None
        M_id = self.Talk.client.sendMessage(0,M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'video',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        return True

def sendVideoWithURL(self, to_, url):
        path = 'pythonLines.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
               shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise e

def sendGif(self, to_, path):
      M = Message(to=to_,contentType = 1)
      M.contentMetadata = {
           'VIDLEN' : '0',
           'DURATION' : '0'
       }
      M.contentPreview = None
      M_id = self.Talk.client.sendMessage(0,M).id
      files = {
         'file': open(path, 'rb'),
      }
      params = {
         'name': 'media',
         'oid': M_id,
         'size': len(open(path, 'rb').read()),
         'type': 'image',
         'ver': '1.0',
      }
      data = {
         'params': json.dumps(params)
      }
      r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
         raise Exception('Upload Gif failure.')
      return True

def sendGifWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Gif failure.')
      try:
         self.sendGif(to_, path)
      except Exception as e:
         raise e 

def downloadFileWithURL(self, fileUrl):
        saveAs = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
        r = self.get_content(fileUrl)
        if r.status_code == 200:
            with open(saveAs, 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            return saveAs
        else:
            raise Exception('Download file failure.')

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
           if wait["autoAdd"] == True:
              ka.findAndAddContactsByMid(op.param1)
              if(wait["message"]in[""," ","\n",None]):
                pass
              else:
                ka.sendText(op.param1,str(wait["message"]))


        if op.type == 55:
	    try:
	      group_id = op.param1
	      user_id=op.param2
	      subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
	    except Exception as e:
	      print e
	      
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = ka.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        ka.sendText(op.param1, "Hi " + "[ " + Name + " ]" + "\ndo not take a peek here to chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                    else:
                                        ka.sendText(op.param1, "Hi " + "[ " + Name + " ]" + "\ndo not take a peek here to chat😁   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                else:
                                    ka.sendText(op.param1, "Hi " + "☞ " + Name + " ☜" + "\ndo not take a peek here to chat😁   ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass 
#==============================================================================#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
#==============================================================================#
        if op.type == 13:
          if mid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ka.acceptGroupInvitation(op.param1)
                G = ka.getGroup(op.param1)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                Ticket = ka.reissueGroupTicket(op.param1)
                ka.acceptGroupInvitationByTicket(op.param1,Ticket)
#                kc.acceptGroupInvitationByTicket(op.param1,Ticket)
 #               kd.acceptGroupInvitationByTicket(op.param1,Ticket)
  #              ke.acceptGroupInvitationByTicket(op.param1,Ticket)
   #             kf.acceptGroupInvitationByTicket(op.param1,Ticket)
    #            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
     #           kh.acceptGroupInvitationByTicket(op.param1,Ticket)
      #          ki.acceptGroupInvitationByTicket(op.param1,Ticket)
       #         kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
              else:
                ka.rejectGroupInvitation(op.param1)
                
#          if Amid in op.param3:
#            if wait["autoJoin"] == True:
 #             if op.param2 in owner:
  #              kb.acceptGroupInvitation(op.param1)
   #           else:
    #            kb.rejectGroupInvitation(op.param1)
     #       else:
      #        print "autoJoin is Off"
                
#          if Bmid in op.param3:
 #           if wait["autoJoin"] == True:
  #            if op.param2 in owner:
   #             kc.acceptGroupInvitation(op.param1)
    #          else:
     #           kc.rejectGroupInvitation(op.param1)
      #      else:
       #       print "autoJoin is Off"
        #        
         # if Cmid in op.param3:
#            if wait["autoJoin"] == True:
 #             if op.param2 in owner:
  #              kd.acceptGroupInvitation(op.param1)
   #           else:
    #            kd.rejectGroupInvitation(op.param1)
     #       else:
      #        print "autoJoin is Off"
       #         
        #  if Dmid in op.param3:
         #   if wait["autoJoin"] == True:
          #    if op.param2 in owner:
           #     ke.acceptGroupInvitation(op.param1)
            #  else:
#                ke.rejectGroupInvitation(op.param1)
 #           else:
  #            print "autoJoin is Off"
#
 #         if Emid in op.param3:
  #          if wait["autoJoin"] == True:
   #           if op.param2 in owner:
    #            kf.acceptGroupInvitation(op.param1)
     #         else:
      #          kf.rejectGroupInvitation(op.param1)
       #     else:
        #      print "autoJoin is Off"
         #       
          #if Fmid in op.param3:
           # if wait["autoJoin"] == True:
#              if op.param2 in owner:
 #               kg.acceptGroupInvitation(op.param1)
  #            else:
   #             kg.rejectGroupInvitation(op.param1)
    #        else:
     #         print "autoJoin is Off"
                
#          if Gmid in op.param3:
 #           if wait["autoJoin"] == True:
  #            if op.param2 in owner:
   #             kh.acceptGroupInvitation(op.param1)
    #          else:
     #           kh.rejectGroupInvitation(op.param1)
      #      else:
       #       print "autoJoin is Off"
                
#          if Hmid in op.param3:
 #           if wait["autoJoin"] == True:
  #            if op.param2 in owner:
   #             ki.acceptGroupInvitation(op.param1)
    #          else:
     #           ki.rejectGroupInvitation(op.param1)
      #      else:
       #       print "autoJoin is Off"

#          if Imid in op.param3:
 #           if wait["autoJoin"] == True:
  #            if op.param2 in owner:
   #             kj.acceptGroupInvitation(op.param1)
    #          else:
     #           kj.rejectGroupInvitation(op.param1)
      #      else:
       #       print "autoJoin is Off"
                
          if Jmid in op.param3:
            if wait["autoJoin"] == True:
              if op.param2 in owner:
                ka.acceptGroupInvitation(op.param1)
              else:
                ka.rejectGroupInvitation(op.param1)
            else:
              print "autoJoin is Off"
#=========================================================================#
        if op.type == 13:
            if mid in op.param3:
                G = ka.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            ka.rejectGroupInvitation(op.param1)
                        else:
                            ka.acceptGroupInvitation(op.param1)
                        ka.sendText(op.param1, "Your invitation was declined\n\n[SELF BOT\n[By.☬ധู้さန້ণق↔ധഖาໄฟ☬]]\n\nhttp://line.me/ti/p/9r-uE5EU09")
                    else:
                        ka.acceptGroupInvitation(op.param1)
                        ka.sendText(op.param1, "Your invitation was declined\n\n[SEL FBOT\n[By.☬ധู้さန້ণق↔ധഖาໄฟ☬]]\n\nhttp://line.me/ti/p/9r-uE5EU09")
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        ka.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    ka.cancelGroupInvitation(op.param1, matched_list)
            if Amid1 in op.param3:
                G = ka.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kb.rejectGroupInvitation(op.param1)
                        else:
                            kb.acceptGroupInvitation(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kb.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kb.cancelGroupInvitation(op.param1, matched_list)
            if Amid2 in op.param3:
                G = ka.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kc.rejectGroupInvitation(op.param1)
                        else:
                            kc.acceptGroupInvitation(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kc.rejectGroupInvitation(op.param1)
                
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            group = ka.getGroup(op.param1)
            gMembMids = [contact.mid for contact in group.invitee]
            if op.param2 not in Bots or admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                try:
                  ka.cancelGroupInvitation(op.param1, gMembMids)
                  ka.sendText(op.param1,ka.getContact(op.param2).displayName + "\n" + "Who do you want to invite  ??? \nYou Are Not Our Admin, So We Cancel it.\nPlease Contact Admin/Owner")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                except:
                  random.choice(KAC).cancelGroupInvitation(op.param1, gMembMids)
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "🔘Who do you want to invite  ??? \n🔘You Are Not Our Admin, So We Cancel it.\n🔘Please Contact Admin/Owner\n\n[ระบบออโต้ถูกเปิดใช้งาน]\n🔘การเชิญสมาชิกเข้าร่วมกลุ่ม ควรแจ้งให้ทราบ..\n🔘โดยผ่าน.. Admin:bot-group หรือลงข้อมูลสมาชิกไว้\n(หากผิดพลาดยังใง รบกวนทักแชท)")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
        if op.type == 13:
          if wait["Protectcancl"] == True:
            if wait["blacklist"][op.param3] == True:
              ka.sendText(op.param1,ka.getContact(op.param3).displayName + " On Blacklist Boss Man\n•We Will Cancel Invitation\n•by : SELFBOT_MAN_PROTECT")
              random.choice(KAC).cancelGroupInvitation(op.param1,[op.param3])
#==============================================================================#
        if op.type == 11:
          if wait["Protectgr"] == True:
            if ka.getGroup(op.param1).preventJoinByTicket == False:
              if op.param2 in Bots:
                pass
              elif op.param2 in owner:
                pass
              elif op.param2 in admin:
                pass
              else:
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Dont Playing Link Group Bro")
                  random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                  random.choice(KAC).preventJoinByTicket = True
                  random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "\n" + "🔘We Enter Into Blacklist Boss Man")
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
        if op.type == 17:
          if wait["Sambutan"] == True:
            if op.param2 in owner:
                return
            ginfo = ka.getGroup(op.param1)
            contact = ka.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ka.sendText(op.param1,"•Hello ↪️" + ka.getContact(op.param2).displayName + "↩️\n•Welcome To 🔛 " + str(ginfo.name) + " " + "\n•by : SELFBOT_MAN_PROTECT")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c) 
            ka.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            ka.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#==============================================================================#
        if op.type == 15:
          if wait["Sambutan"] == True:
            if op.param2 in admin:
                return
            ka.sendText(op.param1,"Good Bye " + ka.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c)
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP" 
#==============================================================================#
        if op.type == 17: #Protect Join
          if wait["Protectjoin"] == True:
            if wait["blacklist"][op.param2] == True:
              ka.sendText(op.param1,ka.getContact(op.param2).displayName + " On Blacklist Boss Man\n•We Will Kick 👀")
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
#==============================================================================#
        if op.type == 17:
          if wait["Notifed"] == True:
            if op.param2 in owner:
                return
            ginfo = ka.getGroup(op.param1)
            contact = ka.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ka.sendText(op.param1,"•สวัสดีจ้าคนมาใหม่ ↪" + ka.getContact(op.param2).displayName + "↩️\n•ยินดีต้อนรับสู่ห้อง\n 🔛 " + str(ginfo.name) + " " + "\n\n•by : SELFBOT TOME↔BOTLINE")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c) 
            ka.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            ka.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#==============================================================================#
        if op.type == 15:
          if wait["Notifed"] == True:
            if op.param2 in admin:
                return
            ka.sendText(op.param1,"Good Bye " + ka.getContact(op.param2).displayName +  "\nSee You Next Time . . . (p′︵‵。) 🤗")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c)
            ka.sendImageWithURL(op.param1,image)
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP" 
#==============================================================================#

        if op.type == 19:
            if wait["Notifed"] == True:
                if op.param2 in Bots:
                    return
                ka.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

        if op.type == 15:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n􀜁􀄄􏿿 Bye~bye 􀜁􀄄􏿿")
                print "MEMBER OUT GROUP"

        if op.type == 17:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ginfo = cka.getGroup(op.param1)
                contact = ka.getContact(op.param2)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                ka.sendImageWithURL(op.param1,image)
                ka.sendText(op.param1,cl.getContact(op.param2).displayName + "\n\n[🙋ยินดี���อนรับ][By. ☬ധู้さန້ণق↔ധഖาໄฟ☬]")
                print "MEMBER HAS JOIN THE GROUP"

        if op.type == 19:
            if wait["Notifedbot"] == True:
                if op.param2 in Bots:
                    return
                ki1.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                ki2.sendText(op.param1,cl.getContact(op.param2).displayName + "\n􀜁􀅔􏿿 ไม่น่าจะจุกเท่าไหร่หรอก 􀜁􀅔􏿿")
                print "MEMBER HAS KICKOUT FROM THE GROUP"

 #       if op.type == 15:
  #          if wait["bcommentOn"] == True:
   #             if op.param2 in Bots:
    #                return
     #           cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["bcomment"]))
      #          print "MEMBER OUT GROUP"

#        if op.type == 17:
 #           if wait["acommentOn"] == True:
  #              if op.param2 in Bots:
   #                 return
    #            cl.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["acomment"]))
     #           print "MEMBER HAS JOIN THE GROUP"

#==============================================================================#
        if op.type == 17:
          if wait["acommentOn"] == True:
            if op.param2 in Bots:
                return
            ginfo = ka.getGroup(op.param1)
            contact = ka.getContact(op.param2)
            image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
            ka.sendText(op.param1,"•Hello ↪️" + ka.getContact(op.param2).displayName + "↩️\n•Welcome To 🔛 " + str(wait["acommentOn"]) + " " + "\n•by : SELFBOTTOME↔BOTLINE")
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c) 
            ka.sendImageWithURL(op.param1,image)
            d = Message(to=op.param1, from_=None, text=None, contentType=7)
            d.contentMetadata={
                                    "STKID": "247",
                                    "STKPKGID": "3",
                                    "STKVER": "100" }                
            ka.sendMessage(d)             
            print "MEMBER JOIN TO GROUP"
#==============================================================================#
        if op.type == 15:
          if wait["bcommentOn"] == True:
            if op.param2 in Bots:
                return
            ka.sendText(op.param1,"Good Bye " + ka.getContact(op.param2).displayName +  str(["bcommentOn"]))
            c = Message(to=op.param1, from_=None, text=None, contentType=13)
            c.contentMetadata={'mid':op.param2}
            ka.sendMessage(c)
            ka.sendImageWithURL(op.param1,image)
            random.choice(KAC).inviteIntoGroup(op.param1,[op.param2])
            print "MEMBER HAS LEFT THE GROUP" 
#==============================================================================#

        if op.type == 19:
            if wait["ccommentOn"] == True:
                if op.param2 in Bots:
                    return
                ka.sendText(op.param1,cl.getContact(op.param2).displayName + "\n" + str(wait["ccomment"]))
                print "MEMBER HAS KICKOUT FROM THE GROUP"


#==============================================================================#
        if op.type == 19: #Member Ke Kick
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              wait["blacklist"][op.param2] = True
#==============================================================================#

 #       if op.type == 26:
 #           msg = op.message            
 #           if msg.contentType == 16:
 #               url = msg.contentMetadata['postEndUrl']
 #               ka.like(url[25:58], url[66:], likeType=1001)
 #               ka.comment(url[25:58], url[66:], wait["comment1"])
#                ki1.like(url[25:58], url[66:], likeType=1001)
 #               ki1.comment(url[25:58], url[66:], wait["comment1"])
  #              ki2.like(url[25:58], url[66:], likeType=1001)
   #             ki2.comment(url[25:58], url[66:], wait["comment1"])
    #            ki3.like(url[25:58], url[66:], likeType=1001)
     #           ki3.comment(url[25:58], url[66:], wait["comment1"])
      #          ki4.like(url[25:58], url[66:], likeType=1001)
       #         ki4.comment(url[25:58], url[66:], wait["comment1"])
        #        ki5.like(url[25:58], url[66:], likeType=1001)
         #       ki5.comment(url[25:58], url[66:], wait["comment1"])
          #      ki6.like(url[25:58], url[66:], likeType=1001)
           #     ki6.comment(url[25:58], url[66:], wait["comment1"])
            #    ki7.like(url[25:58], url[66:], likeType=1001)
             #   ki7.comment(url[25:58], url[66:], wait["comment1"])
              #  ki8.like(url[25:58], url[66:], likeType=1001)
               # ki8.comment(url[25:58], url[66:], wait["comment1"])
#                ki9.like(url[25:58], url[66:], likeType=1001)
 #               ki9.comment(url[25:58], url[66:], wait["comment1"])
  #              ki10.like(url[25:58], url[66:], likeType=1001)
   #             ki10.comment(url[25:58], url[66:], wait["comment1"])
    #            print ("AUTO LIKE SELFBOT")
     #           print ("Auto Like By.☬ധู้さန້ণق↔ധഖาໄฟ☬")
 #==============================================================================#
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            if op.param3 in mid:
              if op.param2 not in Bots or owner:
                  G = kj.getGroup(op.param1)
                  G.preventJoinByTicket = False
                  kj.updateGroup(G)
                  Ticket = kj.reissueGroupTicket(op.param1)
                  backup.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  backup.kickoutFromGroup(op.param1,[op.param2])
                  H = backup.getGroup(op.param1)
                  H.preventJoinByTicket = False
                  backup.updateGroup(H)
                  Ticket = backup.reissueGroupTicket(op.param1)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kj.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kj.updateGroup(G)
                  backup.leaveGroup(op.param1)
                  wait["blacklist"][op.param2] = True
                  f=codecs.open('st2__b.json','w','utf-8')
                  json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
#==============================================================================#
            elif op.param3 in Amid:
              if op.param2 not in Bots or owner:
                  G = kc.getGroup(op.param1)
                  kc.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kc.updateGroup(G)
                  Ticket = kc.reissueGroupTicket(op.param1)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kc.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kc.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Bmid:
              if op.param2 not in Bots or owner:
                  G = kd.getGroup(op.param1)
                  kd.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kd.updateGroup(G)
                  Ticket = kd.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kd.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kd.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Cmid:
              if op.param2 not in Bots or owner:
                  G = ke.getGroup(op.param1)
                  ke.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ke.updateGroup(G)
                  Ticket = ke.reissueGroupTicket(op.param1)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ke.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ke.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Dmid:
              if op.param2 not in Bots or owner:
                  G = kf.getGroup(op.param1)
                  kf.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kf.updateGroup(G)
                  Ticket = kf.reissueGroupTicket(op.param1)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kf.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kf.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Emid:
              if op.param2 not in Bots or owner:
                  G = kg.getGroup(op.param1)
                  kg.kickoutFromGroup(op.param1,[op.param2])
                  G.reventJoinByTicket = False
                  kg.updateGroup(G)
                  Ticket = kg.reissueGroupTicket(op.param1)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kg.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kg.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Fmid:
              if op.param2 not in Bots or owner:
                  G = kh.getGroup(op.param1)
                  kh.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kh.updateGroup(G)
                  Ticket = kh.reissueGroupTicket(op.param1)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kh.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kh.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Gmid:
              if op.param2 not in Bots or owner:
                  G = ki.getGroup(op.param1)
                  ki.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ki.updateGroup(G)
                  Ticket = ki.reissueGroupTicket(op.param1)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ki.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ki.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Hmid:
              if op.param2 not in Bots or owner:
                  G = kj.getGroup(op.param1)
                  kj.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kj.updateGroup(G)
                  Ticket = kj.reissueGroupTicket(op.param1)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kj.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kj.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Imid:
              if op.param2 not in Bots or owner:
                  G = kb.getGroup(op.param1)
                  kb.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  kb.updateGroup(G)
                  Ticket = kb.reissueGroupTicket(op.param1)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = kb.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  kb.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#==============================================================================#
            elif op.param3 in Jmid:
              if op.param2 not in Bots or owner:
                  G = ka.getGroup(op.param1)
                  ka.kickoutFromGroup(op.param1,[op.param2])
                  G.preventJoinByTicket = False
                  ka.updateGroup(G)
                  Ticket = ka.reissueGroupTicket(op.param1)
                  kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kj.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  ka.acceptGroupInvitationByTicket(op.param1,Ticket)
                  time.sleep(0.00001)
                  G = ka.getGroup(op.param1)
                  G.preventJoinByTicket = True
                  ka.updateGroup(G)
                  wait["blacklist"][op.param2] = True
#===============================================================================#
        if op.type == 19: #admin
          if op.param2 in Bots:
            pass
          elif op.param2 in owner:
            pass
          elif op.param2 in admin:
            pass
          else:
            try:
              if op.param3 in admin:
                if op.param2 not in Bots or owner:
                  if op.param2 in Bots:
                    pass
                  elif op.param2 in owner:
                    pass
                  else:
                    try:
                      ka.kickoutFromGroup(op.param1,[op.param2])
                      kb.kickoutFromGroup(op.param1,[op.param2])
                      kc.kickoutFromGroup(op.param1,[op.param2])
                      kd.kickoutFromGroup(op.param1,[op.param2])
                      ke.kickoutFromGroup(op.param1,[op.param2])
                      kf.kickoutFromGroup(op.param1,[op.param2])
                      kg.kickoutFromGroup(op.param1,[op.param2])
                      kh.kickoutFromGroup(op.param1,[op.param2])
                      ki.kickoutFromGroup(op.param1,[op.param2])
                      kj.kickoutFromGroup(op.param1,[op.param2])
                      ka.inviteIntoGroup(op.param1,[op.param3])
                      kb.inviteIntoGroup(op.param1,[op.param3])
                      kc.inviteIntoGroup(op.param1,[op.param3])
                      kd.inviteIntoGroup(op.param1,[op.param3])
                      ke.inviteIntoGroup(op.param1,[op.param3])
                      kf.inviteIntoGroup(op.param1,[op.param3])
                      kg.inviteIntoGroup(op.param1,[op.param3])
                      kh.inviteIntoGroup(op.param1,[op.param3])
                      ki.inviteIntoGroup(op.param1,[op.param3])
                      kj.inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
                    except:
                      random.choice(KAC).getGroup(op.param1)
                      random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                      random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                      wait["blacklist"][op.param2] = True
#==============================================================================#
              elif op.param3 in owner:
                if op.param2 not in Bots or owner:
                  try:
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #ka.inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
                  except:
                    random.choice(KAC).getGroup(op.param1)
                    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    #random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                    wait["blacklist"][op.param2] = True
            except:
              try:
                ka.kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
              except:
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                wait["blacklist"][op.param2] = True
#==============================================================================#
        if op.type == 22:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                ka.leaveRoom(op.param1)
#==============================================================================#
        if op.type == 25:
            msg = op.message
        if op.type == 19:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
            ka.sendText(op.param1,ka.getContact(op.param2).displayName + " Kick 👀")
#==============================================================================#
        if op.type == 11:
          if op.param2 in Bots:
            pass
          elif op.param2 in admin:
            pass
          else:
            msg = Message(to=op.param1, from_=None, text=None, contentType=13)
            msg.contentMetadata={'mid':op.param2}
            ka.sendMessage(msg)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                ka.sendText(msg.to, "「MAN-auto-Chat」⤵️" + "\n" + data['result']['response'].encode('utf-8'))
#==============================================================================#
            if 'MENTION' in msg.contentMetadata.keys() != None:
                if wait["detectMention"] == True:
                    contact = ka.getContact(msg.from_)                  
                    cName = contact.displayName
                    balas = [cName + "\n" + str(wait["tag1"]) , cName + "\n" + str(wait["tag2"])]
                    ret_ = "[Auto Respond] " + random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            ka.sendText(msg.to,ret_)
                            break
#            if 'MENTION' in msg.contentMetadata.keys() != None:
 #                if wait["detectMention"] == True:
  #                   contact = cl.getContact(msg.from_)
   #                  cName = contact.displayName
    #                 balas = ["Dont Tag Me!! Im Busy",cName + ""]
     #                ret_ = "[Auto] " + random.choice(balas)
      #               name = re.findall(r'@(\w+)', msg.text)
       #              mention = ast.literal_eval(msg.contentMetadata['MENTION'])
        #             mentionees = mention['MENTIONEES']
         #            for mention in mentionees:
          #                 if mention['M'] in Bots:
           #                       cl.sendText(msg.to,ret_)
            #                      msg.contentType = 7
             #                     msg.text = ''
              #                    msg.contentMetadata = {
               #                                             'STKPKGID': '9662',
                #                                            'STKTXT': '[]',
                 #                                           'STKVER': '16',
                  #                                          'STKID':'697'
                   #                                     }
                    #              cl.sendMessage(msg)
                     #             break
            if "MENTION" in msg.contentMetadata.keys() != None:
                 if wait['detectMention'] == True:
                     contact = ka.getContact(msg.from_)
                     image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                     cName = contact.displayName
                     msg.text1 = "@"+cName+" "
                     balas = ["\n╭═════════════════╮\n║͜͡☆➣🔒มีเชลบอทลบรัน พร้อมคิกเก้อ💟\n║͜͡☆➣🔒ลบบินกลุ่ม ออโต้ไลค์\n║͜͡☆➣ 🔒และอื่นๆอีกมากมาย\n║͜͡☆➣🔒กันสมาชิกเปิดลิ้งห้อง\n║͜͡☆➣🔒กันรัน\n║͜͡☆➣🔒กันสมาชิกเชิญคนนอกเข้า\n║͜͡☆➣🔒กันสมาชิกเปลี่ยนชื่อกลุ่ม\n║͜͡☆➣🔒กันคนนอกเข้ามาลบคนในกลุ่ม\n║͜͡☆➣🔒และยังมีเซลกันรันอีกด้วย ราคา150บาท\n║͜͡☆➣👉สนใจติดต่อลิ้งด้านล่างเรยครับ👈\n║͜͡☆➣โอนเข้าบัญชี💲เทานั้น\n║͜͡☆➣สนใจ แอดมาคุยได้\n╰═════════════════╯\n╭═════════════════╮\n║͜͡☆➣http://line.me/ti/p/~dmc.072_tome\n║͜͡☆➣http://line.me/ti/p/~tomebotline\n╰═════════════════╯"]
                     ret_ = msg.text1 + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata["MENTION"])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ka.sendText(msg.to,ret_)
                                  msg.contentType = 7
                                  msg.text = ''
                                  msg.contentMetadata = {
                                                            'STKPKGID': '35485149',
                                                            'STKTXT': '[]',
                                                            'STKVER': '16',
                                                            'STKID':'3232633'
                                                        }
                                  ka.sendImageWithURL(msg.to,image)
                                  break            
                    
             
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = ka.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag Me!! Im Busy",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","-_-","Alin lagi off", cName + " Kenapa Tag saya?","SPAM PC aja " + cName, "Jangan Suka Tag gua " + cName, "Kamu siapa " + cName + "?", "Ada Perlu apa " + cName + "?","Tenggelamkan tuh yang suka tag pake BOT","Tersummon -_-"]
                     ret_ = "[Auto Respond] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  ka.sendText(msg.to,ret_)
                                  ka.kickoutFromGroup(msg.to,[msg.from_])
                                  break
#=====================================================================#            
        if op.type == 32:
          if wait["Protectcancel"] == True:
            if op.param2 not in admin:
              if op.param2 in Bots:
                pass
              elif op.param2 in admin:
                pass
              else:
                random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + " •Cancel Invitation 👀")
                random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                wait["blacklist"][op.param2] = True
#==============================================================================#
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    ka.leaveRoom(msg.to)
#==============================================================================#
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                ka.like(url[25:58], url[66:], likeType=1001)
#==============================================================================#
        if op.type == 25:
            msg = op.message
        if op.type == 25:
            msg = op.message                                  
                              
            if msg.text in ["Bot on"]:
                wait["Bot"] = True
                ka.sendText(msg.to,"Bot Sudah on Kembali.")  

        if op.type == 25:
          if wait["Bot"] == True:    
            msg = op.message
            
        if op.type == 25:
            msg = op.message
#==============================================================================#
            if msg.contentType == 13:
              if msg.from_ in owner:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = ka.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                ka.findAndAddContactsByMid(target)
                                contact = ka.getContact(target)
                                cu = ka.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                ka.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                ka.sendText(msg.to,"Profile Picture " + contact.displayName)
                                ka.sendImageWithURL(msg.to,image)
                                ka.sendText(msg.to,"Cover " + contact.displayName)
                                ka.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass
#==============================================================================#
              elif wait["wblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  ka.sendText(msg.to,"already")
                  wait["wblack"] = False
                else:
                  wait["commentBlack"][msg.contentMetadata["mid"]] = True
                  wait["wblack"] = False
                  ka.sendText(msg.to,"decided not to comment")
#==============================================================================#
              elif wait["dblack"] == True:
                if msg.contentMetadata["mid"] in wait["commentBlack"]:
                  del wait["commentBlack"][msg.contentMetadata["mid"]]
                  ka.sendText(msg.to,"deleted")
                  wait["dblack"] = False
                else:
                  wait["dblack"] = False
                  ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
              elif wait["wblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  ka.sendText(msg.to,"already")
                  wait["wblacklist"] = False
                else:
                  wait["blacklist"][msg.contentMetadata["mid"]] = True
                  wait["wblacklist"] = False
                  ka.sendText(msg.to,"aded")
#==============================================================================#
              elif wait["dblacklist"] == True:
                if msg.contentMetadata["mid"] in wait["blacklist"]:
                  del wait["blacklist"][msg.contentMetadata["mid"]]
                  ka.sendText(msg.to,"deleted")
                  wait["dblacklist"] = False
                else:
                  wait["dblacklist"] = False
                  ka.sendText(msg.to,"It is not in the black list")
#==============================================================================#
              elif wait["contact"] == True:
                msg.contentType = 0
                ka.sendText(msg.to,msg.contentMetadata["mid"])
                if 'displayName' in msg.contentMetadata:
                  contact = ka.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = ka.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    ka.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                else:
                  contact = ka.getContact(msg.contentMetadata["mid"])
                  try:
                    cu = ka.channel.getCover(msg.contentMetadata["mid"])
                  except:
                    cu = ""
                    ka.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "🔼POST link🔼 URL⤵️\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    ka.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
#==============================================================================#
            elif msg.text in ["Key","Staff help","help","Help"]:
                ka.sendText(msg.to,helpMessage)

            elif msg.text in ["Tome1","help creator","Man:creator"]:
                ka.sendText(msg.to,creatorMessage)

            elif msg.text in ["Tome2","help self","Man:selfbot"]:
                ka.sendText(msg.to,publikMessage)

            elif msg.text in ["Tome3","Man:set","Man:setting"]:
                ka.sendText(msg.to,setMessage)

            elif msg.text in ["Tome4","Media","Man:media"]:
                ka.sendText(msg.to,mediaMessage)
#==============================================================================#
            elif msg.text == "Ginfo":
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "Close"
                        else:
                            u = "Open"
                        ka.sendText(msg.to,"[Group name]\n" + str(ginfo.name) + "\n\n[Gid]\n" + msg.to + "\n\n[Group creator]\n" + gCreator + "\n\n[Profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\n\n•Members group : " + str(len(ginfo.members)) + " members\n•MemberInvite : " + sinvitee + " people\n•URL group : " + u + "\n•by : SELFBOT_MAN_PROTECT")
                    else:
                        ka.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can not be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
            elif msg.text is None:
                return
#==============================================================================#
            elif msg.text in ["Creator","Owner"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ua0a82f37270408d4e63b0b1fbb0e4c7f'}
                ka.sendMessage(msg)
#==============================================================================#
            elif msg.text in ["@1","@2"]:
                msg.contentType = 13
                ka.sendMessage(msg.to,"ปรึกษาเรื่องบอท ทักได้คับ\n☞ เปิดสอนเขียนบอท Selfbot กันรัน\n☞ รับทำเชลบอท ในราคาเบาๆ Selfbot⤵️\n🔹 ฟังชั่นบอท 🔹\n  -0- เช็คสมาชิกอ่านกลุ่มได้\n  -1- @แท๊กสมาชิกได้ทั้งกลุ่ม\n  -2- มีข้อความต้อนรับสมาชิก เข้า-ออก (Auto)\n  -3- รายงานสมาชิกที่ยุ่งเกี่ยวกับระบบกลุ่ม (รายงานข้อมูล)\n  -4- มีลูกเล่นหลากหลายและยังแปลภาษาได้ด้วย   \n4.1 (ชุด-Media)   \n4.2 (ชุด-Steal)   \n4.3 (ชุด-Hack)   \n4.4 (ชุด-Translator)\n\n☞สำหรับคนที่:มีอริเยอะ ช่วยป้องกัน 2มาตฐาน\n - (ระบบกันรัน : ยกเลิกรันออโต้)\n - (ล้างรัน : ลงคำสั่งเพื่อยกเลิกกลุ่มรัน Auto)\n - และยังป้องกันการดึงแชทรวม (Virus chat) การดึงเข้าแชทรวมด้วยไวรัส แชท,ไวรัส จะถูกยกเลิกการดึงอัตโนมัติ\n\nหมดห่วงทุกการเกรียน สนใจเรียนวิชาหรือสั่งทำ เปิดเช่า⤵️ สอบถามรายละเอียดเพิ่มเติม..  Link⤵️\n🆔line.me/ti/p/~tomebotline \n\nปล. สำหรับคนที่อยากทำชุดบอท(Protect)..ไว้ป้องกันกลุ่ม\n✅ลูกค้าที่ต้องการทำบอท(kicker)เพิ่ม ตัวล่ะ 50บาท\nTHAILAND : creator & admin bot\nName creator : SELFBOT MAN-PC  􀸂􀅞􏿿􀸂􀅟✧꧁ℳѦれ꧂✧􏿿􀸂􀅟􏿿􀸂􀅠􏿿\nprotect & media  @2018")
#==============================================================================#
            elif "Admin add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
                            kb.findAndAddContactsByMid(target)
                            kc.findAndAddContactsByMid(target)
                            kd.findAndAddContactsByMid(target)
                            ke.findAndAddContactsByMid(target)
                            kf.findAndAddContactsByMid(target)
                            kg.findAndAddContactsByMid(target)
                            kh.findAndAddContactsByMid(target)
                            ki.findAndAddContactsByMid(target)
                            kj.findAndAddContactsByMid(target)
                            admin.append(target)
                            ka.sendText(msg.to,"👑Admin Already Added Boss Man👑")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner add @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner add executing"
                _name = msg.text.replace("Owner add @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            ka.findAndAddContactsByMid(target)
#                            kb.findAndAddContactsByMid(target)
 #                           kc.findAndAddContactsByMid(target)
  #                          kd.findAndAddContactsByMid(target)
   #                         ke.findAndAddContactsByMid(target)
    #                        kf.findAndAddContactsByMid(target)
     #                       kg.findAndAddContactsByMid(target)
      #                      kh.findAndAddContactsByMid(target)
       #                     ki.findAndAddContactsByMid(target)
        #                    kj.findAndAddContactsByMid(target)
                            owner.append(target)
                            ka.sendText(msg.to,"👑Owner Already Added Boss Man👑")
                        except:
                            pass
                print "[Command]Owner add executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Admin remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Admin remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ka.sendText(msg.to,"Admin Deleted 👀")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif "Owner remove @" in msg.text:
              if msg.from_ in owner:
                print "[Command]Owner remove executing"
                _name = msg.text.replace("Owner remove @","")
                _nametarget = _name.rstrip('  ')
                gs = ka.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            ka.sendText(msg.to,"Owner Deleted 👀")
                        except:
                            pass
                print "[Command]Owner remove executed"
              else:
                ka.sendText(msg.to,"You Are Not My Boss !!!")
                ka.sendText(msg.to,"Command Denied")
#==============================================================================#
            elif msg.text in ["Adminlist","Stafflist"]:
              if admin == []:
                  ka.sendText(msg.to,"The stafflist is empty")
              else:
                  ka.sendText(msg.to,"Tunggu...")
                  mc = "👑 Admin selfbot-man 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in admin:
                      mc += "[🔘] " + ka.getContact(mi_d).displayName + "🔏\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Stafflist executed"
#==============================================================================#
            elif msg.text in ["Ownerlist","ownerlist"]:
              if owner == []:
                  ka.sendText(msg.to,"The Owner is empty")
              else:
                  ka.sendText(msg.to,"Tunggu...")
                  mc = "👑 Owner selfbot-man 👑\n𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                  for mi_d in owner:
                      mc += "[🔘] " + ka.getContact(mi_d).displayName + "🔏\n"
                  ka.sendText(msg.to,mc)
                  print "[Command]Ownerlist executed"
#==============================================================================#
            elif msg.contentType == 16:
                if wait["Timeline"] == True:
                    msg.contentType = 0
                    msg.text = "🔘POST📬\n💌URL-timeline⤵️\n" + msg.contentMetadata["postEndUrl"]
                    random.choice(KAC).sendText(msg.to,msg.text)
#==============================================================================#
            elif msg.text in ["List group"]:
                    gid = ka.getGroupIdsJoined()
                    h = ""
		    jml = 0
                    for i in gid:
		        gn = ka.getGroup(i).name
                        h += "╠ [ %s ]\n" % (gn)
		        jml += 1
                    ka.sendText(msg.to,"╔══[ List Group ]\n"+ h +"╚══[ Total Group ] "+str(jml))
#==============================================================================#
            elif "/invitemeto: " in msg.text:
              if msg.from_ in owner:
                gid = msg.text.replace("/invitemeto: ","")
                if gid == "":
                  ka.sendText(msg.to,"Invalid group id")
                else:
                  try:
                    ka.findAndAddContactsByMid(msg.from_)
                    ka.inviteIntoGroup(gid,[msg.from_])
                  except:
                    try:
                      kb.findAndAddContactsByMid(msg.from_)
                      kb.inviteIntoGroup(gid,[msg.from_])
                    except:
                      try:
                        kc.findAndAddContactsByMid(msg.from_)
                        kc.inviteIntoGroup(gid,[msg.from_])
                      except:
                        try:
                          kd.findAndAddContactsByMid(msg.from_)
                          kd.inviteIntoGroup(gid,[msg.from_])
                        except:
                          try:
                            ke.findAndAddContactsByMid(msg.from_)
                            ke.inviteIntoGroup(gid,[msg.from_])
                          except:
                            ka.sendText(msg.to,"Mungkin kami tidak di dalaam grup itu")
#==============================================================================#
            elif msg.text in ["Bot out","Leave all group"]:
              if msg.from_ in owner:
                gid = ka.getGroupIdsJoined()
                gid = kb.getGroupIdsJoined()
                gid = kc.getGroupIdsJoined()
                gid = kd.getGroupIdsJoined()
                gid = ke.getGroupIdsJoined()
                for i in gid:
                  ke.leaveGroup(i)
                  kd.leaveGroup(i)
                  kc.leaveGroup(i)
                  kb.leaveGroup(i)
                  ka.leaveGroup(i)
                if wait["lang"] == "JP":
                  ka.sendText(msg.to,"Sayonara")
                else:
                  ka.sendText(msg.to,"He declined all invitations")
#==============================================================================#
            elif msg.text in ["Notifed on","เปิดแจ้งเตือน","M on"]:
              if msg.from_ in admin:
                if wait["Notifed"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All Notifed On\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนของคุณเเล้ว")
            elif msg.text in ["Notifed off","ปิดแจ้งเตือน","M off"]:
              if msg.from_ in admin:
                if wait["Notifed"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                else:
                    wait["Notifed"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All Notifed Off\n\nปิดเเจ้งเเตือนของคุณเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนของคุณเเล้ว")

            elif msg.text in ["Notifedbot on","เปิดเเจ้งเตือนบอท","Mbot on"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All bot Notifed On\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nเปิดเเจ้งเเตือนบอทเเล้ว")
            elif msg.text in ["Notifedbot off","ปิดแจ้งเตือนบอท","Mbot off"]:
              if msg.from_ in admin:
                if wait["Notifedbot"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                else:
                    wait["Notifedbot"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"All bot Notifed Off\n\nปิดเเจ้งเเตือนบอทเเล้ว")
                    else:
                        ka.sendText(msg.to,"Done\n\nปิดเเจ้งเเตือนบอทเเล้ว")

            elif msg.text in ["Like on","เปิด ไลค์"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"เปิดอยู่แล้ว。")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"เปิดระบบออโต้ไลค์.👌")

            elif msg.text in ["ปิด ไลค์","Like off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"ปิดอยู่แล้ว")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"ปิดระบบออโต้ไลค์.👌")

#========================================
#==================================================================================#
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = ka.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                          random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    ka.sendText(msg.to,"I pretended to cancel and canceled.")
#==============================================================================#
            elif msg.text in ["Cl","Cancel"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = ka.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                          random.choice(KAC).cancelGroupInvitation(msg.to,[_mid])
                    ka.sendText(msg.to,"🌐Cancel All Group Invite🌐")
#==============================================================================#
            elif msg.text in ["Ourl","Url on"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    ka.sendText(msg.to,"🔘OPEN link-Url")
                else:
                    ka.sendText(msg.to,"Can not be used outside the group")
#==============================================================================#
            elif msg.text in ["Curl","Url off"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = ka.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    ka.sendText(msg.to,"📴CLOSE link-Url")
                else:
                    ka.sendText(msg.to,"Can not be used outside the group")
#==============================================================================#
            elif msg.text in ["Cancelinvite on","cancelinvite on"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == True:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"🔘OPEN/PROTECT Cancel Invite")
                  else:
                    ka.sendText(msg.to,"Berhasil mengaktifkan Cancel Invite")
            elif msg.text in ["Cancelinvite off","cancelinvite off"]:
              if msg.from_ in owner:
                if wait["Protectcancel"] == False:
                  if wait["lang"] == "JP":
                    ka.sendText(msg.to,"📴CLOSE/PROTECT Cancel Invite")
                  else:
                    ka.sendText(msg.to,"Berhasil menonaktifkan Cancel Invite")
                
            elif "Gcancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            ka.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            ka.sendText(msg.to,"关了邀请拒绝。要时开请指定人数发送")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            ka.sendText(msg.to,strnum + " The group of people and below decided to automatically refuse invitation")
                        else:
                            ka.sendText(msg.to,strnum + "使人以下的小组用自动邀请拒绝")
                except:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Value is wrong")
                    else:
                        ka.sendText(msg.to,"Bizarre ratings")

#==============================================================================#
            elif msg.text in ["Add:on","เปิด เพิ่มเพื่อน","Auto add:on","Add on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Sudah on Bosqu")
                    else:
                        ka.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Ok Bosqu")
                    else:
                        ka.sendText(msg.to,"Sudah on Bosqu")
            elif msg.text in ["Add:off","Auto add off","ปิด เพิ่มเพื่อน","Add off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Sudah off Bosqu")
                    else:
                        ka.sendText(msg.to,"Ok Bosqu")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Ok Bosqu")
                    else:
                        ka.sendText(msg.to,"Sudah off Bosqu")
#==============================================================================#
            elif "Message set:" in msg.text:
                wait["message"] = msg.text.replace("Message set:","")
                ka.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif "Add message: " in msg.text:
                wait["message"] = msg.text.replace("Add message: ","")
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,"message changed\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    ka.sendText(msg.to,"done。\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Message","Com"]:
                if wait["lang"] == "JP":
                    ka.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    ka.sendText(msg.to,"The automatic appending information is set as follows。\n\n" + wait["message"])
            elif "Coms set:" in msg.text:
                c = msg.text.replace("คอมเม้น:","Coms set:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    ka.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment: " in msg.text:
                c = msg.text.replace("Add comment: ","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    ka.sendText(msg.to,"changed\n\n" + c)

            elif msg.text in ["เปิด คอมเม้น","Com on","Comment:on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"Already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"Already on")
            elif msg.text in ["ปิด คอมเม้น","Com off","Comment:off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"Already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Done")
                    else:
                        ka.sendText(msg.to,"Already off")
            elif msg.text in ["Comment","Coms"]:
                ka.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["HHX1","Hhx1"]:
                ka.sendText(msg.to,"[เช็คข้อความต้อนรับของคุณ]\n\n" + str(wait["acomment"]))

            elif msg.text in ["HHX2","Hhx2"]:
                ka.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนออกจากกลุ่ม]\n\n" + str(wait["bcomment"]))

            elif msg.text in ["HHX3","Hhx3"]:
                ka.sendText(msg.to,"[เช็คข้อความกล่าวถึงคนลบสมาชิก]\n\n" + str(wait["ccomment"]))

            elif "Hhx1:" in msg.text:
                c = msg.text.replace("Hhx1:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["acomment"] = c
                    ka.sendText(msg.to,"➠ ตั้งค่าข้อความต้อนรับ👌\n\n" + c)

            elif "Hhx2:" in msg.text:
                c = msg.text.replace("Hhx2:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["bcomment"] = c
                    ka.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนออกจากกลุ่ม👌\n\n" + c)

            elif "Hhx3:" in msg.text:
                c = msg.text.replace("Hhx3:","")
                if c in [""," ","\n",None]:
                    ka.sendText(msg.to,"เกิดข้อผิดพลาด..!!")
                else:
                    wait["ccomment"] = c
                    ka.sendText(msg.to,"➠ ตั้งค่าข้อความกล่าวถึงคนลบสมาชิก👌\n\n" + c)

            elif msg.text in ["Hhx1 on"]:
                if wait["acommentOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        ka.sendText(msg.to,"Already on")
                else:
                    wait["acommentOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        ka.sendText(msg.to,"Already on")
            elif msg.text in ["Hhx2 on"]:
                if wait["bcommentOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        ka.sendText(msg.to,"Already on")
                else:
                    wait["bcommentOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        ka.sendText(msg.to,"Already on")
            elif msg.text in ["Hhx3 on"]:
                if wait["ccommentOn"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        ka.sendText(msg.to,"Already on")
                else:
                    wait["ccommentOn"] = True
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ เปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        ka.sendText(msg.to,"Already on")

            elif msg.text in ["Hhx1 off"]:
                if wait["acommentOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        ka.sendText(msg.to,"Already off")
                else:
                    wait["acommentOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความต้อนรับเเล้ว👌")
                    else:
                        ka.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx2 off"]:
                if wait["bcommentOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        ka.sendText(msg.to,"Already off")
                else:
                    wait["bcommentOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนออกจากกลุ่ม👌")
                    else:
                        ka.sendText(msg.to,"Already off")
            elif msg.text in ["Hhx3 off"]:
                if wait["ccommentOn"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        ka.sendText(msg.to,"Already off")
                else:
                    wait["ccommentOn"] = False
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"➠ ปิดข้อความกล่าวถึงคนลบสมาชิก👌")
                    else:
                        ka.sendText(msg.to,"Already off")
#==================================================================================#
            elif msg.text in ["Purge on","purge on","Purge: on","purge: on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil mengaktifkan High Protect")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan High Protect")
            elif msg.text in ["Purge off","purge off","Purge: off","purge: off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Berhasil menonaktifkan High Protect")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan High Protect")
#==============================================================================#
            elif msg.text in ["Cancel on","cancel on","ปิดเชิญ"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN/PROTECT ระบบป้องกันเชิญถูกเปิดใช้งาน")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Cancel")
            elif msg.text in ["Cancel off","cancel off","เปิดเชิญ"]:
              if msg.from_ in owner:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE/PROTECT ระบบป้องกันเชิญถูกปิดใช้งาน")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Cancel")
#==============================================================================#     
            elif msg.text in ["Qr on","qr on","เปิดป้องกันลิงก์","ป้องกันลิ้ง"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN/PROTECT URL:QR เปิดระบบป้องกันลิงก์กลุ่ม")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Protect QR")       
            elif msg.text in ["Qr off","qr off","ปิดป้องกันลิงก์"]:
              if msg.from_ in owner:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE/PROTECT URL:QR ปิดระบบป้องกันลิงก์กลุ่ม")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Protect QR")
#==============================================================================#                           
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in owner:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN / Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Info Contact")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in owner:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE / Info Contact")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Info Contact")
#==============================================================================#
            elif msg.text in ["Join on","Autojoin on","เปิดเข้ากลุ่ม"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN Auto Join เข้าร่วมกลุ่มเชิญออโต้")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Join")
            elif msg.text in ["Join off","Autojoin off","ปิดเข้ากลุ่ม"]:
              if msg.from_ in owner:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE Auto Join ปิดเข้าร่วมกลุ่มเชิญ")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Join")
#==============================================================================#
            elif msg.text in ["Leave on","Autoleave on"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN Auto Leave เปิดป้องกันการดึงแชทรวม")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Auto Leave")
            elif msg.text in ["Leave off","Autoleave off"]:
              if msg.from_ in owner:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE Auto Leave ปิดป้องกันการดึงแชทรวม")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Auto Leave")
#==============================================================================#
            elif msg.text in ["Share on","Share:on"]:
              if msg.from_ in owner:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN Mode Share")
                    else:
                        ka.sendText(msg.to,"Berhasil mengaktifkan Mode Share")
            elif msg.text in ["Share off","Share:off"]:
              if msg.from_ in owner:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE Mode Share")
                    else:
                        ka.sendText(msg.to,"Berhasil menonaktifkan Mode Share")
#==============================================================================#
            elif msg.text in ["Sambutan on","Sam:on","เปิดต้อนรับ"]:
              if msg.from_ in owner:
                if wait["Sambutan"] == True:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"🔘OPEN เปิดใช้งานต้อนรับ,บอทตอบโต้")
            elif msg.text in ["Sambutan off","Sam:off","ปิดต้อนรับ"]:
              if msg.from_ in owner:
                if wait["Sambutan"] == False:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"📴CLOSE ปิดใช้งานต้อนรับ,บอทตอบโต้")
#==============================================================================#
            elif msg.text in ["Simisimi on","Simisimi:on","Chatbot:on"]:
                settings["simiSimi"][msg.to] = True
                wait["Simi"] = True
                ka.sendText(msg.to,"🔘OPEN เปิดการสนทนาบอท")
            elif msg.text in ["Simisimi off","Simisimi:off","Chatbot:off"]:
                settings["simiSimi"][msg.to] = False
                wait["Simi"] = False
                ka.sendText(msg.to,"📴CLOSE ปิดการสนทนาบอท")
#==============================================================================#
            elif msg.text in ["เปิด อ่าน","Read on","Read:on"]:
                wait['alwayRead'] = True
                ka.sendText(msg.to,"เปิดอ่านข้อความอัตโนมัติ.👌")
                
            elif msg.text in ["ปิด อ่าน","Read off","Read:off"]:
                wait['alwayRead'] = False
                ka.sendText(msg.to,"ปิดอ่านข้อความอัตโนมัติ.👌")
                
            elif msg.text in ["Tag on","Autorespon:on","Respon on","Respon:on"]:
                wait["detectMention"] = True
                ka.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["Tag off","Autorespon:off","Respon off","Respon:off"]:
                wait["detectMention"] = False
                ka.sendText(msg.to,"Auto Respon OFF")

            elif msg.text in ["Tag1","Tag1"]:
                ka.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag1"]))

            elif msg.text in ["Tag2","Tag2"]:
                ka.sendText(msg.to,"ข้อความแทคล่าสุดคือ\n\n" + str(wait["tag2"]))

            elif msg.text in ["Tag1:"]:
                    wait["tag1"] = msg.text.replace("Tag1: ","")
                    ka.sendText(msg.to,"ข้อความแทคล่าสุดคือ")

            elif msg.text in ["Tag2:"]:
                    wait["tag2"] = msg.text.replace("Tag2: ","")
                    ka.sendText(msg.to,"ข้อความแทคล่าสุดคือ")
            
            elif msg.text in ["Kicktag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                ka.sendText(msg.to,"Auto Kick ON")
                
            elif msg.text in ["Kicktag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                ka.sendText(msg.to,"Auto Kick OFF")
#============================================================================#
            elif "Spam " in msg.text:
                if msg.from_ in admin:
                   txt = msg.text.split(" ")
                   jmlh = int(txt[2])
                   teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+ " ","")
                   tulisan = jmlh * (teks+"\n")
                   #Keke cantik <3
                   if txt[1] == "on":
                        if jmlh <= 10000:
                             for x in range(jmlh):
                                   ka.sendText(msg.to, teks)
                        else:
                               ka.sendText(msg.to, "Out of range! ")
                   elif txt[1] == "off":
                         if jmlh <= 10000:
                               ka.sendText(msg.to, tulisan)
                         else:
                               ka.sendText(msg.to, "Out of range! ")
#====================================================================#
            elif "Mid @" in msg.text:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = ka.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        ka.sendText(msg.to, g.mid)
                    else:
                        pass
#====================================================================#

            elif "Sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                ka.sendText(msg.to,"Berhasil mengaktifkan Sider point")
                
            elif "Sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    ka.sendText(msg.to, "Berhasil menonaktifkan Sider point")
                else:
                    ka.sendText(msg.to, "Setting Masih Mode Off\nMohon Maaf") 
#--------------------------------
            elif msg.text in ["Allprotect on","เปิดชุดป้องกัน"]:
		if msg.from_ in admin: 
                    wait["Protectcancel"] = True
                    wait["Protectcancl"] = True                   
                    wait["Protectjoin"] = True
                    wait["Protectgr"] = True
                    wait["Protection"] = True                     
                    ka.sendText(msg.to,"🔘OPEN/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFF.BOT MAN ON")

		if msg.from_ in admin:
                    wait["Protectcancel"] = False
                    wait["Protectcancl"] = False                    
                    wait["Protectjoin"] = False
                    wait["Protectgr"] = False
                    wait["Protection"] = False                    
                    ka.sendText(msg.to,"📴CLOSE/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFFBOT MAN OFF PROTECTION")
#========================[ P R O T E C T I O N : A L L ]========================#
            elif msg.text in ["ProtectALL on","เปิดระบบป้องกัน"]:
		if msg.from_ in admin:
                    wait["Protectcancel"] = True
                    wait["Protectcancl"] = True                   
                    wait["Protectjoin"] = True
                    wait["Protectgr"] = True
                    wait["Protection"] = True                     
                    ka.sendText(msg.to,"🔘OPEN/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFF.BOT MAN ON")
            elif msg.text in ["ProtectALL off","ปิดระบบป้องกัน"]:
		if msg.from_ in admin:
                    wait["Protectcancel"] = False
                    wait["Protectcancl"] = False                    
                    wait["Protectjoin"] = False
                    wait["Protectgr"] = False
                    wait["Protection"] = False                    
                    ka.sendText(msg.to,"📴CLOSE/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFFBOT MAN OFF PROTECTION")
#==============================[ S E T : T I N G ]==============================#
            elif msg.text in ["Allprotect on","เปิดระบบป้องกัน"]:
		if msg.from_ in admin:
                    wait["contact"] = True
                    wait["Auvv   "] = True                   
                    wait["Protectjoin"] = True
                    wait["Protectgr"] = True
                    wait["Protection"] = True                     
                    ka.sendText(msg.to,"🔘OPEN/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFF.BOT MAN ON")
            elif msg.text in ["Allprotect oft","ปิดระบบป้องกัน"]:
		if msg.from_ in admin:
                    wait["Protectcancel"] = False
                    wait["Protectcancl"] = False                    
                    wait["Protectjoin"] = False
                    wait["Protectgr"] = False
                    wait["Protection"] = False                    
                    ka.sendText(msg.to,"📴CLOSE/PROTECT ระบบป้องกันถูกเปิดใช้งาน")
		else:
		    ka.sendText(msg.to,"TEAM STAFFBOT MAN OFF PROTECTION")
#==============================================================================#
            elif msg.text in ["เชคค่า","เช็คค่า","Set"]:
              if msg.from_ in admin:
                print "Setting pick up..."
                md = "╭══════════════════╮\n║─┅═✥ᴛᴇᴀᴍᵀᴴᴬᴵᴸᴬᴺᴰʙᴏᴛLɪɴᴇ✥═┅─\n║    •─✯͜͡✯TOME★BOTLINE✯͜͡✯─• \n╰══════════════════╯\n╭═════════════════╮\n"
                if wait["likeOn"] == True: md+="╠❂➣ ออโต้ไลค์ : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ ออโต้ไลค์ : ❌ ปิดแล้ว\n"
                if wait["detectMention"] == True: md+="╠❂➣ ตอบแทค : ✔ เปิดแล้ว\n"
                else:md+="╠❂➣ ตอบแทค : ❌ ปิดแล้ว\n"
                if wait["kickMention"] == True: md+="╠❂➣ ออโต้เตะ: ✔ เปิดอยู่\n"
                else:md+="╠❂➣ ออโต้เตะ : ❌ ปิดอยู่\n"
                if wait["Notifed"] == True: md+="╠❂➣ Notifed : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ Notifed : ❌ ปิดอยู่\n"
                if wait["Notifedbot"] == True: md+="╠❂➣ Notifedbot : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ Notifedbot : ❌ ปิดอยู่\n"
                if wait["acommentOn"] == True: md+="╠❂➣ Hhx1 : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ Hhx1 : ❌ ปิดอยู่\n"
                if wait["bcommentOn"] == True: md+="╠❂➣ Hhx2 : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ Hhx2 : ❌ ปิดอยู่\n"
                if wait["ccommentOn"] == True: md+="╠❂➣ Hhx3 : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ Hhx3 : ❌ ปิดอยู่\n"
                if wait["autoCancel"]["on"] == True:md+="╠❂➣ Group cancel :" + str(wait["autoCancel"]["members"]) + " ห้องที่เปิดใช้งาน\n"
                else: md+="╠❂➣ Group cancel : ❌ ปิดอยู่\n"
                if wait["autoAdd"] == True: md+="╠❂➣ ออโต้ เพิ่มเพื่อน : ✔ เปิดอยู่\n"
                else:md+="╠❂➣ ออโต้ เพิ่มเพื่อน : ❌ ปิดอยู่\n"
                if wait["Protectgr"] == True: md+="╠❂➣🔒Protect QR Enable\n"
                else: md+="╠❂➣🔓Protect QR Disable\n"
                if wait["Protectcancl"] == True: md+="╠❂➣🔒Protect Invite Enable\n"
                else: md+="╠❂➣🔓Protect Invite Disable\n"
                if wait["Protectcancel"] == True: md+="╠❂➣🔒Protect Cancel Enable\n"
                else: md+="╠❂➣🔓Protect Cancel Disable\n"
                if wait["Protectjoin"] == True: md+="╠❂➣🔒High protect Enable\n"
                else: md+="╠❂➣🔓High protect Disable\n"
                if wait["contact"] == True: md+="╠❂➣🔘Contact ✔\n"
                else: md+="╠❂➣🔘Contact ✖\n"
                if wait["autoJoin"] == True: md+="╠❂➣🔘Auto Join ✔\n"
                else: md+="╠❂���🔘Auto Join ✖\n"
                if wait["leaveRoom"] == True: md+="╠❂➣🔘Auto Leave ✔\n"
                else: md+="╠❂➣🔘Auto Leave ✖\n"
                if wait["timeline"] == True: md+="╠❂➣🔘Share ✔\n"
                else: md+="╠❂➣🔘Share ✖\n"
                if wait["Sambutan"] == True: md+="╠❂➣🔘Sambutan ✔\n"
                else: md+="╠❂➣🔘Sambutan ✖\n"
                ka.sendText(msg.to,md + "╰══════════════════╯")
                msg.contentType = 13
                msg.contentMetadata = {'mid': admsa}
                ka.sendMessage(msg)
   #           else:
    #            ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Tagall","Tag all","Mention all"]:
              if msg.from_ in owner:
                  group = ka.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      ka.sendMessage(msg)
                  except Exception as error:
                      print error
#==============================================================================#
            elif "แทค" == msg.text.lower():
                 group = ka.getGroup(msg.to)
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
                 cnt.text = "[SELF BOT\n[By.☬ധู้さန້ণق↔ധഖาໄฟ☬]:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 ka.sendMessage(cnt)
#==================================================================================#
            elif msg.text == "Lurking on":
              if msg.from_ in owner:
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
                            ka.sendText(msg.to,"Lurking already on")
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
                        ka.sendText(msg.to, "Set reading point:\n" + readTime)
                            
            elif msg.text == "Lurking off":
              if msg.from_ in owner:
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
                    ka.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del read['readPoint'][msg.to]
                            del read['readMember'][msg.to]
                            del read['readTime'][msg.to]
                    except:
                          pass
                    ka.sendText(msg.to, "Delete reading point:\n" + readTime)
    
            elif msg.text == "Lurking reset":
              if msg.from_ in owner:
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
                    ka.sendText(msg.to, "Reset reading point:\n" + readTime)
                else:
                    ka.sendText(msg.to, "Lurking belum diaktifkan ngapain di reset?")
                        
            elif msg.text == "Lurking":
              if msg.from_ in owner:
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
                             ka.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in read["ROM"][msg.to].items():
                                chiya.append(rom[1])
                                   
                            cmem = ka.getContacts(chiya)
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
                          ka.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
                    else:
                        ka.sendText(msg.to, "Lurking has not been set.")
#==============================================================================#     
            elif msg.text in ["Gurl","Url","ลิงก์กลุ่ม"]:
              if msg.from_ in admin:
                if msg.toType == 2:
                    x = ka.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        ka.updateGroup(x)
                    gurl = ka.reissueGroupTicket(msg.to)
                    ka.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        ka.sendText(msg.to,"Can't be used outside the group")
                    else:
                        ka.sendText(msg.to,"Not for use less than group")
              else:
                ka.sendText(msg.to,"This Command Only For Admin & Owner")
#==============================================================================#
            elif msg.text in ["Masuk","Bot in","Staff in"]:
              if msg.from_ in owner:
                G = ka.getGroup(msg.to)
                ginfo = ka.getGroup(msg.to)
                G.preventJoinByTicket = False
                ka.updateGroup(G)
                invsend = 0
                Ticket = ka.reissueGroupTicket(msg.to)
                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
		kj.acceptGroupInvitationByTicket(msg.to,Ticket)
                time.sleep(0.00001)
                G = ka.getGroup(msg.to)
                G.preventJoinByTicket = True
                ka.updateGroup(G)
                print "Semua Sudah Lengkap"
#==============================================================================#
            elif msg.text in ["timeline"]:
		try:
                    url = ka.activity(limit=10)
		    ka.sendText(msg.to,url['result']['posts'][0]['postInfo']['postId'])
		except Exception as E:
		    print E
#==============================================================================#
            elif msg.text in ["Keluar","Staff out","Out","Staff bye"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        kb.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        kd.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        kf.leaveGroup(msg.to)
			kg.leaveGroup(msg.to)
                        kh.leaveGroup(msg.to)
                        ki.leaveGroup(msg.to)
                        kj.leaveGroup(msg.to)
                        #ka.leaveGroup(msg.to)
                    except:
                        pass
#===============================================================================#
            elif msg.text in ["@bye"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    ginfo = ka.getGroup(msg.to)
                    try:
                        ka.leaveGroup(msg.to)
                    except:
                        pass
#==============================================================================#
            elif msg.text in ["Absen"]:
              if msg.from_ in admin:
                ka.sendText(msg.to,"ルフィ😭")
                kb.sendText(msg.to,"ゾーラー😭")
                kc.sendText(msg.to,"サンジ😭")
                kd.sendText(msg.to,"ウソップ😭")
                ke.sendText(msg.to,"チョッパー😭")
#==============================================================================#
            elif msg.text.lower() in ["respon"]:
                ka.sendText(msg.to,responsename)
                kb.sendText(msg.to,responsename2)
                kc.sendText(msg.to,responsename3)
                kd.sendText(msg.to,responsename4)
                ke.sendText(msg.to,responsename5)
                kf.sendText(msg.to,responsename6)
                kg.sendText(msg.to,responsename7)
                kh.sendText(msg.to,responsename8)
                ki.sendText(msg.to,responsename9)
                kj.sendText(msg.to,responsename10)
#==============================================================================#
            elif msg.text.lower() in ["Sp","Speed"]:
                fake=["0.002253985673451seconds"]
                fspeed=random.choice(fake)
                ka.sendText(msg.to," Progress.....")
                ka.sendText(msg.to,(fspeed)) 
#==============================================================================#
            elif msg.text in ["Sp","Speed","speed"]:
                start = time.time()
                ka.sendText(msg.to, "Bot 1 Processing Request")
                elapsed_time = time.time() - start
                ka.sendText(msg.to, "%sseconds" % (elapsed_time))
#                ki.sendText(msg.to, "%sseconds" % (elapsed_time))
 #               ki2.sendText(msg.to, "%sseconds" % (elapsed_time))
  #              ki3.sendText(msg.to, "%sseconds" % (elapsed_time))
   #             ki4.sendText(msg.to, "%sseconds" % (elapsed_time))
    #            ki5.sendText(msg.to, "%sseconds" % (elapsed_time))
     #           ki6.sendText(msg.to, "%sseconds" % (elapsed_time))
#==============================================================================#
            elif msg.text in ["Banlist","บัญชีดำ"]:
              if msg.from_ in admin:
                if wait["blacklist"] == {}:
                    ka.sendText(msg.to,"Nothing Banned User")
                else:
                    ka.sendText(msg.to,"💂ศาล💹เบิกตัว📚\n🔘จำเลย ผู้กระทำความผิด ขึ้นบัญชีดำ⤵️")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "👤" +ka.getContact(mi_d).displayName + " 👀รอลงอาญา\n"
                    ka.sendText(msg.to,mc)
#==============================================================================#
            elif msg.text in ["Clear ban","Cb","ล้างดำ"]:
              if msg.from_ in owner:
                wait["blacklist"] = {}
                ka.sendText(msg.to,"💀Clear Blacklist Boss Man💀")
#==============================================================================#
            elif "Error!" in msg.text:
              if msg.from_ in owner:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Error!","")
                    gs = ka.getGroup(msg.to)
                    gs = kb.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    gs = kd.getGroup(msg.to)
                    gs = ke.getGroup(msg.to)
                    gs = kf.getGroup(msg.to)
                    gs = kg.getGroup(msg.to)
                    gs = kh.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kj.getGroup(msg.to)
                    ka.sendText(msg.to,"This My Team WAR")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ka.sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in Bots or owner:
                            if target in owner:
                              pass
                            elif target in admin:
                              pass
                            elif target in Bots:
                              pass
                            else:
                              try:
                                klist=[ka,kb,kc,kd,ke,kf,kg,kh,ki,kj]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                              except:
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
#==============================================================================#
            elif msg.text in ["Bot restart"]:
              if msg.from_ in owner:
    	          ka.sendText(msg.to, "Kami Siap Restart\nWaktu Restart Sekitar 10 Detik ")
                  restart_program()
              else:
                ka.sendText(msg.to,"This Command Only For Owner")
 #==============================================================================#
	    elif "/music " in msg.text:
					songname = msg.text.replace("/music ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						ka.sendText(msg.to, "🔘Title : " + song[0] + "\n🔘Length : " + song[1] + "\n🔘Link download : " + song[4])
						ka.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						ka.sendAudioWithURL(msg.to,abc)
						ka.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
#==============================================================================#
            elif '/lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('/lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        ka.sendText(msg.to, hasil)
                except Exception as wak:
                        ka.sendText(msg.to, str(wak))
#==============================================================================#
            elif '/ig ' in msg.text.lower():
                try:
                    instagram = msg.text.lower().replace("/ig ","")
                    html = requests.get('https://www.instagram.com/' + instagram + '/?')
                    soup = BeautifulSoup(html.text, 'html.parser')
                    data = soup.find_all('meta', attrs={'property':'og:description'})
                    text = data[0].get('content').split()
                    data1 = soup.find_all('meta', attrs={'property':'og:image'})
                    text1 = data1[0].get('content').split()
                    tj = text1[0].replace("s150x150/","")
                    user = "🔘Name: " + text[-2] + "\n"
                    user1 = "🔘Username: " + text[-1] + "\n"
                    followers = "🔘Followers: " + text[0] + "\n"
                    following = "🔘Following: " + text[2] + "\n"
                    post = "🔘Post: " + text[4] + "\n"
                    link = "🔘Link: " + "https://www.instagram.com/" + instagram
                    detail = "========INSTAGRAM INFO ========\n"
                    details = "\n========INSTAGRAM INFO ========"
                    ka.sendText(msg.to, detail + user + user1 + followers + following + post + link + details)
                    ka.sendImageWithURL(msg.to, tj)
                except Exception as njer:
                	ka.sendText(msg.to, str(njer))
#==============================================================================#
            elif 'Youtubelink: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ka.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ka.sendText(msg.to,"🔘กรุณาใช้คำศัพท์ที่ถูกต้องและทำการค้นหาอีกครั้ง")
#==============================================================================#
            elif '/yt: ' in msg.text:
                try:
                    textToSearch = (msg.text).replace('Youtube ', "").strip()
                    query = urllib.quote(textToSearch)
                    url = "https://www.youtube.com/results?search_query=" + query
                    response = urllib2.urlopen(url)
                    html = response.read()
                    soup = BeautifulSoup(html, "html.parser")
                    results = soup.find(attrs={'class':'yt-uix-tile-link'})
                    ka.sendText(msg.to,'https://www.youtube.com' + results['href'])
                except:
                    ka.sendText(msg.to,"🔘กรุณาใช้คำศัพท์ที่ถูกต้องและทำการค้นหาอีกครั้ง")
#==============================================================================#
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")

            elif "Say welcome" in msg.text:
                gs = ka.getGroup(msg.to)
                say = msg.text.replace("Say welcome","Selamat Datang Di "+ gs.name)
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#  
            elif "playstore " in msg.text.lower():
                tob = msg.text.lower().replace("playstore ","")
                ka.sendText(msg.to,"Sedang Mencari...")
                ka.sendText(msg.to,"🔘Title : "+tob+"\n🔘Source : Google Play\n🔘Link download : https://play.google.com/store/search?q=" + tob)
                ka.sendText(msg.to,"🔘by : SELFBOT MAN MEDIA @2018")
#==============================================================================#
            elif "/เพลสโตร์:" in msg.text.lower():
                tob = msg.text.lower().replace("/เพลสโตร์:","")
                ka.sendText(msg.to,"Playstore...")
                ka.sendText(msg.to,"🔘Title : "+tob+"\n🔘Source : Google Play\n🔘Link download : https://play.google.com/store/search?q=" + tob)
                ka.sendText(msg.to,"🔘by : SELFBOT MAN MEDIA @2018")
#==============================================================================#
            elif msg.text.lower() in ["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                ka.sendMessage(msg)
#==============================================================================#
            elif "/apakah " in msg.text:
                apk = msg.text.replace("/apakah ","")
                rnd = ["Ya","Tidak","Bisa Jadi","Mungkin"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
                
            elif "/hari " in msg.text:
                apk = msg.text.replace("/hari ","")
                rnd = ["Senin","Selasa","Rabu","Kamis","Jumat","Sabtu","Minggu"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")                

            elif "/berapa " in msg.text:
                apk = msg.text.replace("/berapa ","")
                rnd = ['10%','20%','30%','40%','50%','60%','70%','80%','90%','100%','0%']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
                
            elif "/berapakah " in msg.text:
                apk = msg.text.replace("/berapakah ","")
                rnd = ['1','2','3','4','5','6','7','8','9','10','Tidak Ada']
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")                

            elif "/kapan " in msg.text:
                apk = msg.text.replace("/kapan ","")
                rnd = ["kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi","Tidak Akan Pernah"]
                p = random.choice(rnd)
                lang = 'id'
                tts = gTTS(text=p, lang=lang)
                tts.save("hasil.mp3")
                ka.sendAudio(msg.to,"hasil.mp3")
#==============================================================================#
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ka.sendImageWithURL(msg.to,path)
                except:
                    pass
#==============================================================================#
            elif "/รูปภาพ:" in msg.text:
                search = msg.text.replace("/รูปภาพ:","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    ka.sendImageWithURL(msg.to,path)
                except:
                    pass
#==============================================================================#
            elif "Tr-id " in msg.text:
                isi = msg.text.replace("Tr-id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                ka.sendText(msg.to, A)

            elif "Tr-en " in msg.text:
                isi = msg.text.replace("Tr-en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                ka.sendText(msg.to, A)
#==============================================================================#
            elif "Id@en" in msg.text:
                bahasa_awal = 'id'
                bahasa_tujuan = 'en'
                kata = msg.text.replace("Id@en ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ka.sendText(msg.to,"----Dari Indonesia----\n" + "" + kata + "\n\n----Ke Inggris----\n" + "" + result)

            elif "En@id" in msg.text:
                bahasa_awal = 'en'
                bahasa_tujuan = 'id'
                kata = msg.text.replace("En@id ","")
                url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
                agent = {'User-Agent':'Mozilla/5.0'}
                cari_hasil = 'class="t0">'
                request = urllib2.Request(url, headers=agent)
                page = urllib2.urlopen(request).read()
                result = page[page.find(cari_hasil)+len(cari_hasil):]
                result = result.split("<")[0]
                ka.sendText(msg.to,"----Dari Inggris----\n" + "" + kata + "\n\n----Ke Indonesia----\n" + "" + result)
#==============================================================================#
            elif msg.text.lower() == 'runtime':
                eltime = time.time() - mulai
                van = "Bot Sudah Berjalan Selama :\n"+waktu(eltime)
                ka.sendText(msg.to,van)
#==============================================================================#
            elif msg.text.lower() == '/เช็คเวลาบอท':
                eltime = time.time() - mulai
                van = "🔘ระยะเวลาการทำงานของบอท:⤵️\n"+waktu(eltime)
                ka.sendText(msg.to,van)
#==============================================================================#
            elif "SearchID: " in msg.text:
                userid = msg.text.replace("SearchID: ","")
                contact = ka.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ka.sendMessage(msg)
#==============================================================================#
            elif "LineID: " in msg.text:
                userid = msg.text.replace("LineID: ","")
                contact = ka.findContactsByUserid(userid)
                msg.contentType = 13
                msg.contentMetadata = {'mid': contact.mid}
                ka.sendMessage(msg)
#==============================================================================#
            elif "removechat" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ka.removeAllMessages(op.param2)
                        kb.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kd.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)
                        kf.removeAllMessages(op.param2)
                        kg.removeAllMessages(op.param2)
                        kh.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kj.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ka.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        ka.sendText(msg.to,"Error")
#==============================================================================#
            elif "/ล้างแชทบอท" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        ka.removeAllMessages(op.param2)
                        kb.removeAllMessages(op.param2)
                        kc.removeAllMessages(op.param2)
                        kd.removeAllMessages(op.param2)
                        ke.removeAllMessages(op.param2)
                        kf.removeAllMessages(op.param2)
                        kg.removeAllMessages(op.param2)
                        kh.removeAllMessages(op.param2)
                        ki.removeAllMessages(op.param2)
                        kj.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        ka.sendText(msg.to,"🔘ลบข้อมูลแชทบอทเรียบร้อย")
                    except Exception as error:
                        print error
                        ka.sendText(msg.to,"Error")
#==============================================================================#
            elif msg.text in ["Glist"]:
              if msg.from_ in owner:
                ka.sendText(msg.to, "Tunggu Sebentar. . .")                    
                gid = ka.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "╠" + "%s\n" % (ka.getGroup(i).name +"▶["+str(len(ka.getGroup(i).members))+"]")
                ka.sendText(msg.to,"╔════[ Glist ]════\n" + h + "╠════════════" + "\n║ Total Groups =" +" ["+str(len(gid))+"]\n╚════[ Glist ]════")

            elif msg.text in ["Glistmid"]:   
              if msg.from_ in owner:
                gruplist = ke.getGroupIdsJoined()
                kontak = ke.getGroups(gruplist)
                num=1
                msgs="════════List GrupMid══════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n══════List GrupMid════l═══\n\nTotal Grup : %i" % len(kontak)
                ke.sendText(msg.to, msgs)
#==============================================================================#
        if op.type == 25:
            msg = op.message
            if msg.text.lower() in ["pheytcg fgtagg all"]:
                group = ka.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    ka.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "PHET TAG DONE : " + str(jml) +  " Members"
                cnt.to = msg.to
                ka.sendMessage(cnt)

        if op.type == 26:
            msg = op.message
            if msg.text.lower() in ["1123"]:
                group = ka.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]
                nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                if jml <= 100:
                    mention(msg.to, nama)
                    if jml > 100 and jml < 200:
                        for i in range(0, 100):
                            nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, len(nama)):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                if jml > 200 and jml < 300:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, len(nama)):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                if jml > 300 and jml < 400:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, len(nama)):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                if jml > 400 and jml < 500:
                    for i in range(0, 100):
                        nm1 += [nama[i]]
                    mention(msg.to, nm1)
                    for j in range(101, 200):
                        nm2 += [nama[j]]
                    mention(msg.to, nm2)
                    for k in range(201, 300):
                        nm3 += [nama[k]]
                    mention(msg.to, nm3)
                    for l in range(301, 400):
                        nm4 += [nama[l]]
                    mention(msg.to, nm4)
                    for h in range(401, len(nama)):
                        nm5 += [nama[h]]
                    mention(msg.to, nm5)
                if jml > 500:
                    ka.sendText(msg.to,'Member melebihi batas.')
                cnt = Message()
                cnt.text = "PHET TAG DONE : " + str(jml) +  " Members"
                cnt.to = msg.to
                ka.sendMessage(cnt)
#=====================================================================================#

        if op.type == 26:
            msg = op.message            
            if msg.contentType == 16:
                url = msg.contentMetadata['postEndUrl']
                ka.like(url[25:58], url[66:], likeType=1001)
                ka.comment(url[25:58], url[66:], wait["comment1"])
#                ki1.like(url[25:58], url[66:], likeType=1001)
 #               ki1.comment(url[25:58], url[66:], wait["comment1"])
  #              ki2.like(url[25:58], url[66:], likeType=1001)
   #             ki2.comment(url[25:58], url[66:], wait["comment1"])
    #            ki3.like(url[25:58], url[66:], likeType=1001)
     #           ki3.comment(url[25:58], url[66:], wait["comment1"])
      #          ki4.like(url[25:58], url[66:], likeType=1001)
       #         ki4.comment(url[25:58], url[66:], wait["comment1"])
        #        ki5.like(url[25:58], url[66:], likeType=1001)
         #       ki5.comment(url[25:58], url[66:], wait["comment1"])
          #      ki6.like(url[25:58], url[66:], likeType=1001)
           #     ki6.comment(url[25:58], url[66:], wait["comment1"])
            #    ki7.like(url[25:58], url[66:], likeType=1001)
             #   ki7.comment(url[25:58], url[66:], wait["comment1"])
              #  ki8.like(url[25:58], url[66:], likeType=1001)
               # ki8.comment(url[25:58], url[66:], wait["comment1"])
#                ki9.like(url[25:58], url[66:], likeType=1001)
 #               ki9.comment(url[25:58], url[66:], wait["comment1"])
  #              ki10.like(url[25:58], url[66:], likeType=1001)
   #             ki10.comment(url[25:58], url[66:], wait["comment1"])
                print ("AUTO LIKE SELFBOT")
                print ("Auto Like By.TOMEBOTLINE")
 
#=====================================================================================#
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
#==============================================================================#                                           
        if op.type == 59:
            print op


    except Exception as error:
        print error


while True:
    try:
        Ops = ka.fetchOps(ka.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(ka.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            ka.Poll.rev = max(ka.Poll.rev, Op.revision)
            bot(Op)

