#!/usr/bin/python3

import sys
import os
import discord
import asyncio
import logging

async def set_afk(args, author, channel):
	if len(args) < 1:
		await channel.send("ERREUR!\n" +
		"```d!afk : Code erreur 1 : Arguments insuffisants\n" + 
		"Rappel : d!afk <message>```", delete_after=10)
		return
	try: 
		file = open("afks.txt", "r")
		content = file.readlines()
		i = 0
		if "!" in author.mention:
			id = author.mention.split('!')[1][:-1]
		else:
			id = author.mention.split('@')[1][:-1]
		while i < len(content):
			if str(id) in content[i].split('§')[0]:
				await channel.send("ERREUR!\n" + 
				"```d!afk : Code erreur 3 : Afk déjà créé\n" + 
				"Rappel : Pour enlever le mode afk, utilisez d!back```", delete_after=10)
				return
			i = i + 1
	except FileNotFoundError:
		file = open("afks.txt", "w")
	file.close()
	file = open("afks.txt", "a")
	if "!" in author.mention:
		id = author.mention.split('!')[1][:-1]
	else:
		id = author.mention.split('@')[1][:-1]
	file.write(str(id) + "§" + ' '.join(args) + "\n")
	await channel.send("Vous êtes à présent considéré afk. Toute personne vous pingant verra le message " + ' '.join(args), delete_after=10)

async def ping_afks(mentions, channel, author):
	i = 0
	try: 
		file = open("afks.txt", "r")
		afks = file.readlines()
	except FileNotFoundError: 
		await channel.send("ERREUR!\n" + 
		"Ping afk non trouvé. Merci de contacter l'idiot qui m'a programmé pour l'insulter de tout les noms.", delete_after=10)
		return
	while i < len(mentions):
		j = 0
		while j < len(afks):
			if afks[j].split('§')[0] in mentions[i].mention:
				await channel.send("Bonjour " + author.mention + ", <@" + afks[j].split('§')[0] + "> est actuellent AFK.\n" + 
				"Il a laissé le message suivant : " + afks[j].split('§')[1], delete_after=10)
				if (len(afks[j].split('§')) > 2):
					await channel.send("(btw il/elle est con.ne il/elle a mis un § dans son message d'afk du coup ya pas tout qui s'affiche... Pourtant c'est évident que j'ai été codé par un crétin qui allait pas tout afficher.)", delete_after=10)
			j = j + 1
		i = i + 1

async def rem_afk(id, channel):
	try: 
		file = open("afks.txt", "r")
	except FileNotFoundError:
		await channel.send("ERREUR!\n" + 
		"```d!back : Code Erreur 1 : Fichier non trouvé, contactez le triple idiot qui m'a programmé. C'est vraiment un con.```", delete_after=10)
		return
	afks = file.readlines()
	file.close()
	file = open("afks.txt", "w")
	i = 0
	found = bool(False)
	while i < len(afks):
		if str(id) in afks[i].split('§')[0]:
			await channel.send("Bon retour à toi, <@" + str(id) + ">!", delete_after=10)
			found = bool(True)
		else:
			file.write(afks[i])
		i = i + 1
	if not found:
		await channel.send("ERREUR!\n" + 
		"```d!back : Code erreur 2 : Vous n'avez pas été trouvé dans le fichier. Etiez vous afk?```", delete_after=10)