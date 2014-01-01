transcode
=========

Transcode (and sync) audio files between two directory trees

This utility will recursively descend the source directory tree.  If it finds
a flac file, it will transcode the file to the vorbis format into the 
destination directory tree.  All other files are merely copied.  The structure
of the destination directory tree will mirror that of the source directory
tree.  A source file is treated as a FLAC-encoded audio file if it has the 
flac extension.
The base name of the transcoded files will be the same.  The extension
of the transcoded files will be ogg.

The use case for this utility is where you have a CD collection which has
been ripped to FLAC format and you want to transcode to the lossy but
compressed vorbis format prior to copying the transcoded files to an audio
player capable of playing vorbis-encoded files.

It should be trivial to extend this utility to use other audio encoding
formats.

