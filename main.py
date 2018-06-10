import discord
import asyncio
import random


client = discord.Client()

COR =0x10EA67
ROSA =0xff6347
VERDE =0xB9FF00
msg_id = None
msg_user = None




@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo')
    print(client.user.name)
    print(client.user.id)
    print('-------Pscodium---------')




@client.event
async def on_message(message):
    await client.change_presence(game=discord.Game(name='my game'))



    if message.content.upper().startswith(';;PING'):
        userID = message.author.id
        await client.send_message(message.channel, "<@%s> Pong!" % (userID))





    if message.content.startswith(';;entrar'):
      try:
        canal = message.author.voice.voice_channel
        await client.join_voice_channel(canal)
      except discord.errors.InvalidArgument:
             await client.send_message(message.channel, "Você precisa esta conectado a um canal de voz!")

    if message.content.startswith(';;sair'):
      try:
        canaldevoz = client.voice_client_in(message.server)
        await canaldevoz.disconnect()
      except AttributeError:
          await client.send_message(message.channel,"O bot não esta conectado em nenhum canal de voz!")







    if message.content.lower().startswith(';;moeda'):
        choice = random.randint(1,2)
        if choice == 1:
            await client.add_reaction(message, '😀')
        if choice == 2:
            await client.add_reaction(message, '👑')




    if message.content.lower().startswith(';;ola'):
        await client.send_message(message.channel, "Olá rapaziada, tudo bom?")



    if message.content.lower().startswith(";;elo"):
     texto =discord.Embed(
        title="Escolha seu Elo e sua Lane",
        color=COR,
        description="- Unranked = ❌      - Top = 🗡\n"
                    "- Bronze = 🗑        - Jungle = ⚡\n"
                    "- Prata = ⚔         - Mid = 🔊\n"
                    "- Ouro = 💰          - Adc = 🔫\n"
                    "- Diamante = 💎      - Sup = ❤\n"
                    "- Desafiador = 📐",)

    botmsg = await client.send_message(message.channel, embed=texto)


    await client.add_reaction(botmsg, "❌")
    await client.add_reaction(botmsg, "🗑")
    await client.add_reaction(botmsg, "⚔")
    await client.add_reaction(botmsg, "💰")
    await client.add_reaction(botmsg, "💎")
    await client.add_reaction(botmsg, "📐")
    await client.add_reaction(botmsg, "🗡")
    await client.add_reaction(botmsg, "⚡")
    await client.add_reaction(botmsg, "🔊")
    await client.add_reaction(botmsg, "🔫")
    await client.add_reaction(botmsg, "❤")


    global msg_id
    msg_id = botmsg.id

    global msg_user
    msg_user = message.author

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message

    if reaction.emoji == "❌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Unranked", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🗑" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚔" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "💰" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "💎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "📐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Desafiador", msg.server.roles)
     await client.add_roles(user, role)
     print("add")


    if reaction.emoji == "🗡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Top", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Jungle", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔊" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Mid", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "🔫" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Adc", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

    if reaction.emoji == "❤" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Sup", msg.server.roles)
     await client.add_roles(user, role)
     print("add")

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message

    if reaction.emoji == "❌" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Unranked", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🗑" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Bronze", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚔" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Prata", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "💰" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Ouro", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "💎" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Diamante", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "📐" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Desafiador", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🗡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Top", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "⚡" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Jungle", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔊" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Mid", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "🔫" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Adc", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove")

    if reaction.emoji == "❤" and msg.id == msg_id: #and user == msg_user:
     role = discord.utils.find(lambda r: r.name == "Sup", msg.server.roles)
     await client.remove_roles(user, role)
     print("remove");




@client.event
async def on_member_join(member):
  canal = client.get_channel("450854682206666752")
  regras = client.get_channel("447798289312514071")
  msg = "Bem Vindo ao Servidor __***The After***__ {}\n leia as {}".format(member.mention, regras.mention)
  await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro

@client.event
async def on_member_remove(member):
   canal = client.get_channel("450851199353225226")
   msg = "Adeus Meu Jovem {}".format(member.mention)
   await client.send_message(member, msg) #substitua canal por member para enviar a msg no DM do membro


client.run('NDUwNjkwMTkxMDQxMTAxODU5.De5M-g.E6FeZLIi4ENEaEPbPM3lzoCgDw8')
