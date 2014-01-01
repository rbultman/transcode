from transcode import transDirs
from options import parseOptions

(options, args) = parseOptions()

print("Number of threads requested: {0}".format(options.numThreads))

transDirs(args[0], args[1], options.numThreads)

