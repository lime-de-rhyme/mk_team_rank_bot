from discord.ext import commands
import settings
import team_rank_table

trt = team_rank_table.trt  # TEAM RANK TABLE. THIS IS A DICTIONARY.
DISCORD_TOKEN = settings.DISCORD_TOKEN

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="$")

@bot.command()
async def rank(ctx, team_name):
    for k, v in trt.items():
        for tn in v:
            if tn.lower() == team_name.lower():
                await ctx.channel.send(f"RANK: {k}")
                break
    await ctx.channel.send(f"{team_name} is not found.")
            
	
    
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
