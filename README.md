# LMN3-Drum-Kit-Mapper
Built for the LMN3, an open source DAW-in-a-box, this creates a simple GUI to map drum kit sounds to keys

## Prerequisites
This is python script is to be run on the Raspberry Pi that is running your DAW.  It assumes you have already copied your drum kit directory to the `/home/pi/.config/LMn-3/drum_kit` directory.

The python script requires tkinter. To install tkinter, open a terminal and type `sudo apt-get install python3-tk`

## Install and Run
Download the script and run it in a terminal with, `python drumkit_yaml_GUI.py`

You will be presented with a piano looking GUI.  Clicking on each key will open a file browser where you can set/select a sound file to that specific key.

When you are done assigning keys, click on the yellow "Make YAML."  You'll be prompted to enter the name of the drum_kit directory and lastly whether you'd like the YAML file copied thereto.



