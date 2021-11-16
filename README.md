# cr-exp-plotter
Plot all of your friends Clash Royale experience in a graph that evolves over time.

## How does it work?
This bot will create a graph showing all your friend's current XP in Clash Royale. Every day it will send a new updated graph to a Discord channel using a webhook.

## Screenshot
![image](https://user-images.githubusercontent.com/60482551/142044106-a48845d0-0245-434a-9dca-19cabaa5559c.png)

## How do I set this up?
- Download the files [here](https://github.com/thomaskeig/cr-exp-plotter/archive/refs/heads/main.zip) and unzip the folder.
- Open up command prompt (or command line if you're using linux) in the directory of all the files and install the required packages. You can do this by using the command `pip install -r requirements.txt` on Windows and `sudo pip install -r requirements.txt` on Linux.
- Set up your accounts to track, to learn how to do this, read [this](https://github.com/thomaskeig/cr-exp-plotter#how-to-add-players) section below.
- Create a Discord webhook, search it up if you're unsure how to do this.
- Open `settings.yml` and change the settings to how you like them.
- Run the bot by opening up command promt in the folder that `main.py` is located in and type `python main.py`.
- When it reaches the time you chose in the settings your updated graph will be shown in you Discord channel.

## How to add players
- Open cache/data.json file in your favourite editor
- Edit the file to contain every player you want to track, it is recommended that you don't track more than 5 players, as the graph will look a bit messy, however there is no limit that the program will take.
  - Copy this part of the file underneath itself enough times until you have your desired player count. (Dont forget the ",". \![image](https://user-images.githubusercontent.com/60482551/142044002-35ab9177-f268-47d1-8ca5-9dd9c197f973.png)
  - Edit the player tag for each player, there is no error checking for this so make sure you get it right! You can find how how to find a player tag by using [this](https://www.youtube.com/watch?v=A1FWTjBw73k) video
  - Edit the player name for each player, this does not have to be the same is their in-game name, it is the name that will be shown on the graph.
  - The "xp" and "dates" list should be left empty. The program will fill these in appropriately.
  - It is advised that you copy the entire new file contents into [this](https://jsonlint.com/) website to check is is valid JSON
  - If you have any issues please create a new issue [here](https://github.com/thomaskeig/cr-exp-plotter/issues) and I'll reply asap!


## YouTube Tutorials
If you make a YouTube tutorial on how to set this up, message me on Twitter at @thomaskeig_ and I'll leave a link here!
