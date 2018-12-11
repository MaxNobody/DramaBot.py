#!/usr/bin/python3

import sys
import os
import discord
import asyncio
import logging
import json

async def set_afk(args, author, channel):
	if len(args) < 1:
		await channel.send("ERREUR!\n" +
		"```d!afk : Code erreur 1 : Arguments insuffisants\n" + 
		"Rappel : d!afk <message>```")
		return
	try: 
		file = open("afks.txt", "r")
		content = file.readlines()
		i = 0
		while i < len(content):
			if author.mention in content[i].split('§')[0]:
				await channel.send("ERREUR!\n" + 
				"```d!afk : Code erreur 3 : Afk déjà créé\n" + 
				"Rappel : Pour enlever le mode afk, utilisez d!back```")
				return
			i = i + 1
	except FileNotFoundError:
		file = open("afks.txt", "w")
	file.close()
	file = open("afks.txt", "a")
	file.write(author.mention + "§" + ' '.join(args) + "\n")
	await channel.send("Vous êtes à présent considéré afk. Toute personne vous pingant verra le message " + ' '.join(args))

async def ping_afks(mentions, channel, author):
	i = 0
	try: 
		file = open("afks.txt", "r")
		afks = file.readlines()
	except FileNotFoundError: 
		await channel.send("ERREUR!\n" + 
		"Ping afk non trouvé. Merci de contacter l'idiot qui m'a programmé pour l'insulter de tout les noms.")
		return
	while i < len(mentions):
		print("BOUH")
		j = 0
		while j < len(afks):
			print("YAH Mentions[i].mention = " + mentions[i].mention + "afks[j].split('§')[0] = " + afks[j].split('§')[0])
			if mentions[i].mention in afks[j].split('§')[0]:
				await channel.send("Bonjour " + author.mention + ", " + afks[j].split('§')[0] + " est actuellent AFK.\n" + 
				"Il a laissé le message suivant : " + afks[j].split('§')[1])
				if (len(afks[j].split('§')) > 2):
					await channel.send("(btw il/elle est con.ne il/elle a mis un § dans son message d'afk du coup ya tout qui s'affiche pas... Pourtant c'est évident que j'ai été codé par un crétin qui allait pas tout afficher.)")
			j = j + 1
		i = i + 1