#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys
import os

#List commands to execute hereself.

#Server setup
GIT = "sudo apt-get install git"
PIP = "sudo apt-get install python-pip"
JAVA = "sudo apt-get install openjdk-8-jre"
UNZIP = "sudo apt-get install unzip"

#######  Solr install and start
#Solr configurations
collection = "new"
solr_port = "8080"

GETSOLR = "wget http://archive.apache.org/dist/lucene/solr/6.0.0/solr-6.0.0.tgz"
UNPAKSOLR = "tar -xvf solr-6.0.0.tgz"
STARTSOLR = "solr-6.0.0/bin/solr start -p " + solr_port
CREATE_COLLECTION = "solr-6.0.0/bin/solr create -c " + collection


#######  Python stuff
SOLRPY = "sudo pip install -U solrpy"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    GIT,
    PIP,
    JAVA,
    UNZIP,
    GETSOLR,
    UNPAKSOLR 
    ]


#SECOND list of commands in sequence ## Comment Creata_collection after the first install
cmds2 = [ 
    STARTSOLR,
    CREATE_COLLECTION
    ]
    
    
#THIRD list of commands in sequence
cmds3 = [ 
    SOLRPY
    ]

dir = os.getcwd()
print dir

###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print "Running Command Number %s" % count
    subprocess.call(cmd, shell=True)
    

###### Iterates over the SECOND list of commands
count2=0
for cmd in cmds2:
    count2+=1
    print "Running Command Number %s" % count2
    subprocess.call(cmd, shell=True)
    
###### Iterates over the THIRD list of commands
count3=0
for cmd in cmds3:
    count3+=1
    print "Running Command Number %s" % count3
    subprocess.call(cmd, shell=True)
