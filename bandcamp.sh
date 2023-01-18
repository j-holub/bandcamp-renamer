#!/usr/bin/bash

# Author: Jay Oliver
# Date Created: 15/09/2022
# Date Last Modified: 15/09/2022
# Comments:
# This script should be run from the same directory as the stuff you wish to
# move to the music directory
#
# !!!!!!!!!!!!!!!!!!!!!!!!! NOTE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# the music and bandcamp program directories are hardcoded below. Set them
# as needed lest you stuff ends up in space or something.....

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

# ensure a '/' is NOT the last character pls
music_dir="/home/jo/Music" 
bc_dic="/home/jo/programs/mint/bandcamp-renamer"
band_al_sep=0
band=''
album=''
full_fname=${1%/*}

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

python3 "$bc_dic/bc_renamer.py" "$final_dir" "%n %t"
echo Everything should be good!
