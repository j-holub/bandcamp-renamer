#!/usr/bin/env python

import argparse
import os
import re
import sys

# ###### #
# Config #
# ###### #

# formats that can be downloaded from bandcamp
file_formats = ['.mp3', '.flac', '.aac', '.ogg', '.oga', '.m4a', '.CAF', '.wav', '.aiff', '.aif', '.aifc']

# regex to check for the correct file
#            Artistname        Albumtitle         TrackNr     Songtitle
pattern = "(\w|\s|\d|\.)*-(\w|\s|\d|\(|\)|\.|,)*-\s\d\d\s(\w|\s|\d|\(|\)|\.|,)*"
regex = re.compile(pattern)

# ######### #
# Functions #
# ######### #


# Parses a filename from bandcamp and extracts the information about the artist, album, tracknumber
# and title
#
# @param song - filename (without the extension)
#
# @return object containing the infos
# 'artist', 'album', 'tracknumber', 'songname'
def parseInfoFromSong(song):
	# get the arist-, album- and songname
	artist, album, songname = str.split(song, ' - ')
	# seperate track number from track title
	tracknumber = songname[0:2]
	songname = songname[2:]

	# return object
	songinfo = {
		'artist': artist,
		'album': album,
		'songname': songname,
		'tracknumber': tracknumber
	}

	return songinfo

# --------------------------


# Takes the absolute path to a file and renames it according to the format given
#
# @param path   - absolute path to the songfile
# @param format - format that the file should be renamed to
# @param verbose (optional) - if set, messages of the renaming are output to the command line
# 
# @return void 
def renameSongFile(path, format, verbose=False):

	# split the path
	dir = os.path.dirname(path)
	filename, extension  = os.path.splitext(os.path.basename(path))

	# get the songinfo
	info = parseInfoFromSong(filename)

	# apply the songinfo to the format string
	new_songname = format

	# artist
	new_songname = str.replace(new_songname, "%a", info['artist'])
	# album
	new_songname = str.replace(new_songname, "%A", info['album'])
	# songname
	new_songname = str.replace(new_songname, "%t", info['songname'])
	# track number
	new_songname = str.replace(new_songname, "%n", info['tracknumber'])

	# rename the file
	os.rename(path, "%s/%s%s" % (dir, new_songname, extension))

	# if verbose was set print the renaming
	if(verbose):
		print "--------------------------------------------"
		print "Directory: %s" % dir
		print "Old: '%s%s'" % (filename, extension)
		print "New: '%s%s'" % (new_songname, extension)
		print "--------------------------------------------"


# -------------------------------

# Takes the absolute path to a directory containing the song files
# If these files match one of the extensions specified in 'file_formats'
# and matches the bandcamp file naming convention, these files are renamed
# 
# @param path - absolute path to the directory containing the files
# @param format - format that the file should be renamed to
# @param recursive (optional) - if set, subdirectories are renamed as well in a recursive fashion
# @param verbose (optional) - if set, messages of the renaming are output to the command line
#
# @return void
def renameDirectory(path, format, recursive=False, verbose=False):


	# list all the files in the directory
	list_of_files = os.listdir(path)

	# iterate through everything found
	for item in list_of_files:

		# if it's a directory and the recursive flag was set handle it
		if(os.path.isdir(item) and recursive):
			# recursively handle that subdirectory
			renameDirectory("%s/%s" % (path, item), format, recursive=True)
		# single file
		else:
			# extract the file extension
			extension = os.path.splitext(item)[1]
			# check for supported extension and bandcamp name format
			if((str.lower(extension) in file_formats) and regex.match(item)):
				# rename the file
				renameSongFile("%s/%s" % (path, item), format=format, verbose=verbose)

# --------------------------------



# ################ #
# Argument Parsing #
# ################ #

formatHelp = """The Format to rename the file to. Format specifiers are: 
			
%%a - artist
%%A - album
%%t - songtitle
%%n - track number

"""

parser = argparse.ArgumentParser(description="Renames songs downloaded from bandcamp to a format you like", formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('path', help='Path to the directory containing the files or the file itself')
parser.add_argument('format', help=formatHelp)
parser.add_argument('-r', '--recursive', action='store_true', help="If set the program will go into sub directories and rename those files as well")
parser.add_argument('-v', '--verbose', action='store_true', help="If set the program will output messages to the command line")
arguments = parser.parse_args()


# ##################### #
# Argument verification #
# ##################### #

# get the absolute path
path = os.path.abspath(arguments.path)

# check if path is actually a path or a file
if(not os.path.isdir(path) and not os.path.isfile(path)):
	print "ERROR: '%s' is neither a file nor a directory" % path
	sys.exit()

# check if it is a full directory that has to be renamed
if(os.path.isdir(path)):	
	renameDirectory(path, arguments.format, recursive=arguments.recursive, verbose=arguments.verbose)

# check if it's only one file
elif(os.path.isfile(path)):
	renameSongFile(path, arguments.format, verbose=arguments.verbose)
