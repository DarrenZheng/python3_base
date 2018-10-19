import os
import time

source = ['/tmp/test/source/onlyfile/a.txt', '/tmp/test/source/dir']

#source = '/tmp/test/source/dir'

target_dir = '/tmp/test/backup/'

real_source = ""

for item in source:
    real_source = real_source + item + ' '

target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_cmd = "zip -qr '%s' %s" %(target, real_source)

if os.system( zip_cmd ) == 0:
    print("backup", target, "success")
else:
    print("backup fail!")

