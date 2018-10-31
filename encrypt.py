import subprocess
from shutil import copyfile
import sys
import os

if(len(sys.argv) != 5):
    print("Usage python $.py in_file out_file times password")
    sys.exit(0)

in_file = sys.argv[1]
out_file = sys.argv[2]
times = int(sys.argv[3])
password = sys.argv[4]

copyfile(in_file, 'input_file') #src, dst

for i in range(0,times):
    cmd = 'openssl aes-256-cbc -in input_file -out ' + out_file + ' -pass pass:' + password + ' -base64' 
    print subprocess.check_output(cmd, shell = True)
    print 'times : ' , i+1
    if(times > 1):
        copyfile(out_file, 'input_file')

os.system('rm -f input_file')
