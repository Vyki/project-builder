#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import os, sys, re

def sinput(text):
    text = raw_input(text)    
    if text == 'exit': exit()
    return text
    
options = sys.argv
projectsDir = None
gitExists = False

while projectsDir == None or os.path.exists(projectsDir) == False:
    projectsDir = sinput("Projects directory: ")

projectName = sinput("Project name: ")
projectDomain = sinput("Project local domain name: ")

projectDir = projectsDir + "/" + projectDomain

if os.path.exists(projectDir):
    print("Project dir already exists")
else:
    try: 
        os.mkdir(projectDir)
        print("Project dir created")
    except OSError:
        exit("Operation failed: cannot create project dir")

if os.path.exists(projectDir + "/index.html") == False:
    try:
        hfile = open(projectDir + "/index.html", "w")
    except IOError:
        print("Cannot create index.html file!")
    else:
        hfile.write("<html>\n<head>\n<title>" + projectName + "</title>\n</head>\n<body>\n<h1>Hello " + projectName + "</h1>\n</body>\n</html>\n")
        hfile.close() 
try:        
    hosts = open("/etc/hosts", "r")
except IOError:
    print("Cannot open /etc/hosts - virtual domain name was not created!")
else:
    domainExists = re.search(r"(127.0.[0|1].1)(\s+)(www.)?(" + projectDomain + ")", hosts.read(), re.MULTILINE | re.IGNORECASE)
    hosts.close()
    
    if domainExists == None:
        if os.access("/etc/hosts", os.W_OK):
            os.system('sed -i "1i127.0.0.1\t' + projectDomain + '\\n127.0.0.1\twww.' + projectDomain + '\\n" /etc/hosts')
        else:
            print('You are not allowed to write to hosts file. Please login as root in following dialog!')
            os.system('sudo sed -i "1i127.0.0.1\t' + projectDomain + '\\n127.0.0.1\twww.' + projectDomain + '\\n" /etc/hosts')

if('git' in options or 'git-ftp' in options):    
    if os.path.exists(projectDir + "/.git"):
        print("Git repository already exists")
    else:
        os.system("git init " + projectDir)
        
if('git-ftp' in options):  
    gFtpLoc = sinput("FTP location: ")
    gFtpUser = sinput("FTP user: ")
    gFtpPass = sinput("FTP password: ")
    
    try:
        hfile = open(projectDir + "/.git/config", "a")
    except IOError:
        print('Cannot open project git configuration file!')
    else:
        hfile.write("[git-ftp]\n\tuser = " + gFtpUser + "\n\tpassword = " + gFtpPass+ "\n\turl = " + gFtpLoc + "\n")
        hfile.close()   
    
os.system("firefox " + projectDomain)


    