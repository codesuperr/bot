#importer le module discord.py
import discord
from discord import *

from discord.utils import get
# ajouter un composant de discord.py
from discord.ext import commands

#cree le bot
bot = commands.Bot(command_prefix="!")
warnings = {}

#detecter quand le bot est pret("allume")
@bot.event

async def on_ready():
    print("bot prêt")
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("Je suis un bot"))

#detecter l'emoji python
@bot.event

async def on_raw_reaction_add(payload):
    emoji = payload.emoji.name
    canal = payload.channel_id
    message = payload.message_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")

    membre = bot.get_guild(payload.guild_id).get_member(payload.user_id)
    print(membre)
    print(message)

    if canal == 835161008829366322 and message == 835196970515431445 and emoji == "python":
        print("Grade ajouté !")
        await membre.add_roles(python_role)
        await membre.send("Tu obtiens le grade python !")

@bot.event
async def on_raw_reaction_add(payload):

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    print(message)
    id = payload.user_id
    guild = payload.guild_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    # verifier si l'emoji qu'on a ajoutée est "python"
    if canal == 835161008829366322 and message == 835196970515431445 and emoji == "python":
        await membre.add_roles(python_role)
        await membre.send("Tu obtiens le grade python !")









@bot.event
async def on_raw_reaction_remove(payload):

    emoji = payload.emoji.name  # recupere l'emoji
    canal = payload.channel_id  # recupere le numero du canal
    message = payload.message_id  # recupere le numero du message
    id = payload.user_id
    guild = payload.guild_id
    python_role = get(bot.get_guild(payload.guild_id).roles, name="python")
    membre = await bot.get_guild(payload.guild_id).fetch_member(payload.user_id)
    # verifier si l'emoji qu'on a ajoutée est "python"
    if canal == 835161008829366322 and message == 835196970515431445 and emoji == "python":
        await membre.remove_roles(python_role)
        await membre.send("Tu as perdu le grade python !")


#cree la command !regles

@bot.command()
async def regles(ctx):
    await ctx.send("Les regles sont :\n\tI - pas d'insultes\n\tII - pas de double compte\n\tIII - pas de spam")

#cree la command !bienvenu
@bot.command()
async def bienvenu(ctx, nouveau_membre : discord.Member):
    #recupere le pseudo
    pseudo = nouveau_membre.mention
    await ctx.send(f"Bienvenu à {pseudo} sur le serveur TestBotServer! N'esite pas a faire la commande '!regles'")
@bot.command()
@commands.has_role("president ultime")
async def warning(ctx, membre: discord.Member):

    pseudo = membre.mention
    id = membre.id

    # si la personne n'a pas de warning
    if id not in warnings:
        warnings[id] = 0
        print("Le membre n'a aucun avertissement")

    warnings[id] += 1
    await membre.send(f"vous avez eu un avertissement.\nvous avez eu {warnings[id]} avertssement / 3")

    print("ajoute l'avertissement", warnings[id], "/3")

    # verifier le nombre d'avertissements
    if warnings[id] == 3:
        # remet à les warnings
        warnings[id] = 0
        # message
        await membre.send("Vous avez été éjécté du serveur ! trop d'avertissements !")
        # ejecter la personne
        await membre.kick()


@bot.command()
@commands.has_role("president ultime")
async def betises(ctx, nouveau_membre : discord.Member):
    #recupere le pseudo
    pseudo = nouveau_membre.mention
    await ctx.send(f"tu fais des betises {pseudo} sur le serveur TestBotServer! fait !regles pour afficher les regles")



#verifier l'erreur
@bienvenu.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("vous devez obligatoirement entrer !bienvenu <@pseudo>")


@warning.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("vous devez obligatoirement entrer !warning <@pseudo>")

#donner le jeton pour qu'il se connecte
jeton = "ODM0Nzk1NjcwMDQ0NjcyMDQx.YIGGDQ.XmgAOXIp8jLN4-pCyJhdTNTomQQY"

#phrase
print("lancement du bot...")

#connecter au seveur
bot.run(jeton)

