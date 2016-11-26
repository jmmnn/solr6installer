#!/usr/bin/env python

# Setting up the environment

import subprocess
import sys
import os

#List commands to execute hereself.

#Server setup
UPDATE ="sudo apt-get update"
GIT = "sudo apt-get install git"
PIP = "sudo apt-get install python-pip"
JAVA = "sudo apt-get install default-jre"
UNZIP = "sudo apt-get install unzip"

#######  Solr install and start
#Solr configurations
collection = "new"
solr_port = "8080"

GETSOLR = "wget http://archive.apache.org/dist/lucene/solr/5.5.0/solr-5.5.0.tgz"
UNPAKSOLR = "tar -xvf solr-5.5.0.tgz"
STARTSOLR = "solr-5.5.0/bin/solr start -p " + solr_port
CREATE_COLLECTION = "solr-5.5.0/bin/solr create -c " + collection


#######  Python stuff
SOLRPY = "sudo pip install -U solrpy"

#FIRST list of commands in sequence ## Uncomment these for 1st install
cmds = [
    UPDATE,
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

###### Iterates over the FIRST list of commands
count=0
for cmd in cmds:
    count+=1
    print ("____Running Command Number : ",count , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
    

###### Iterates over the SECOND list of commands
count2=0
for cmd in cmds2:
    count2+=1
    print ("____Running Command Number : ",count2 , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
    
###### Iterates over the THIRD list of commands
count3=0
for cmd in cmds3:
    count3+=1
    print ("____Running Command Number : ",count3 , " $" , cmd)
    subprocess.call(cmd, shell=True)
    print ("____Finished Running Command: $" , cmd)
