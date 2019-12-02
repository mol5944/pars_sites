import requests
from os import mkdir
from os.path import exists
from threading import Thread
from time import sleep
from shutil import rmtree

wordlist = input('wordlist: ')
timeout = int(input('timeout: '))
folder_save = input('folder_save: ')
threads = int(input('threads: '))
sleep_thr = int(input('sleep_threads: '))

def generator(string):
    for word in string:
        url = word.replace('\n','')
        yield url

def save_html(file_name,html):
    with open(file_name,'wt') as file:
        file.write(html)

def request(url,timeout,file_name):
    print('checked: ' + url)
    try:
        resp = requests.get(url,timeout=timeout)
    except:
        pass
    else:
        save_html(file_name,resp.text)

if exists(folder_save):
    print('########################################')
    print('Folder already exists.')
    if input('Delete this folder? [yes/no]: ').lower() == 'yes':
        rmtree(folder_save)
    else:
        quit()
    print('########################################')

mkdir(folder_save)
count = 1
count_thr = 0

with open(wordlist,'rt',errors='ignore') as dictionary:
    for url in generator(dictionary):
        if count_thr > threads:
            count_thr = 0
            sleep(sleep_thr)
        
        file_save = folder_save + '/' 'index_' + str(count) + '.html'
        count += 1

        thr = Thread(target=request, args=(url,timeout,file_save,))
        thr.start()

        count_thr += 1
