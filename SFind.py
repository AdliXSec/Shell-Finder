import os
from platform import system
from sys import argv

try:
    import requests
except ImportError:
    os.system('pip install requests')
    exit(' Reload This Tools')

if system() == 'Windows':
    hapus = 'cls'
else:
    hapus = 'clear'

brown = '\033[33m'
greenLight = '\033[32m'
cyan = '\033[36m'
red = '\033[31m'
yellow = '\033[33m'
blue = '\033[34m'
white = '\033[37m'
purple = '\033[35m'

def banner():
    print(f'''
    
    {cyan}               ,.
    {cyan}              /-|
    {cyan}             (--;
    {cyan}            (,-'; {greenLight}    _____ _          _ _          
    {cyan}          _/_.-'; {greenLight}   / ____| |        | | |         
    {cyan}        _/-.__._< {greenLight}  | (___ | |__   ___| | |         
    {cyan}     .-'`-.__   '\{greenLight}   \___ \| '_ \ / _ \ | |  {yellow}|   
    {cyan}  .'`---=___`===':{greenLight}   ____) | | | |  __/ | |  {yellow}| {red}Author : AdliXSec
    {cyan} /_..---' ___.--.'{greenLight}  |_____/|_| |_|\___|_|_|  {yellow}| {red}Team   : Dark Clown Security
    {cyan} |` ___.--' __ .i|{greenLight}   ______ _           _    {yellow}| 
    {cyan} |-' ___.--'_.8:E|{greenLight}  |  ____(_)         | |   
    {cyan} \,-'  __.-/88::E!{greenLight}  | |__   _ _ __   __| | ___ _ __ 
    {cyan}  `-.,' _.'|88::E|{greenLight}  |  __| | | '_ \ / _` |/ _ \ '__|
    {cyan}     `;'../88:: E;{greenLight}  | |    | | | | | (_| |  __/ |   
    {cyan}      | .'!88::E"/{greenLight}  |_|    |_|_| |_|\__,_|\___|_|   
    {cyan}      /.''!"iiE /  {yellow} ________________________________
    {cyan}      `--'`._.-'  {red}GitHub : https://github.com/AdliXSec                             
        ''')

def cmsscan(url):
    cmsop = requests.get(url+'/admin',timeout=7)
    cmsjoomla = requests.get(url + '/administrator/index.php',timeout=7)
    cmswp = requests.get(url + '/wp-login.php',timeout=7)
    cmswp2 = requests.get(url + '/wp-admin/')
    cmsdrupal = requests.get(url + '/admin',timeout=7)
    if 'dashboard' in cmsop.text:
        cms = 'OPencarte'
    elif 'Joomla' in cmsjoomla.text:
        cms = 'Joomla'
    elif 'WordPress' in cmswp.text:
        cms = 'Wordpress'
    elif cmswp2.status_code == 302 or cmswp2.status_code == 200:
        cms = 'Wordpress'
    elif 'sites/default' in cmsdrupal.text:
        cms = 'Drupal'
    else:
        cms = 'Other'

    return cms

def main():
    os.system(hapus)
    try:
        print('\n')
        url = open(argv[1], 'r')
        banner()
        print('')
        for site in url.read().splitlines():

            if cmsscan(site) == 'Wordpress':
                dir = open('dir/dirwp.txt', 'r')
            if cmsscan(site) == 'Joomla':
                dir = open('dir/dirjoomla.txt', 'r')
            if cmsscan(site) == 'Drupal':
                dir = open('dir/dirdrupal.txt', 'r')
            if cmsscan(site) == 'OPencarte':
                dir = open('dir/diropencarte.txt', 'r')
            elif cmsscan(site) == 'Other':
                dir = open('dir/dir.txt', 'r')

            for d in dir.read().splitlines():
                shell = open('shell/shell.txt', 'r')
                for x in shell.read().splitlines():
                    link = site + d + '/' + x
                    c = requests.get(link)
                    if 'not' in c.text or 'found' in c.text and c.status_code == 200:
                        print(f'{red} [-] Page Not Found in : {link}')
                    elif 'public_html' in c.text or 'password' in c.text  or 'shell' in c.text and c.status_code == 200:
                        print(f'{greenLight} [+] Shell Found in : {link} {white}[CMS {cmsscan(site)}]')
                    else:
                        print(f'{red} [-] Shell Not Found in : {link}')

    except IndexError:
        banner()
        print(' How To Use : ')
        print(f'\n{white} python SFind.py <listweb.txt> \n')
        exit()
    except:
        print(' Unknown Error ! ')
        exit()

if __name__ == '__main__':
    main()