import requests
import discord
from discord import app_commands
from discord.ext import commands
import asyncio
from gamesearcher import Search

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.members = False

bot = commands.Bot(command_prefix="!", intents=intents)

search = Search()

@bot.tree.command(
    name="search",
    description="Search for a pirated game using gamestatus.info API."
)
@app_commands.describe(
    game="Game name",
)

async def search_command(interaction: discord.Interaction, game: str):
    await interaction.response.defer()
    try:


        game_info = search.search_game(game)

        if not game_info:
            await interaction.followup.send(f"No games found with name {game}")
            return
        embeds = []

        for info in game_info:
            embed = discord.Embed(title=info['title'], description=info['readable_status'])
            embed.set_thumbnail(url=info['short_image'])
            
            protections = ', '.join(eval(info['protections'])) if info['protections'] else 'None'
            hacked_groups = ', '.join(eval(info['hacked_groups'])) if info['hacked_groups'] else 'None'
            torrent_link = info['torrent_link'] if info['torrent_link'] else 'No torrent link available'

            embed.add_field(name="Protections", value=protections, inline=False)
            embed.add_field(name="Hacked Groups", value=hacked_groups, inline=False)
            embed.add_field(name="Torrent Link", value=torrent_link, inline=False)

            embeds.append(embed)

        for embed in embeds:
            await interaction.followup.send(embed=embed)

        
    except Exception as e:
        await interaction.followup.send(f"An error occurred: {e}")

# Place your bot token here, recommended to use .env file.
bot.run("YOUR_BOT_TOKEN")

# Example usage
# if __name__ == "__main__":
#   search = Search()
#    game_info = search.search_game("gasasasas")
#    if game_info:
#       print(game_info)
