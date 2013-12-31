import os
import sys

# avconv -i srcfile -b 320k -c libvorbis destfile

def handleFiles(dest, src):
	# handle files by copying or transcoding
	(srcPath, srcFile) = os.path.split(src)
	# print("\tBase: " + srcPath + ", File: " + srcFile)
	(basename, extension) = os.path.splitext(srcFile)
	# print("\t\tRoot: " + basename + ", Ext: " + extension)
	if extension == ".flac":
		# got a flac file to transcode
		print("\tTranscoding " + src)
		# see if the dest exists
		target = os.path.join(os.path.dirname(dest), basename + ".ogg")
		if not os.path.exists(target):
			print("\tDestination: " + target)
		else:
			print("\tDestination exists, doing nothing.")
	else:
		# just copy the file
		target = os.path.join(os.path.dirname(dest), srcFile)
		print("\tCopying " + target)


# This function takes two directories and transcodes between them.
def transDirs(destDir, srcDir):
	print(os.path.abspath(destDir) + " <= " + os.path.abspath(srcDir))
	listDir = os.listdir(srcDir)
	for f in listDir:
		if os.path.isfile(srcDir + os.sep + f):
			handleFiles(destDir + os.sep + f, srcDir + os.sep + f)
		elif os.path.isdir(srcDir + os.sep + f):
			transDirs(destDir + os.sep + f, srcDir + os.sep + f)



