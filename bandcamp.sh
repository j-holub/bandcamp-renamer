#!/usr/bin/bash

# Author: Jay Oliver
# Date Created: 15/09/2022
# Date Last Modified: 18/01/2023
# Comments:
# This script should be run from the same directory as the stuff you wish to
# move to the music directory; ideally in a 'Downloads' directory.
#
# !!!!!!!!!!!!!!!!!!!!!!!!! NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# the music and bandcamp script directories are hardcoded below. Set them
# as needed lest you stuff ends up in space or something.....


# Functions
#######################################################################
trim_space () {
    echo "${1}" | xargs
}

mk_if_not () {
    if [ ! -d "$1" ]
    then
        echo making band $1
        mkdir -p "$1"
    fi
}

# Variables
#######################################################################
# ensure a '/' is NOT the last character pls
music_dir="../Music" 
bc_dir="../bandcamp-renamer"
python_ver=python3

if [ ! -d $music_dir ]; then
    echo "The specified music directory $music_dir wasn't found."
    exit 1
fi

if [ ! -d $bc_dir ]; then
    echo "The specified python script directory $bc_dir wasn't found."
    exit 1
fi

# Script variables. You shouldn't need to change these.
band_al_sep=0
band=''
album=''
full_fname=${1%/*}

# Script
#######################################################################
if ! hash 7z 2>/dev/null; then
    echo "7zip is required for this script. Aborting."
    exit 1
fi

if ! hash $python_ver 2>/dev/null; then
    echo "Python is required for this script. Ensure it is installed and that"
    echo "the version provided above is one on your system."
    exit 1
fi

for i in $@
do
    if [ $i = '-' ]
    then
        band_al_sep=1
    else

        if [ $band_al_sep -eq 0 ]
        then
            band="$band"" ""$i"
        else
            album="$album"" ""$i"
        fi
    fi
done

album=${album%.*}  # remove file extension

band="$(trim_space "$band")"
album="$(trim_space "$album")"
final_dir="$music_dir/$band/$album/"

7z e -o"$final_dir" "$full_fname" 

$python_ver "$bc_dir/bc_renamer.py" "$final_dir" "%n %t"
