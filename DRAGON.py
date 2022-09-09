from ast import Try
from email import header
import requests
import webbrowser
import os
#colors
RED     = '\033[31m'
GREEN   = '\033[32m'
YELLOW  = '\033[33m'
BLUE    = '\033[34m'
MAGENTA = '\033[35m'
CYAN    = '\033[36m'
WHITE   = '\033[37m'
RESET   = '\033[39m'

os.system("title [user:%USERNAME%] [totals users :16] [admin :2] [attacks:51]")
os.system("mode con lines=40 cols=55")
print(f'''\033[33m

        ╔╦╗╦═╗╔═╗╔═╗╔═╗╔╗╔
         ║║╠╦╝╠═╣║ ╦║ ║║║║
        ═╩╝╩╚═╩ ╩╚═╝╚═╝╝╚╝
           version:1.0.0
''')

ip=input(f'$>> IP target :')
def ipinfo():
	
	url=f'https://demo.ip-api.com/json/{ip}?fields=66842623&lang=en'
	headers={
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'demo.ip-api.com',
	'Origin': 'https://ip-api.com',
	'Referer': 'https://ip-api.com/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
	 }
	
	req=requests.post(url,headers=headers)
	print(f'\033[34m[+]  status :'+req.json()['status'])
	print(f'\033[34m[+]  continent :'+req.json()['continent'])
	print(f'\033[34m[+]  continentCode :'+req.json()['continentCode'])
	print(f'\033[34m[+]  country :'+req.json()['country'])
	print(f'\033[341m[+]  countryCode : '+req.json()['countryCode'])
	print(f'\033[34m[+]  region : '+req.json()['region'])
	print(f'\033[34m[+]  regionName :'+req.json()['regionName'])
	print(f'\033[34m[+]  city : '+req.json()['city'])
	print(f'\033[34m[+]  district : '+req.json()['district'])
	print(f'\033[34m[+]  zip : '+req.json()['zip'])
	print(f'\033[34m[+]  timezone : '+req.json()['timezone'])
	print(f'\033[34m[+]  currency : '+req.json()['currency'])
	print(f'\033[34m[+]  isp : '+req.json()['isp'])
	print(f'\033[34m[+]  as : '+req.json()['as'])
	print(f'\033[34m[+]  asname : '+req.json()['asname'])
	print(f'\033[34m[+]  query : '+req.json()['query'])
	print(f'\033[34m[+]  lat : '+str(req.json()['lat']))
	print(f'\033[34m[+]  lon : '+str(req.json()['lon']))
	print(f'\033[34m[+]  offset :'+str(req.json()['offset']))
	print(f'\033[34m[+]  mobile : '+str(req.json()['mobile']))
	print(f'\033[34m[+]  proxy : '+str(req.json()['proxy']))
	print(f'\033[34m[+]  hosting : '+str(req.json()['hosting']))


	
	url1=f'https://ipwhois.pro/{ip}?key=Sxd2AkU2ZL0YtkSR&security=1&lang=en'
	headers1={
	    'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'en-US,en;q=0.9',
	'Connection': 'keep-alive',
	'Host': 'ipwhois.pro',
	'Origin': 'https://ipwhois.io',
	'Referer': 'https://ipwhois.io/',
	'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
	'sec-ch-ua-mobile': '?0',
	'sec-ch-ua-platform': "Windows",
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'cross-site',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36ed-with'
	
	}
	req1=requests.get(url1,headers=headers1)
	
	print(f'\033[34m[+]  calling_code : '+str(req1.json()['calling_code']))
	print(f'\033[34m[+]  img country :   '+str(req1.json()['flag']['img']))
	print(f'\033[34m[+]  vpn : '+str(req1.json()['security']['vpn']))
	print(f'\033[34m[+]  tor : '+str(req1.json()['security']['tor']))
	print(f'\033[34m[+]  anonymous : '+str(req1.json()['security']['anonymous']))

	req3=requests.get(f'https://ipapi.co/{ip}/json/')
	print(f'\033[34m[+]  version : '+str(req3.json()['version']))
	print(f'\033[34m[+]  asn : '+str(req3.json()['asn']))
	print(f'\033[34m[+]  Location : '+str(req.json()['lat'])+','+str(req.json()['lon']))

ipinfo()
myweb = input("This tool was developed by ufo , do you want to visit my personal github? (Y/N)")
if myweb == "y":
	webbrowser.open("https://github.com/ufuu700")
elif myweb == "n":
	print("thank you for using :( ")
else:
	print("i said Y or N =_=")
	exit()
