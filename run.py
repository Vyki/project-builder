#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
import os

def sinput(text):
    text = raw_input(text)    
    if text == 'exit': exit()
    return text
    
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
    file = open(projectDir + "/index.html", "w")
    file.write("<html>\n<head>\n<title>" + projectName +"</title>\n</head>\n<body>\n<h1>Hello " + projectName + "</h1>\n</body>\n</html>\n")
    file.close() 

    
if os.path.exists(projectDir + "/.git"):
    print("Git repository already exists")
else:
    os.system("git init " + projectDir)
    
os.system("firefox " + projectDomain)


    