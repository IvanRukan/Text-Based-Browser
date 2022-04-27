import sys
import os
from collections import deque
import requests
from bs4 import BeautifulSoup
from colorama import Fore


def website(url):
    string_cont = ''
    if 'https://' not in url:
        url = 'https://' + url
    content = BeautifulSoup(requests.get(url).content, 'html.parser')
    tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'a', 'ul', 'ol', 'li']
    for each in tags:
        if each == 'a':
            temp = content.find_all(each)
            temp = [Fore.BLUE + element.text + '\n' for element in temp]
            temp = ' '.join(temp)
            string_cont += temp
        else:
            temp = content.find_all(each)
            temp = [element.text for element in temp]
            temp = ' '.join(temp)
            string_cont += temp
    last_one.append(string_cont)
    url = url.lstrip('https://')
    url = url[:url.index('.'):]
    with open(f'{arguments[1]}\\{url}', 'w', encoding='utf-8') as f:
        f.writelines(string_cont)
    print(string_cont)


last_one = deque()
arguments = sys.argv
try:
    os.mkdir(f'{arguments[1]}')
except FileExistsError:
    pass
while True:
    link = input()
    if link == 'exit':
        break
    if link.count('.') >= 1:
        website(link)
    elif link == 'back' and len(last_one) != 0:
        print(last_one.popleft())
    else:
        print('Incorrect URL')


