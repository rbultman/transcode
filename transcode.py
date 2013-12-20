import os
import sys

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
	print "  file file - Just transcode one file"
	print "  dir  file - Just transcode one file placing it in the"
	print "              destination diretory."

def fileType(f):
	if os.path.isfile(f):
		print "It is a regular file."
	elif os.path.isdir(f):
		print "Is is a directory."
	else:
		print "File type is not determined."

def listFiles(aPath):
	if os.path.exists(aPath) == False:
		print aPath + " does not exist."
	else:
		print aPath + " found."

# This function takes two directories and transcodes between them.
def transDirs(destDir, srcDir):
	print "Transcodig files from " + srcDir + " to " + destDir

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


