Hello!

I made the pyGollum python chatbot into a Discord bot!

In order to run the bot, you must get a Discord developer token:
1. Go to https://discordapp.com/developers/applications
2. Create a new application
3. On the left, click `bot`, then `create`
4. Copy client secret (don't tell this to anyone!)
5. Paste it into `Discord/token_manager.py`

Also, make sure that the channelid variable in `discord_main.py` is the correct channel ID!

To get a channel id, first go to `User Settings > Appearance > ADVANCED > Developer Mode` and make sure that's on.  Then, right-click the channel you want to use and say `Copy id`.  Paste this into `discord_main.py` instead of the default channelid.