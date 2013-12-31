import os
import sys
from transcode import transDirs

def usage():
	print sys.argv[0] + " - Transcode files to the Vorbis format."
	print ""
	print "Usage: "
	print "       " + sys.argv[0] + " dest source"
	print ""
	print "Depending on the types of the parameters given, " + sys.argv[0]
	print "will recursively descend a directory tree and transcode all"
	print "flac files that it finds to Vorbis, placing the transcoded"
	print "files in a mirrored directory tree."
	print ""
	print "source and dest can be any of these combinations:"
	print "  Dest Src"
	print "  ---- ----"
	print "  dir  dir  - The normal way to call " + sys.argv[0]
	print "              This will recursively descend the source"
	print "              directory, transcoding as it descends, and"
	print "              building the mirror tree at the destination"
	print "              given. No existing files are overwritten."
	print "  NOTE: the following are not yet implemented."
	print "  file file - Just transcode one file"
	print "  dir  file - Just transcode one file placing it in the"
	print "              destination diretory."

def listFiles(aPath):
	if os.path.exists(aPath) == False:
		print aPath + " does not exist."
	else:
		print aPath + " found."

def checkParams(dest, src):
	retval = 0

	if not os.path.exists(dest):
		print("ERROR: The destination directory does not exist: " + dest + "\n")
		retval = 1
	elif not os.path.isdir(dest):
		print("ERROR: The destination parameter must be a directory.\n")
		retval = 1
	elif not os.path.exists(src):
		print("ERROR: The source directory does not exist: " + src + "\n")
		retval = 1
	elif not os.path.isdir(src):
		print("ERROR: The source parameter must be a directory.\n")
		retval = 1

	return retval


# check number of parameters
if len(sys.argv) != 3:
	usage()
	sys.exit()

# Check parameter types
# Allowed types:
# Dest Src
# ---- ----
# file file
# dir  dir
# dir  file
dest = sys.argv[1]
src = sys.argv[2]

# Check parameters and launch if successful
if checkParams(dest, src) != 0:
	usage()
else:
	transDirs(dest, src)



