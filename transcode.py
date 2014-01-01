import os
import sys
from subprocess import call
import shutil
import threading
import time

# avconv -i srcfile -b 320k -c libvorbis destfile
#			rtn = call(["avconv", "-i", src, "-b", "320k", "-c", "libvorbis", target])

files = []

# make a closure to transcode the file
def makeTranscode(dest,src):
	def transcodeFile():
		print "\nTranscoding " + src + " to " + dest
		rtn = call(["avconv", "-i", src, "-b", "320k", "-c", "libvorbis", dest])
		if rtn != 0:
			print("ERROR: avconv returned non-zero: " + str(rtn))
			sys.exit(0)
		else:
			print("\nTranscode complete, {0}.".format(src))
	return transcodeFile

# make a closure to copy the file
def makeCopy(dest, src):
	def copyFile():
		print "\nCopying " + src + " to " + dest
		shutil.copy(src, dest)
		print("\nCopy complete, {0}.".format(src))
	return copyFile

class ActionThread(threading.Thread):
	# action is a closure to be evaluated later
	def __init__(self, action):
		threading.Thread.__init__(self)
		self.action = action

	def run(self):
		# evaluate the closure
		self.action()

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

def doActions(numThreads):
	threads = []

	def removeDeadThreads():
		toDelete = []
		# try to remove threads from thread tracker
		for i in range(0, len(threads)):
			if not threads[i].isAlive():
				toDelete.append(i)
		while len(toDelete) > 0:
			print("\n----> Removing completed thread.")
			i = toDelete.pop()
			threads.pop(i)

	# Process actions by creating worker threads
	while len(files) > 0:
		# try to add threads
		if len(threads) < numThreads:
			print("\n----> Starting new thread.")
			# pop off an action and create a thread to handle it
			action = files.pop()
			newThread = ActionThread(action)
			newThread.start()
			# add thread to thread tracker
			threads.append(newThread)
		else:
			# max threads reached, sleep a little
			print("\n----> Max threads reached, sleeping.")
			time.sleep(1)
			removeDeadThreads()
	
	# wait for all threads to complete
	while len(threads) > 0:
		time.sleep(1)
		removeDeadThreads()

	print("\nProcessing complete.")

# A driver function.
# destDir and srcDir must already exist.
def transDirs(destDir, srcDir, numThreads):
	buildTranscodeList(destDir, srcDir)
	print "Found " + str(len(files)) + " files to transcode and/or copy."
	doActions(numThreads)

