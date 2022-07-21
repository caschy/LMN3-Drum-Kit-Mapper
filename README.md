# LMN3-Drum-Kit-Mapper
Built for the LMN3, an open source DAW-in-a-box, this creates a simple GUI to map drum kit sounds to keys

## Prerequisites
This is python script can be run on any machine where you want to create a folder of drum kit sounds and associated YAML file.  The YAML file is what this script creates and defines the mapping of MIDI keys to sound files.

The python script requires tkinter. To install tkinter, open a terminal and type `sudo apt-get install python3-tk`

## Install and Run
Download the script and ico.ico (icon file)

Run the script in a terminal with, `python drumkit_yaml_GUI.py`

You will be presented with a piano looking GUI.  Clicking on each key will open a file browser where you can set/select a sound file to that specific key.

When you are done assigning keys, click on the yellow "Make YAML."  You'll be prompted to enter the name of the drum kit and lastly where to save the YAML file.

If all went well, you'll be left with a YAML file named by your previous input.



