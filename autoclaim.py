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
OO0OOOO0000OO0000 =os .getenv ("DOMAIN")#line:24
O0OOO000OOOOOO0O0 =f"https://{OO0OOOO0000OO0000}/faucet.php"#line:25
OOOOOO0OO000OO00O =os .getenv ("MAIL")#line:26
O00O00O00OO00OO00 =os .getenv ("PASSWORD")#line:27
OO00O0O000OOO00O0 =os .getenv ("USERNAME")#line:28
OO0OOOOOOO000OOOO =os .getenv ("SITE_KEY")#line:29
O00OO000OOO0OOO0O =os .getenv ("API_KEY")#line:30
print ("*** Auto Claim for Pick websites ***")#line:32
print ("Auto claiming on "+colored (O0OOO000OOOOOO0O0 .replace ('/login.php',''),'magenta'))#line:33
print (colored ("Buy this script from the author only!",'white','on_red',attrs =['bold'])+"\n")#line:34
print ("Author: "+colored ("Dijey",'green'))#line:35
print ("Maintainer: "+colored ("Dijey",'green'))#line:36
print ("Facebook: "+colored ("https://fb.me/d1j3y",'cyan'))#line:37
print ("Mobile: "+colored ("+261 32 61 968 23\n\n",'yellow'))#line:38
O00000000OOO00OO0 =Options ()#line:40
O00000000OOO00OO0 .add_argument ("--width=240")#line:41
O00000000OOO00OO0 .add_argument ("--height=800")#line:42
O00000000OOO00OO0 .add_argument ("--headless")#line:43
O00000000OOO00OO0 .add_argument ("--user-agent=Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36")#line:44
OOOO0O00O0OOOOOOO =webdriver .Firefox (options =O00000000OOO00OO0 )#line:45
time .sleep (15 )#line:46
OOOO0O00O0OOOOOOO .find_element (By .TAG_NAME ,'body').send_keys (Keys .COMMAND +'t')#line:47
def OO00000OO00OO00OO (OOOOO00OO000OO0O0 ):#line:49
	_O0O0OOOOOOOOOO00O =time .time ()#line:50
	O0OO0OOO00OOO0OOO =time .strftime ("%Y-%m-%d %H:%M:%S",time .localtime (_O0O0OOOOOOOOOO00O ))#line:51
	print (f"[{O0OO0OOO00OOO0OOO}] {OOOOO00OO000OO0O0}")#line:52
OO00000OO00OO00OO ("Please wait while bypassing turnstil...")#line:54
OOOO0O00O0OOOOOOO .get ("https://m.youtube.com")#line:55
time .sleep (2 )#line:56
OOOO0O00O0OOOOOOO .get (O0OOO000OOOOOO0O0 )#line:57
time .sleep (5 )#line:59
O00OOOOO00000000O =WebDriverWait (OOOO0O00O0OOOOOOO ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:60
O00000O000OO0OOOO =OOOO0O00O0OOOOOOO .find_element (By .NAME ,"user_email")#line:61
O0O0OO0OO000OOO00 =OOOO0O00O0OOOOOOO .find_element (By .NAME ,"password")#line:62
O00000OOO0O0OO0OO =OOOO0O00O0OOOOOOO .find_element (By .ID ,"process_login")#line:63
O00000O000OO0OOOO .send_keys (OOOOOO0OO000OO00O )#line:65
O0O0OO0OO000OOO00 .send_keys (O00O00O00OO00OO00 )#line:66
OOOO0O00O0OOOOOOO .switch_to .frame (O00OOOOO00000000O )#line:68
OO000000O0O0O0000 =OOOO0O00O0OOOOOOO .find_element (By .ID ,"recaptcha-anchor")#line:69
OO000000O0O0O0000 .click ()#line:70
OO00000OO00OO00OO ("Solving login captcha...")#line:71
try :#line:74
	WebDriverWait (OOOO0O00O0OOOOOOO ,5 ).until (EC .presence_of_element_located ((By .XPATH ,'//div[@class="recaptcha-checkbox-checkmark" and @style=""]')))#line:75
	OO00000OO00OO00OO ("Captcha solved successfully!")#line:76
	OOOO0O00O0OOOOOOO .switch_to .default_content ()#line:77
except :#line:78
	OO00000OO00OO00OO ("Captcha not solved! Trying another way...")#line:79
	OOOO0O00O0OOOOOOO .switch_to .default_content ()#line:80
	OOOO0O00O0OOOOOOO .refresh ()#line:81
	WebDriverWait (OOOO0O00O0OOOOOOO ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:83
	O0OO0OO0000OOO000 =TwoCaptcha (O00OO000OOO0OOO0O )#line:84
	O0OO0O00O0O0OO0O0 =O0OO0OO0000OOO000 .recaptcha (sitekey =OO0OOOOOOO000OOOO ,url =O0OOO000OOOOOO0O0 )#line:85
	OO000O0OO000O0O0O =O0OO0O00O0O0OO0O0 ['code']#line:86
	OO00000OO00OO00OO ("Successfully solved the Captcha!")#line:87
	OO00000OO00OO00OO ("Login...")#line:88
	O00000O000OO0OOOO =OOOO0O00O0OOOOOOO .find_element (By .NAME ,"user_email")#line:90
	O0O0OO0OO000OOO00 =OOOO0O00O0OOOOOOO .find_element (By .NAME ,"password")#line:91
	O00000OOO0O0OO0OO =OOOO0O00O0OOOOOOO .find_element (By .ID ,"process_login")#line:92
	O00000O000OO0OOOO .send_keys (OOOOOO0OO000OO00O )#line:94
	O0O0OO0OO000OOO00 .send_keys (O00O00O00OO00OO00 )#line:95
	O00OOOO0OOO0OO00O =OOOO0O00O0OOOOOOO .find_element (By .ID ,'g-recaptcha-response')#line:97
	OOOO0O00O0OOOOOOO .execute_script (f'arguments[0].value = "{OO000O0OO000O0O0O}";',O00OOOO0OOO0OO00O )#line:98
O00000OOO0O0OO0OO .click ()#line:100
O00O0OOOO00O0OO00 =WebDriverWait (OOOO0O00O0OOOOOOO ,100 ).until (EC .presence_of_element_located ((By .XPATH ,f"//*[contains(text(), '{OO00O0O000OOO00O0}')]")))#line:102
if O00O0OOOO00O0OO00 :#line:104
	OO00000OO00OO00OO (colored ("Logged in!",'green'))#line:105
	while True :#line:106
		try :#line:107
			O0OO0OO0O00O0O000 =WebDriverWait (OOOO0O00O0OOOOOOO ,50 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:108
			OOOO0O00O0OOOOOOO .switch_to .frame (O0OO0OO0O00O0O000 )#line:109
			time .sleep (3 )#line:110
			OOOOOO00OO0O0OO0O =WebDriverWait (OOOO0O00O0OOOOOOO ,10 ).until (EC .element_to_be_clickable ((By .ID ,"recaptcha-anchor")))#line:111
			OOOOOO00OO0O0OO0O .click ()#line:112
		except :#line:113
			OO00000OO00OO00OO ("Claim is not yet available! Come back later...")#line:114
			OOOO0O00O0OOOOOOO .quit ()#line:115
			exit ()#line:116
		try :#line:118
			WebDriverWait (OOOO0O00O0OOOOOOO ,5 ).until (EC .presence_of_element_located ((By .XPATH ,'//div[@class="recaptcha-checkbox-checkmark" and @style=""]')))#line:119
			OO00000OO00OO00OO ("Captcha solved successfully!")#line:120
			OOOO0O00O0OOOOOOO .switch_to .default_content ()#line:121
		except :#line:122
			OO00000OO00OO00OO ("Captcha not solved! Trying another way...")#line:123
			OOOO0O00O0OOOOOOO .switch_to .default_content ()#line:124
			OOOO0O00O0OOOOOOO .refresh ()#line:125
			WebDriverWait (OOOO0O00O0OOOOOOO ,100 ).until (EC .presence_of_element_located ((By .XPATH ,'//iframe[@title="reCAPTCHA"]')))#line:127
			O0OO0OO0000OOO000 =TwoCaptcha (O00OO000OOO0OOO0O )#line:128
			O0OO0O00O0O0OO0O0 =O0OO0OO0000OOO000 .recaptcha (sitekey =OO0OOOOOOO000OOOO ,url =O0OOO000OOOOOO0O0 )#line:129
			OO000O0OO000O0O0O =O0OO0O00O0O0OO0O0 ['code']#line:130
			OO00000OO00OO00OO ("Successfully solved the Captcha!")#line:131
			OO00000OO00OO00OO ("Bypassing captcha...")#line:132
			O00OOOO0OOO0OO00O =OOOO0O00O0OOOOOOO .find_element (By .ID ,'g-recaptcha-response')#line:133
			OOOO0O00O0OOOOOOO .execute_script (f'arguments[0].value = "{OO000O0OO000O0O0O}";',O00OOOO0OOO0OO00O )#line:134
		OO0O00OO00000OOOO =OOOO0O00O0OOOOOOO .find_element (By .ID ,"process_claim_hourly_faucet")#line:136
		OO0O00OO00000OOOO .click ()#line:137
		OO00000OO00OO00OO (colored ("=== New claim triggered ===",'white','on_green'))#line:138
		for OO0OO0OOO00O00O0O in tqdm (range (3605 ),bar_format ='{l_bar}{bar}|{remaining}',leave =False ):#line:140
			time .sleep (1 )#line:141
		OO00000OO00OO00OO ("Preparing for new claim...")#line:143
		OOOO0O00O0OOOOOOO .refresh ()#line:144
		time .sleep (5 )#line:145
