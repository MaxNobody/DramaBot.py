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
			if author.name in content[i].split('§')[0]:
				await channel.send("ERREUR!\n" + 
				"```d!afk : Code erreur 3 : Afk déjà créé\n" + 
				"Rappel : Pour enlever le mode afk, utilisez d!back```")
			i = i + 1
	except FileNotFoundError:
		file = open("afks.txt", "w")
	file.close()
	file = open("afks.txt", "a")
	file.write("<@" + str(author.id) + ">§" + ' '.join(args))
	await channel.send("Vous êtes à présent considéré afk. Toute personne vous pingant verra le message " + ' '.join(args))