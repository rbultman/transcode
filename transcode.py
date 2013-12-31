import os
import sys
from subprocess import call
import shutil

# avconv -i srcfile -b 320k -c libvorbis destfile
#			rtn = call(["avconv", "-i", src, "-b", "320k", "-c", "libvorbis", target])

files = []

# make a closure to transcode the file
def makeTranscode(dest,src):
	def transcodeFile():
		print "Transcoding " + src + " to " + dest
		rtn = call(["avconv", "-i", src, "-b", "320k", "-c", "libvorbis", dest])
		if rtn != 0:
			print("ERROR: avconv returned non-zero: " + str(rtn))
			sys.exit(0)
	return transcodeFile

# make a closure to copy the file
def makeCopy(dest, src):
	def copyFile():
		print "Copying " + src + " to " + dest
		shutil.copy(src, dest)
	return copyFile

def handleFiles(dest, src):
	# handle files by copying or transcoding
	(srcPath, srcFile) = os.path.split(src)
	(basename, extension) = os.path.splitext(srcFile)
	if extension == ".flac":
		# got a flac file to transcode
		# see if the dest exists
		target = os.path.join(os.path.dirname(dest), basename + ".ogg")
		if not os.path.exists(target):
			files.append(makeTranscode(target, src))
	else:
		# just copy the file
		target = os.path.join(os.path.dirname(dest), srcFile)
		if not os.path.exists(target):
			files.append(makeCopy(target,src))

# This function takes two directories and transcodes between them.
def buildTranscodeList(destDir, srcDir):
	listDir = os.listdir(srcDir)
	if not os.path.exists(destDir):
		os.mkdir(destDir)
	for f in listDir:
		if os.path.isfile(srcDir + os.sep + f):
			handleFiles(destDir + os.sep + f, srcDir + os.sep + f)
		elif os.path.isdir(srcDir + os.sep + f):
			buildTranscodeList(destDir + os.sep + f, srcDir + os.sep + f)

def transDirs(destDir, srcDir):
	buildTranscodeList(destDir, srcDir)
	print "Found " + str(len(files)) + " files to transcode and/or copy."
	for a in files:
		a()

