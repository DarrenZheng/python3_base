import os
import time

source = ['/tmp/test/source/onlyfile/a.txt', '/tmp/test/source/dir']

#source = '/tmp/test/source/dir'

target_dir = '/tmp/test/backup/'

today = target_dir + time.strftime('%Y-%m-%d')
now = ''

print('today =', today)
print('now = ', now)

os.system('mkdir -p ' + today)

comment = input("do you want to say something?")

if len(comment) == 0:
    now = today + "/" + time.strftime('%Hhours-%Mmins-%Sseconds') + '.zip'
else:
    now = today + "/" + time.strftime('%Hhours-%Mmins-%Sseconds') + \
          '_' + comment + \
          '.zip'

zip_cmd = "zip -qr '%s' %s" %(now, ' '.join(source))

if os.system(zip_cmd) == 0:
    print('备份' + now + ' success')
else:
    print('备份失败')




