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
# @param filename
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