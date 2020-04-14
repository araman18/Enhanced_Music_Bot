
# Enhanced_Music_Bot
Discord bot for playing modified music in discord servers, made with discord.py rewrite

This bot is has the functionality of a normal music bot, with play, queue, stop, resume, pause etc but is also able to play modified versions of tracks on spotify and youtube 
Calling .play <Song Name/Url> bass will bass boost the song then play it
Calling .play <Song Name/Url> nc will put the song through a nightcore filter then play it
Calling .play <Song Name/Url> will play the song normally

Libraries used are specified in requirments.txt

## Instructions

Dependencies include modules in requirments.txt as well as FFmpeg, can be installed by choco on windows.

In order to run the bot in your own server follow the following steps

1.)Change the server name/guild name to the name of your 

2.)Use https://discordapp.com/oauth2/authorize?client_id=CLIENT_ID_HERE&scope=bot to add the bot to your server

3.)To run the bot first use the command below to install dependancies
<p> pip install -r requirements.txt pip install -r requirements.txt<p>
  
4.)Install FFmpeg if not already installed

5.) run "python main.py" to start running the bot



