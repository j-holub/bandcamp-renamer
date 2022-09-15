import re
import sys
import os
sys.path.insert(
    0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

test_names = [
    "174UDSI - Recollections - 25 Keys.mp3",
    "4EverfreeBrony - Recollections - 08 Not Much To Miss (feat. EileMonty).mp3",
    "AJ Young - Recollections - 43 Witchcraft & Wubbery.mp3",
    "AlicornAscension - Recollections - 32 Blue (feat. 4EverfreeBrony).mp3",
    "AnNy Tr3e - Recollections - 20 Into The Wild.mp3",
    "Arturo Höst & Ponderous Loop - Recollections - 39 Vardøger.mp3",
    "Aurelleah - Recollections - 27 On Wings Of Moonlight (feat. 1004Lights & Megan McDuffee).mp3",
    "bank pain - Recollections - 48 Ironsight Carousel.mp3",
    "BroniKoni - Recollections - 30 Keep The Beat Alive.mp3",
    "Budzy - Recollections - 18 Subconscious (PegasYs & Pinkie Rose Remix).mp3",
    "Budzy - Recollections - 24 Dimensions (feat. Lorris).mp3",
    "cover.png",
    "DJT & R3CTIFIER - Recollections - 37 Besties.mp3",
    "DJT - Recollections - 13 Waking Up Alone (feat. Metajoker).mp3",
    "Einarx - Recollections - 68 Guardian (Reprise).mp3",
    "eksoka - Recollections - 61 Advanced Magic.mp3",
    "EVRLST - Recollections - 14 Unaware (feat. PegasYs).mp3",
    "Exiark & Chi-Chi - Recollections - 38 Life Still Left In Me.mp3",
    "Exiark - Recollections - 02 Let There Be Light (feat. Chi-Chi).mp3",
    "ExplodingPonyToast, LutariFan & ThatMusicBrony - Recollections - 40 Start Again (IKX Remix).mp3",
    "Faulty - Recollections - 04 Vivo.mp3",
    "Filly In The Box - Recollections - 47 Still Blind (Sky Runner Remix).mp3",
    "Flittzy - Recollections - 31 What More Can I say.mp3",
    "Foozogz - Recollections - 06 New Journey.mp3",
    "Francis Vace - Recollections - 57 Cold Feet Pt. 2.mp3",
    "Frozen Night - Recollections - 11 Her Nightmare.mp3",
    "Hay Tea & Age Of Vinyl - Recollections - 46 Iridescence VIP.mp3",
    "Homage & TCB - Recollections - 16 It's Raining Now.mp3",
    "Hydra - Recollections - 60 Stratosphere.mp3",
    "iblank2apples - Recollections - 36 Flutterwander.mp3",
    "John Kenza - Recollections - 23 Celestial Dance VIP.mp3",
    "JoinedTheHerd - Recollections - 05 Memory Lane.mp3",
    "Jyc Row & Felicia Farerre - Recollections - 28 Night Queen VIP (feat. PrinceWhateverer).mp3",
    "L.M. - Recollections - 03 Together.mp3",
    "loophoof & NeverLastStanding - Recollections - 17 Have Here.mp3",
    "loophoof - Recollections - 58 Would Stay.mp3",
    "L-Train - Recollections - 09 My Monstrosity (feat. 4EverfreeBrony).mp3",
    "Mane In Green - Recollections - 29 Step! Buck! Leap! Touch!.mp3",
    "Mantlegen - Recollections - 67 Arf.mp3",
    "MEQA - Recollections - 51 Upshot.mp3",
    "Metajoker & GatoPaint - Recollections - 10 Better Off.mp3",
    "Midnight Musician - Recollections - 22 Where Is Your Heaven Now.mp3",
    "MrMehster - Recollections - 62 Spirit Animal.mp3",
    "Mufaya - Recollections - 72 Dark Ascension.mp3",
    "Nevermourn & RoomVR - Recollections - 45 Dawning Light.mp3",
    "Osoch - Recollections - 52 Stealer Of Magic (feat. Ponysphere & Chris Wöhrer).mp3",
    "Ponderous Loop, Arturo Höst, Quadrivia, Emily Koch & lia;quo - Recollections - 01 Journey Pt. 1.mp3",
    "PrinceWhateverer - Recollections - 07 Solidarity (In This Together).mp3",
    "Przewalski's Ponies - Recollections - 26 Just Tell Me....mp3",
    "Quadrivia & Arturo Höst - Recollections - 49 Ultimate Wolfpuncher.mp3",
    "Quicksilver - Recollections - 55 Malefactor.mp3",
    "Radiarc - Recollections - 12 Always There.mp3",
    "Replacer - Recollections - 34 Hello Commander.mp3",
    "Reverbrony - Recollections - 54 The Flightless Fury (feat. Razor Tongue).mp3",
    "Seventh Element - Recollections - 69 Shadows.mp3",
    "Silva Hound - Recollections - 19 Glimmer Time.mp3",
    "StealingShad3z - Recollections - 56 Changes (feat. GhostXb).mp3",
    "StrachAttack - Recollections - 42 Horizon.mp3",
    "Suskii & DJT - Recollections - 41 Spooky Ghost Buggos.mp3",
    "Synthis - Recollections - 15 Insane (feat. Sora).mp3",
    "Synthis - Recollections - 44 Insane (feat. Sora) -L.M. Remix-.mp3",
    "Syzy - Recollections - 65 Pots & Pans.mp3",
    "TCB - Recollections - 59 Only One (R3CTIFIER Remix).mp3",
    "The Wasteland Wailers - Recollections - 33 Fly Like You (feat. Brittany Church).mp3",
    "Totalspark - Recollections - 63 They're Coming.mp3",
    "TPressleyJ - Recollections - 66 Polar Opposition VIP.mp3",
    "Tripon - Recollections - 50 Hop, Skip & Jump Up.mp3",
    "UndreamedPanic & bank pain - Recollections - 35 Night Light (ThatMusicBrony Remix).mp3",
    "UndreamedPanic - Recollections - 21 Clear Skies VIP.mp3",
    "Velvet R. Wings & SDreamExplorerS - Recollections - 53 Withdrawn Tribes.mp3",
    "Wandering Artist - Recollections - 71 Train Bells.mp3",
    "Zephysonas - Recollections - 70 The Hour Of Twilight.mp3",
    "Zizkil - Recollections - 64 Crimson Elegance.mp3",
    "WRAITH - Speed Armageddon (Split w- Bastardizer) - 01 Speed Kills.mp3"
    ]

# "{artist name} - "
# "{album name} - "
# "{song num} {song name}
pattern = (r"(\w|\s|\d|\.|-|\&|,|\;|\')*\s-\s"
           r"(\w|\s|\d|\(|\)|\.|\&|,|\;|\'|\w*-)*\s-\s"
           r"\d\d\s(\w|\s|\d|\(|\)|\.|\&|,|\;|\'|\.\.\.)*")
regex = re.compile(pattern)

for file in test_names:
    if not regex.match(file):
        print(f"{file}")
