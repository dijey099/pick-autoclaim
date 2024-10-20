""#line:4
__all__ =[]#line:6
import os #line:8
import time #line:9
from tqdm import tqdm #line:10
from termcolor import colored #line:11
from twocaptcha import TwoCaptcha #line:12
from dotenv import load_dotenv #line:13
from selenium import webdriver #line:14
from selenium .webdriver .common .keys import Keys #line:15
from selenium .webdriver .common .by import By #line:16
from selenium .webdriver .support .ui import WebDriverWait #line:17
from selenium .webdriver .support import expected_conditions as EC #line:18
from selenium .webdriver .firefox .options import Options #line:19
load_dotenv (dotenv_path ="config")#line:22
O00OO00OOO0000O0O =os .getenv ("DOMAIN")#line:24
O00O0000OO0O0O00O =f"https://{O00OO00OOO0000O0O}/faucet.php"#line:25
O0O00000OOOOOOOO0 =os .getenv ("MAIL")#line:26
O000OOOOO00OO0O00 =os .getenv ("PASSWORD")#line:27
OO0O0OOOOOO00O00O =os .getenv ("USERNAME")#line:28
O00O0OOOOOO0000O0 =os .getenv ("SITE_KEY")#line:29
O0O0OO0O00OOO000O =os .getenv ("API_KEY")#line:30
print ("*** Auto Claim for Pick websites ***")#line:32
print ("Auto claiming on "+colored (O00O0000OO0O0O00O .replace ('/login.php',''),'magenta'))#line:33
print (colored ("Buy this script from the author only!",'white','on_red',attrs =['bold'])+"\n")#line:34
print ("Author: "+colored ("Dijey",'green'))#line:35
print ("Maintainer: "+colored ("Dijey",'green'))#line:36
print ("Facebook: "+colored ("https://fb.me/d1j3y",'cyan'))#line:37
print ("Mobile: "+colored ("+261 32 61 968 23\n\n",'yellow'))#line:38
O00OOOOOOOOO00O00 =Options ()#line:40
O00OOOOOOOOO00O00 .add_argument ("--width=240")#line:41
O00OOOOOOOOO00O00 .add_argument ("--height=800")#line:42
O00OOOOOOOOO00O00 .add_argument ("--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36")#line:43
O0000O0O000O0OO0O =webdriver .Firefox (options =O00OOOOOOOOO00O00 )#line:44
time .sleep (15 )#line:45
O0000O0O000O0OO0O .find_element (By .TAG_NAME ,'body').send_keys (Keys .COMMAND +'t')#line:46
def O0OO00O0O0OOO0OOO (O00O0OOOOOO0O0OO0 ):#line:48
	_O0000OO0O000OOOO0 =time .time ()#line:49
	O000OO0OO0O000000 =time .strftime ("%Y-%m-%d %H:%M:%S",time .localtime (_O0000OO0O000OOOO0 ))#line:50
	print (f"[{O000OO0OO0O000000}] {O00O0OOOOOO0O0OO0}")#line:51
O0OO00O0O0OOO0OOO ("Please wait while bypassing turnstil...")#line:53
O0000O0O000O0OO0O .get ("https://m.youtube.com")#line:54
time .sleep (2 )#line:55
O0000O0O000O0OO0O .get (O00O0000OO0O0O00O )#line:56
time .sleep (5 )#line:58
O0OOOOOO00000O0O0 =WebDriverWait (O0000O0O000O0OO0O ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:59
O00O00O0OOOO0OO00 =O0000O0O000O0OO0O .find_element (By .NAME ,"user_email")#line:60
OO000O0OO0O0000OO =O0000O0O000O0OO0O .find_element (By .NAME ,"password")#line:61
O00OO0OO000000000 =O0000O0O000O0OO0O .find_element (By .ID ,"process_login")#line:62
O00O00O0OOOO0OO00 .send_keys (O0O00000OOOOOOOO0 )#line:64
OO000O0OO0O0000OO .send_keys (O000OOOOO00OO0O00 )#line:65
O0000O0O000O0OO0O .switch_to .frame (O0OOOOOO00000O0O0 )#line:67
O0O0O0O0000O000O0 =O0000O0O000O0OO0O .find_element (By .ID ,"recaptcha-anchor")#line:68
O0O0O0O0000O000O0 .click ()#line:69
O0OO00O0O0OOO0OOO ("Solving login captcha...")#line:70
try :#line:73
	WebDriverWait (O0000O0O000O0OO0O ,5 ).until (EC .presence_of_element_located ((By .XPATH ,'//div[@class="recaptcha-checkbox-checkmark" and @style=""]')))#line:74
	O0OO00O0O0OOO0OOO ("Captcha solved successfully!")#line:75
	O0000O0O000O0OO0O .switch_to .default_content ()#line:76
except :#line:77
	O0OO00O0O0OOO0OOO ("Captcha not solved! Trying another way...")#line:78
	O0000O0O000O0OO0O .switch_to .default_content ()#line:79
	O0000O0O000O0OO0O .refresh ()#line:80
	WebDriverWait (O0000O0O000O0OO0O ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:82
	OO0OO0OO0O000O0O0 =TwoCaptcha (O0O0OO0O00OOO000O )#line:83
	OO00O00O0OOOO000O =OO0OO0OO0O000O0O0 .recaptcha (sitekey =O00O0OOOOOO0000O0 ,url =O00O0000OO0O0O00O )#line:84
	O00O0OOOO0OOOOOO0 =OO00O00O0OOOO000O ['code']#line:85
	O0OO00O0O0OOO0OOO ("Successfully solved the Captcha!")#line:86
	O0OO00O0O0OOO0OOO ("Login...")#line:87
	O00O00O0OOOO0OO00 =O0000O0O000O0OO0O .find_element (By .NAME ,"user_email")#line:89
	OO000O0OO0O0000OO =O0000O0O000O0OO0O .find_element (By .NAME ,"password")#line:90
	O00OO0OO000000000 =O0000O0O000O0OO0O .find_element (By .ID ,"process_login")#line:91
	O00O00O0OOOO0OO00 .send_keys (O0O00000OOOOOOOO0 )#line:93
	OO000O0OO0O0000OO .send_keys (O000OOOOO00OO0O00 )#line:94
	O0O0OOO00OOO0O000 =O0000O0O000O0OO0O .find_element (By .ID ,'g-recaptcha-response')#line:96
	O0000O0O000O0OO0O .execute_script (f'arguments[0].value = "{O00O0OOOO0OOOOOO0}";',O0O0OOO00OOO0O000 )#line:97
O00OO0OO000000000 .click ()#line:99
OO0OO0OOO000O0OOO =WebDriverWait (O0000O0O000O0OO0O ,100 ).until (EC .presence_of_element_located ((By .XPATH ,f"//*[contains(text(), '{OO0O0OOOOOO00O00O}')]")))#line:101
if OO0OO0OOO000O0OOO :#line:103
	O0OO00O0O0OOO0OOO (colored ("Logged in!",'green'))#line:104
	while True :#line:105
		try :#line:106
			O0000OO0000O00O00 =WebDriverWait (O0000O0O000O0OO0O ,50 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:107
			O0000O0O000O0OO0O .switch_to .frame (O0000OO0000O00O00 )#line:108
			time .sleep (3 )#line:109
			O0O00OOO0OOO0O0O0 =WebDriverWait (O0000O0O000O0OO0O ,10 ).until (EC .element_to_be_clickable ((By .ID ,"recaptcha-anchor")))#line:110
			O0O00OOO0OOO0O0O0 .click ()#line:111
		except :#line:112
			O0OO00O0O0OOO0OOO ("Claim is not yet available! Come back later...")#line:113
			O0000O0O000O0OO0O .quit ()#line:114
			exit ()#line:115
		try :#line:117
			WebDriverWait (O0000O0O000O0OO0O ,5 ).until (EC .presence_of_element_located ((By .XPATH ,'//div[@class="recaptcha-checkbox-checkmark" and @style=""]')))#line:118
			O0OO00O0O0OOO0OOO ("Captcha solved successfully!")#line:119
			O0000O0O000O0OO0O .switch_to .default_content ()#line:120
		except :#line:121
			O0OO00O0O0OOO0OOO ("Captcha not solved! Trying another way...")#line:122
			O0000O0O000O0OO0O .switch_to .default_content ()#line:123
			O0000O0O000O0OO0O .refresh ()#line:124
			WebDriverWait (O0000O0O000O0OO0O ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:126
			OO0OO0OO0O000O0O0 =TwoCaptcha (O0O0OO0O00OOO000O )#line:127
			OO00O00O0OOOO000O =OO0OO0OO0O000O0O0 .recaptcha (sitekey =O00O0OOOOOO0000O0 ,url =O00O0000OO0O0O00O )#line:128
			O00O0OOOO0OOOOOO0 =OO00O00O0OOOO000O ['code']#line:129
			O0OO00O0O0OOO0OOO ("Successfully solved the Captcha!")#line:130
			O0OO00O0O0OOO0OOO ("Bypassing captcha...")#line:131
			O0O0OOO00OOO0O000 =O0000O0O000O0OO0O .find_element (By .ID ,'g-recaptcha-response')#line:132
			O0000O0O000O0OO0O .execute_script (f'arguments[0].value = "{O00O0OOOO0OOOOOO0}";',O0O0OOO00OOO0O000 )#line:133
		O0OOO00O000O000O0 =O0000O0O000O0OO0O .find_element (By .ID ,"process_claim_hourly_faucet")#line:135
		O0OOO00O000O000O0 .click ()#line:136
		O0OO00O0O0OOO0OOO (colored ("=== New claim triggered ===",'white','on_green'))#line:137
		for OOO00OOOOOO0O00OO in tqdm (range (3605 ),bar_format ='{l_bar}{bar}|{remaining}',leave =False ):#line:139
			time .sleep (1 )#line:140
		O0OO00O0O0OOO0OOO ("Preparing for new claim...")#line:142
		O0000O0O000O0OO0O .refresh ()#line:143
		time .sleep (5 )