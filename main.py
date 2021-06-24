from discord.ext import commands
import settings
import team_rank_table

trt = team_rank_table.trt  # TEAM RANK TABLE. THIS IS A DICTIONARY.
DISCORD_TOKEN = settings.DISCORD_TOKEN

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
bot = commands.Bot(command_prefix="$")

# when $rank hhi
def rank_of_HhI():
    HhI = ["HhI★", "HhI☆"]
    for hhi in HhI:
        for team_list in trt.values():
            for tl in team_list:
                if tl == hhi:
                    keys = [k for k, v in trt.items() if v == team_list]
                    HhI += keys   # HhI[2] = HhI★`s rank, HhI[3] = HhI☆'s rank
                    break
    return HhI[2], HhI[3]

@bot.command()
async def rank(ctx, team_name):
    for k, v in trt.items():
        for tn in v:
            if tn.lower() == team_name.lower():
                await ctx.channel.send(f"RANK: {k}")
                return
    if team_name.lower() == "hhi":
	black_star, white_star =  rank_of_HhI()
	await ctx.channel.send(f"{team_name} has two divisions.\nHhI★ is D rank, HhI☆ is G rank.")
	return
    else:
        await ctx.channel.send(f"{team_name} is not found.")
	return
            
	
    
# EXECUTES THE BOT WITH THE SPECIFIED TOKEN. TOKEN HAS BEEN REMOVED AND USED JUST AS AN EXAMPLE.
bot.run(DISCORD_TOKEN)
