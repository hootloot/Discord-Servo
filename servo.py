import discord
import pyautogui
from discord.ext import commands

client = discord.Client()
client = commands.Bot(command_prefix="=")
TOKEN = "Nzc4NjgyMDY5NTY3Nzk5NDA2.X7ViMA.iZsTmKnaLTY9m-YMeuWPizmTwqc"


@client.event
async def on_ready():
    game = discord.Game("with servos")
    await client.change_presence(status=discord.Status.online, activity=game)
    print("Bot is online!")



@client.command(name= "info")
async def info(ctx, member: discord.Member =None):
    embed = discord.Embed(color=0x7943df, timestamp=ctx.message.created_at, title="Commands")
    embed.set_footer(text=f"Whats good, {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="Instructions:", value="Use:```=servo```Then write the degree for the servo to move.", inline=False)
    embed.add_field(name="Do Not:", value="Choose a degree that is less than 10", inline=False)

    await ctx.send(embed=embed)


@client.command()
async def servo(message):
    await message.channel.send('```Write the degree```')
    msg = await client.wait_for('message')
    pyautogui.typewrite(str(msg.content))
    pyautogui.press("enter")
    await message.channel.send("```Servo Moved```")


client.run(TOKEN)