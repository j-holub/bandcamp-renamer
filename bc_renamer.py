import argparse
import os
import re
import sys

# ###### #
# Config #
# ###### #

# formats that can be downloaded from bandcamp
file_formats = ['.mp3', '.flac', '.aac', '.ogg', '.oga', '.m4a', '.CAF', '.wav', '.aiff', '.aif', '.aifc']


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

# Takes the absolute path to a directory containing the song files
# If these files match one of the extensions specified in 'file_formats'
# these files are renamed
# 
# @param path - absolute path to the directory containing the files
# @param format - format that the file should be renamed to
#
# @return void
def renameDirectory(path, format):

	# list all the files in the directory
	list_of_files = os.listdir(path)

	# iterate through everything found
	for entry in list_of_files:

		# check if the extension is supported
		extension = os.path.splitext(entry)[1]
		if(str.lower(extension) in file_formats):
			# rename the file
			renameSongFile("%s/%s" % (path, entry), format)

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
	renameDirectory(path, arguments.format)

# check if it's only one file
elif(os.path.isfile(path)):
	renameSongFile(path, arguments.format)
