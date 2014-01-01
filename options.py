import os
from optparse import OptionParser

def checkParams(dest, src, parser):
	# Check parameter types
	# Allowed types:
	# Dest Src
	# ---- ----
	# file file
	# dir  dir
	# dir  file
	# NOTE: only dir dir is implemented now.

	if not os.path.exists(dest):
		parser.error("ERROR: The destination directory does not exist: " + dest)
	elif not os.path.isdir(dest):
		parser.error("ERROR: The destination parameter must be a directory.")
	elif not os.path.exists(src):
		parser.error("ERROR: The source directory does not exist: " + src)
	elif not os.path.isdir(src):
		parser.error("ERROR: The source parameter must be a directory.")

def parseOptions():
	usage = "usage: %prog [options] destdir srcdir\n"
	usage = usage + "\tdestdir - The destination directory for the transcoded files.\n" 
	usage = usage + "\tsrcdir  - the sourec directory of the transcoded files.\n\n" 
	usage = usage + "Transcode all flac format files (.flac) to vorbis format files (.ogg)\n" 
	usage = usage + "Recursively descend directories if found in srcdir, recreating a mirrored\n" 
	usage = usage + "directory structure in destdir."
	parser = OptionParser(usage=usage)

	parser.add_option("-n", type="int", dest="numThreads", default=1,
			help="the number of threads to use.")
	(options, args) = parser.parse_args()

	if len(args) != 2:
		parser.error("incorrect number of arguments")

	checkParams(args[0], args[1], parser)

	return (options, args)

