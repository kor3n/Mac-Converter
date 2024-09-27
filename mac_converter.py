'''MAC Converter

Converts Mac Addresses to XX:XX:XX:XX:XX:XX, XX-XX-XX-XX-XX-XX, XXXX.XXXX.XXXX format

:Authors:
    @kor3n
:Version: 1.2.1
:Date: 27/09/2024
'''
# standard Imports
import re

VERSION = '1.2.1'

BANNER: str = f'''
 ---------------------------------------------------------------------------------
 |    *                                                                          |
 |  (  `     (        (       (                                    )             |
 |  )\))(    )\       )\      )\                )      (   (    ( /(   (   (     |
 | ((_)()\((((_)(   (((_)   (((_)   (    (     /((    ))\  )(   )\()) ))\  )(    |
 | (_()((_))\ _ )\  )\___   )\___   )\   )\ ) (_))\  /((_)(()\ (_))/ /((_)(()\   |
 | |  \/  |(_)_\(_)((/ __| ((/ __| ((_) _(_/( _)((_)(_))   ((_)| |_ (_))   ((_)  |
 | | |\/| | / _ \   | (__   | (__ / _ \| ' \))\ V / / -_) | '_||  _|/ -_) | '_|  |
 | |_|  |_|/_/ \_\   \___|   \___|\___/|_||_|  \_/  \___| |_|   \__|\___| |_|    |
 |                                                                @kor3n v{VERSION}  |
 ---------------------------------------------------------------------------------
'''
MENU: str = '''
 ---------------------------------------------------------------------------------
 |    Usage:                                                                     |
 | 1. Enter/Paste Mac Addresses                                                  |
 | 2. Ctrl-Z + Enter (windows) to convert.                                       |
 | 3. MAC's compatible: XX:XX:XX:XX:XX:XX, XX-XX-XX-XX-XX-XX, XXXX.XXXX.XXXX     |
 ---------------------------------------------------------------------------------
 '''


def main():
    '''Main Function

    This is the main function that calls other required functions to complete the script.
    '''

    print(BANNER)
    print(MENU)
    lower = False
    case = input('Use upper-case formatting for a MAC Addresses? (Y/n): ')
    if case.upper() == "N":
        lower = True
    contents = []
    addresses = []
    contents.append(input('    > '))

    regexco = re.compile('([0-9A-Fa-f]{2}[:]){5}([0-9A-Fa-f]{2})')  # XX:XX:XX:XX:XX:XX
    regexda = re.compile('([0-9A-Fa-f]{2}[-]){5}([0-9A-Fa-f]{2})')  # XX-XX-XX-XX-XX-XX
    regexdd = re.compile('([0-9A-Fa-f]{4}[.]){2}([0-9A-Fa-f]{4})')  # XXXX.XXXX.XXXX

    for mac in contents:
        if regexco.match(mac):
            addresses.append(mac.replace(':', ''))
        elif regexda.match(mac):
            addresses.append(mac.replace('-', ''))
        elif regexdd.match(mac):
            addresses.append(mac.replace('.', ''))
    print('''

 ---------------------------------------------------------------------------------
 |    XX:XX:XX:XX:XX:XX                                                          |
 ---------------------------------------------------------------------------------
    ''')
    if lower:
        for addr in addresses:
            print(f'{addr[:2].upper()}:{addr[2:4].upper()}:{addr[4:6].upper()}:{addr[6:8].upper()}:{addr[8:10].upper()}:{addr[10:12].upper()}')
    elif lower is False:
        for addr in addresses:
            print(f'{addr[:2].lower()}:{addr[2:4].lower()}:{addr[4:6].lower()}:{addr[6:8].lower()}:{addr[8:10].lower()}:{addr[10:12].lower()}')

    print('''

 ---------------------------------------------------------------------------------
 |    XX-XX-XX-XX-XX-XX                                                          |
 ---------------------------------------------------------------------------------
    ''')
    if lower:
        for addr in addresses:
            print(f'{addr[:2].upper()}-{addr[2:4].upper()}-{addr[4:6].upper()}-{addr[6:8].upper()}-{addr[8:10].upper()}-{addr[10:12].upper()}')
    elif lower is False:
        for addr in addresses:
            print(f'{addr[:2].lower()}-{addr[2:4].lower()}-{addr[4:6].lower()}-{addr[6:8].lower()}-{addr[8:10].lower()}-{addr[10:12].lower()}')

    print('''

 ---------------------------------------------------------------------------------
 |    XXXX.XXXX.XXXX                                                             |
 ---------------------------------------------------------------------------------
    ''')
    if lower:
        for addr in addresses:
            print(f'{addr[:4].upper()}.{addr[4:8].upper()}.{addr[8:12].upper()}')
    elif lower is False:
        for addr in addresses:
            print(f'{addr[:4].lower()}.{addr[4:8].lower()}.{addr[8:12].lower()}')

    print('\n\n')


if __name__ == "__main__":
    main()
