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

def check_yaml_exists(file_yaml):
    '''Check that given yaml file exists and return filestream'''
    try:
        ifstream  = open(file_yaml, 'r')
    except IOError:
        print("Required file: "+file_yaml+" does not exist in directory")
    return ifstream

def import_app_details(app_name):
    '''Import app details with given filename and return as dictionary'''

    file_yaml = app_name+".yaml"

    ifstream = check_yaml_exists(file_yaml)

    app_params = yaml.load( ifstream )

    print( app_params )

    ifstream.close()

    return app_params

def write_app_title(ofstream, params):
    '''Check that is exists and write the app title to filestream with heading 1 decoration'''

    try:
        ofstream.write( params["name"] )
        ofstream.write( "\n=====\n" )
    except IOError:
        print("Required dictionary label: \"name\" not found.")


def write_app_version(ofstream, params):
    '''Output version otherwise skip'''

    try:
        'version' in params #ofstream.write( "This documentation refers to  Version: "+app_params["version"]+"\n" )
    except:
        print("Skipping ... no version specified")

    ofstream.write( "This documentation refers to  Version: "+app_params["version"]+"\n" )

#main build script

all_args = (sys.argv)

app_name = all_args[-1]

app_params = import_app_details(app_name)

output_filename = "../"+app_name+".rst"

ofstream = open( output_filename ,'w')

# name

write_app_title(ofstream, app_params)

# version

write_app_version(ofstream, app_params)

# links

try:
    ofstream.write( "Links\n-----\n" )
    ofstream.write( "`"+app_params["name"]+" <"+app_params["website"]+">`_\n" )
    ofstream.write( "`Documentation is available here <"+app_params["website"]+">`_\n" )
except IOError:
    print("Required dictionary label \"links\" not found." )

# license

try:
    ofstream.write( "License\n-----\n" )
    ofstream.write( app_params["name"]+" is available under an `"+app_params["license"]["text"]+" <"+app_params["license"]["link"]+">`_\n" )
    ofstream.write( "Access\n-----\n" )
    ofstream.write( app_params["terms"]+"\n" )
except IOError:
    print("Required dictionary label \"license\" not found." )

# running

try:
    ofstream.write( "Running\n-----\n" )
    ofstream.write( ".. include:: "+app_params["running"]+"\n" )
    ofstream.write( "`Example job script <"+app_params["script"]+">`_\n.....\n" )
    ofstream.write( ".. include:: "+app_params["script"]+"\n" )
except IOError:
    print("Required dictionary label \"running\" not found." )  

try:
    ofstream.write( "Compilatiton\n-----\n" )
    ofstream.write( "`Compiling"+app_params["name"]+"version"+app_params["version"]+"on Isambard (Arm) <"+app_params["compile"]+">`_\n.....\n" )
except IOError:
    print("Required dictionary label \"compile\" not found.")  


ofstream.close()
