#!/usr/bin/env python

# By Ivan Eguiguren
# 15/01/2016
# based on information found in:
# http://aaronparecki.com/articles/2011/07/10/1/enabling-ssh-on-the-seagate-blackarmor-nas-220
#

import pycurl, getpass, re, paramiko

bug = '/backupmgt/killProcess.php?session=9999999999;'
enableSSH = '%2Fusr%2Fsbin%2Fdropbear;'

def getPassword():
    password = getpass.getpass(prompt='Insert the new root password ', stream=None)
    return password


def getIP():
    correct = False
    while not correct:
        print "Insert the NAS's IP: "
        IP = raw_input()
        regex = re.findall(r'(?:\d{1,3}\.){3}\d{1,3}', IP)
        if regex:
            values = regex[0].split('.')
            for v in values:
                if int(v) >= 0 and int(v) <= 255:
                    correct = True
                else:
                    correct = False
        else:
            print "IP not valid: " + IP
    return IP


#getting IP to connect to the NAS
ip = getIP()

# Enabling ssh process
curl = pycurl.Curl()
curl.setopt(curl.URL, 'http://' + ip + bug + enableSSH)
curl.perform()
print''

#changing root password
passwd = getPassword()
curl.setopt(curl.URL, 'http://' + ip + bug + 'echo+' + passwd + '+%7C+passwd+--stdin;' )
curl.perform()
print ''

#activating ssh on NAS boot
dropbear = 'echo "ssh stream tcp nowait root /usr/sbin/dropbear dropbear -i" >> /etc/inetd.conf'
ssh = paramiko.SSHClient()
try:
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip, username="root", password=passwd)
    ssh.exec_command( dropbear )
    ssh.close()
    print "ssh server activated on boot"
except:
    print "Error activating ssh on boot"