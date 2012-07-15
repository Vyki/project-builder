#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import os, sys

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
        print('Cannot create index.html file!')
    else:
        hfile.write("<html>\n<head>\n<title>" + projectName +"</title>\n</head>\n<body>\n<h1>Hello " + projectName + "</h1>\n</body>\n</html>\n")
        hfile.close() 

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


    