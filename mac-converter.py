import re

## Converts Mac Addresses to XX:XX:XX:XX:XX:XX, XX-XX-XX-XX-XX-XX, XXXX.XXXX.XXXX format



def Main():
	print('''
 ---------------------------------------------------------------------------------
 |    *                                                                          |
 |  (  `     (        (       (                                    )             |
 |  )\))(    )\       )\      )\                )      (   (    ( /(   (   (     |
 | ((_)()\((((_)(   (((_)   (((_)   (    (     /((    ))\  )(   )\()) ))\  )(    |
 | (_()((_))\ _ )\  )\___   )\___   )\   )\ ) (_))\  /((_)(()\ (_))/ /((_)(()\   |
 | |  \/  |(_)_\(_)((/ __| ((/ __| ((_) _(_/( _)((_)(_))   ((_)| |_ (_))   ((_)  |
 | | |\/| | / _ \   | (__   | (__ / _ \| ' \))\ V / / -_) | '_||  _|/ -_) | '_|  |
 | |_|  |_|/_/ \_\   \___|   \___|\___/|_||_|  \_/  \___| |_|   \__|\___| |_|    |
 |                                                                   kor3n V1.0  |
 ---------------------------------------------------------------------------------
''')
	print(''' ---------------------------------------------------------------------------------
 |    Usage:                                                                     |
 | 1. Enter/Paste Mac Addresses                                                  |
 | 2. Ctrl-Z + Enter (windows) to convert.                                       |
 | 3. MAC's compatible: XX:XX:XX:XX:XX:XX, XX-XX-XX-XX-XX-XX, XXXX.XXXX.XXXX     |
 ---------------------------------------------------------------------------------
 ''')
	lower = 0
	case = input('Use upper-case formatting for Macaddresses? (Y/n): ')
	if case.upper() == "N":
		lower = 1
	print('Mac Addresses:')
	contents = []
	addresses = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		contents.append(line)
	
	## Clean input for mac addresses and remove ":-."
	regexco = re.compile('([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})') # XX:XX:XX:XX:XX:XX
	regexda = re.compile('([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})') # XX-XX-XX-XX-XX-XX
	regexdd = re.compile('([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})') # XXXX.XXXX.XXXX
	
	for mac in contents:
		if regexco.match(mac):
			addresses.append(mac.replace(':',''))
		elif regexda.match(mac):
			addresses.append(mac.replace('-',''))
		elif regexdd.match(mac):
			addresses.append(mac.replace('.',''))
	
	#print(addresses)
	#print(addresses[0].upper())
	#print(addresses[0].lower())
	## Convert Mac Addresses for XX:XX:XX:XX:XX:XX
	print(''' 

 ---------------------------------------------------------------------------------
 |    XX:XX:XX:XX:XX:XX                                                          |
 ---------------------------------------------------------------------------------
	''')
	if lower == 0:
		for addr in addresses:
			print(addr[:2].upper() + ':' + addr[2:4].upper() + ':' + addr[4:6].upper() + ':' + addr[6:8].upper() + ':' + addr[8:10].upper() + ':' + addr[10:12].upper())
	elif lower == 1:
		for addr in addresses:
			print(addr[:2].lower() + ':' + addr[2:4].lower() + ':' + addr[4:6].lower() + ':' + addr[6:8].lower() + ':' + addr[8:10].lower() + ':' + addr[10:12].lower())
			
	print(''' 

 ---------------------------------------------------------------------------------
 |    XX-XX-XX-XX-XX-XX                                                          |
 ---------------------------------------------------------------------------------
	''')
	if lower == 0:
		for addr in addresses:
			print(addr[:2].upper() + '-' + addr[2:4].upper() + '-' + addr[4:6].upper() + '-' + addr[6:8].upper() + '-' + addr[8:10].upper() + '-' + addr[10:12].upper())
	elif lower == 1:
		for addr in addresses:
			print(addr[:2].lower() + '-' + addr[2:4].lower() + '-' + addr[4:6].lower() + '-' + addr[6:8].lower() + '-' + addr[8:10].lower() + '-' + addr[10:12].lower())
		
	print(''' 

 ---------------------------------------------------------------------------------
 |    XXXX.XXXX.XXXX                                                             |
 ---------------------------------------------------------------------------------
	''')
	if lower == 0:
		for addr in addresses:
			print(addr[:4].upper() + '.' + addr[4:8].upper() + '.' + addr[8:12].upper())
	elif lower == 1:
		for addr in addresses:
			print(addr[:4].lower() + '.' + addr[4:8].lower() + '.' + addr[8:12].lower())
	
	print('\n\n')
	
	
if __name__ == "__main__":
	Main()