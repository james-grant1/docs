#Script to loop over the rst files in applications folder and add them to the list of files.
# Automates the process of including new software/applications in documentation.

import os

ofstream = open( "applications.rst", 'w' )

ofstream.write( ".. toctree::\n" )
ofstream.write( "   :maxdepth: 1\n" )
ofstream.write( "   :caption: Applications\n\n" )

for file in os.listdir('applications'):
     [filename,extension]=file.split('.')
     print(filename,extension)
     if extension=="rst":
         include_string = "   applications/"+file+"\n"
         ofstream.write( include_string )

ofstream.close()

