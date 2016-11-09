# Bandcamp Renamer

So you have bought an album or a whole discography on [bandcamp](http://bandcamp.com). But the files downloaded have these really long name and overall just don't fit into your digital music collection.

With **bandcamp renamer** you can rename these files to any format you wish, with just one simple command line call.

## Usage

The command line synthax is very simple

```
bcrn <file or directory> <format> [options]
```

You can rename just a *single file* or a *whole directory* (with subdirectories if specified). The script will detect it by itself.

The script will only touch files that match the format of the **bandcamp** file naming and end in the file extensions provided by **bandcamp** (Mp3, FLAC, ACC, Ogg Vortis, ALAC, WAV, AIFF).


### Format

With the format string you can specifiy into what format the files should be renamed to.

Below are some key specifiers you can use. They will use the information from the original file name.

| Specifier |    Meaning   |
|:---------:|:------------:|
|     %a    |  artist name |
|     %A    |  album title |
|     %n    | track number |
|     %t    |  song title  |

Examples are `%n - %t`, `%a - %n: %t` and `%n: %t`. 

### Options

The following options can be used to alter the scripts behaviour

|    Option   | Short Version |                          Meaning                         |
|:-----------:|:-------------:|:--------------------------------------------------------:|
|    --copy   |       -c      | Copies the files instead of simply renaming them         |
| --recursive |       -r      | Files located in subdirectories will be renamed as well  |
|  --verbose  |       -v      | Messages for the renaming are output to the command line |



## Examples

### Single File

```
bcrn "Artist - Album - 01 Awesome Song.mp3" "%n - %t"
```

This will rename the file to `01 - Awesome Song.mp3`.

### Whole Directory/Album

```
bcrn "Great Album" "%n_%t_(%A)"
```

This will rename all the song files inside the `Great Album` directory to `TrackNumber_SongTitle_(Great Album).mp3`.

### With Subdirectories (Discography)

Sometimes you download the whole discography of an artist and want  to rename them all at once. At these times the `recursive flag` comes in handy.

```
bcrn "Artist Discography Folder" "%a - %n: %t" -r
```

This will rename all fildes within `Artist Discography Folder` and **all** its subdirectories (usually the albums) to `ArtistName - TrackNumber: SongTitle`.

## Install

**Download** this repositories using the button to the top right or simply **clone** the repository.

```
git clone https://github.com/00SteinsGate00/bandcamp-renamer.git
```

To install the script copy it to somewhere within your `$PATH`, for example `/usr/bin` and give it the correct permissions.

From within the project's directory run

```
sudo cp bc_renamer.py /usr/bin/bcrn
sudo chmod +x /usr/bin/bcrn
```

## Licence

[MIT Licence](LICENCE.md)