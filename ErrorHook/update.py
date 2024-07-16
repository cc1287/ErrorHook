import requests
import os,tempfile
import subprocess

with tempfile.TemporaryDirectory() as temp_dir:
    print('临时目录:', temp_dir)
    temp_file_path = os.path.join(temp_dir, 'setup.py')
    with open(temp_file_path, 'w') as f:
        f.write(requests.get('https://gitee.com/cc1287/error-hook/raw/master/setup.py').text)
    print(subprocess.run('certutil -hashfile '+temp_file_path+' SHA256', shell=True,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE, 
                         universal_newlines=True).stdout)
