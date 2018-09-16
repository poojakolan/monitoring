import datetime
import os
import shlex
import subprocess
import time

top_dir_data = {}
top_dir_data['data'] = []
server_data = {'ip1': 'username1', 'ip2': 'username2'}
#
for server in server_data:
    server_obj = {}
    server_obj['ip'] = server
    server_obj['disk_data'] = []
    server_obj['top_folders'] = []
    print(server)
    print(server_data[server])
    process1 = subprocess.Popen(shlex.split('ssh '+server_data[server]+'@'+server+' df -h'), stdout=subprocess.PIPE)
    #process1 = subprocess.Popen(shlex.split('df -h'), stdout=subprocess.PIPE)
    stdout1 = process1.communicate()[0]
    disk_list = stdout1.decode().split("\n")
    for disk in disk_list[1:]:
        disk_params = disk.split()
        column=0
        if(len(disk_params) != 0):
            disk_obj = {}
            disk_obj['disk_name'] = disk_params[0]
            disk_obj['total_size'] = disk_params[1]
            disk_obj['used_size'] = disk_params[3]
            disk_obj['used_percent'] = disk_params[4]
            disk_obj['mounted_path'] = disk_params[5]
            server_obj['disk_data'].append(disk_obj)

    cmd = 'ssh -t '+server_data[server]+'@'+server+" 'cd /tc && du -hs * | sort -rh | head -10'"
    top_folder_data = subprocess.check_output(cmd, shell=True)
    top_folder_list = top_folder_data.decode().split("\n")
    
    for folder in top_folder_list[:10]:
        folder_data = folder.split()
        if(len(folder_data) != 0):
            folder_obj = {}
            folder_obj['size'] = folder_data[0]
            folder_obj['name'] = folder_data[1]
            server_obj['top_folders'].append(folder_obj)

    top_dir_data['data'].append(server_obj)

print(top_dir_data)
'''file_name = 'machine_memory_details_'+st+'.xlsx'
from_addr = 
to_addr = 
subject = 
body = 
email_cmd = 'echo '+body+' | mail -s '+subject+' -r '+from_addr+' -a '+file_name+' '+to_addr
process2 = subprocess.Popen(shlex.split(email_cmd), stdout=subprocess.PIPE)
stdout2 = process1.communicate()[0]
print(stdout2)
#remove file
process3 = subprocess.Popen(shlex.split('rm '+file_name), stdout=subprocess.PIPE)
stdout3 = process1.communicate()[0]
print(stdout3)'''
