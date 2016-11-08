import argparse
import os
import re
import sys

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
# 
# @return void 
def renameSongFile(path, format):

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

# -------------------------------


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
	# TODO rename folder
	print ("dir")

# check if it's only one file
elif(os.path.isfile(path)):
	# TODO rename file
	#print("file")
	renameSongFile(path, arguments.format)
