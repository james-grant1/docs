# Creates app rst file from yaml and dependent files:
#
# usage
# 
# ipython make_app.py <app_folder> 
#
# app.yaml format::
#
# name: "ExAMPLE"
# version: "0.0.0"
# website: "https://www.google.com"
# docs: "https://lmgtfy.com"
# license:
#   text: "open source"
#   link: "https://opensource.org/licenses"
# terms: "Open source software, all source and binaries are available to all users"
# running: "running.rst"
# script: "script.rst"
# compile: "compile.rst"
# previous: False
#
# Also depends on:
# running.rst - how to run including link to 
# script.rst - example jobscript
# compile.rst - and compilation instructions which may additionally point to example makefile etc.

import yaml
import sys

all_args = (sys.argv)

app_name = all_args[-1]

file_yaml = app_name+".yaml"

try:
    ifstream  = open(file_yaml, 'r')
except IOError:
    print("Required file: "+file_yaml+" does not exist in directory")

app_params = yaml.load( ifstream )

print( app_params )

ifstream.close()

output_filename = "../"+app_name+".rst"

ofstream = open( output_filename ,'w')

try:
    ofstream.write( app_params["name"] )
    ofstream.write( "\n=====\n" )
except:
    print("Required dictionary label: \"name\" not found.")

try:

    ofstream.write( "This documentation refers  Version: "+app_params["version"]+"\n" )

try:
    ofstream.write( "Links\n-----\n" )
    ofstream.write( "`"app_params["name"]+" <"+app_params["website"]+">_\n" )
    ofstream.write( "`Documentation is available here <"+app_params["website"]+">_\n" )

ofstream.close()
