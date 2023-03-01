#!/usr/bin/python3

from ftplib import FTP
from pathlib import Path
import os

ftp = FTP("77.222.57.4")
ftp.login("grandnn201_grandnn", "M8B^4QXHZNLZm2NW")
for item in [w for w in Path('text.txt').read_text(encoding="utf-8").replace("\n", " ").split()]:
    ftp.cwd(f'/{item[0]}')
    try:
        ftp.size(item + '.jpg')
        with open(f'{item}.jpg', 'wb') as file:
            ftp.retrbinary(f'RETR {item}.jpg', file.write)
            print(item)
    except Exception:
        with open('arts.txt', 'a') as f:
            f.write(f'{item}\n')
        continue
ftp.quit()
