#!/usr/bin/python3

import sys
import os
import discord
import logging
import json

async def sigcreate(args, channel):
	if len(args) != 2:
		await channel.send("ERREUR!\n" +
		"```d!sigcreate : Code erreur 1 : Nombre d'argument ne correspondant pas\n" + 
		"Rappel : d!sigcreate NomJeu NomSignal (sans espaces!)```")
		return
	if "@" in args[0] or "§" in args[0] or "@" in args[1] or "§" in args[1]:
		await channel.send("ERREUR!\n" + 
		"```d!sigcreate : Code erreur 2 : Caractères interdits\n" + 
		"Les caractères § et @ ne sont pas autorisés```")
	try:
		file = open("signals.txt", "r+")
		content = file.readlines()
		i = 0
		while i < len(content):
			if args[1] in content[i].split('§')[1]:
				await channel.send("ERREUR!\n" + 
				"```d!sigcreate : Code erreur 3 : Signal déjà créé```")
				return
			i = i + 1
	except FileNotFoundError:
		file = open("signals.txt", "w")
	file.write(args[0] + "§" + args[1] + "§\n")

async def sigadd(args, channel):
	if len(args) != 2:
		await channel.send("ERREUR!\n" +
		"```d!sigadd : Code erreur 1 : Nombre d'argument ne correspondant pas\n" + 
		"Rappel : d!sigadd NomSignal Mention (sans espaces!)```")
		return
	if not args[1].startswith("<@") or not args[1].endswith(">"):
		await channel.send("ERREUR!\n" + 
		"```d!sigadd : Code erreur 2 : Second argument n'est pas la mention d'un joueur```")
		return
	try:
		file = open("signals.txt", "r+")
		content = file.readlines()
		file.close()
		file = open("signals.txt", "w")
		i = 0
		while (i < len(content)):
			if args[0] in content[i]:
				file.write(content[i][:-1] + args[1] + "§\n")
				return
			else:
				file.write(content[i])
			i = i + 1
		await channel.send("ERREUR!\n" + 
		"```d!sigadd : Code erreur 3 : Partie non trouvée```")
	except FileNotFoundError:
		await channel.send("ERREUR!\n" + 
		"```d!sigadd : Code erreur 4 : Fichier manquant. Contactez le con qui m'a codé.```")
		return

async def sigsend(args, channel):
	if len(args) != 1:
		await channel.send("ERREUR!\n" + 
		"```d!sigsend : Code erreur 1 : Nombre d'argument ne correspondant pas\n" + 
		"Rappel : d!sigsend NomJeu```")
	try:
		file = open("signals.txt", "r")
		content = file.readlines()
		i = 0
		while (i < len(content)):
			if args[0] in content[i]:
				users = content[i].split('§')[2:]
				game = content[i].split('§')[0]
				i = 0
				message = "Hey "
				while (i < len(users) - 1):
					if i != 0 and i + 1 != len(users) - 1:
						message = message + ", "
					elif i + 1 == len(users) - 1:
						message = message + " et "
					message = message + users[i]
					i = i + 1
				await channel.send(message + ", vous êtes invités à jouer à " + game)
				return
			i = i + 1
		await channel.send("ERREUR!\n" + 
		"```d!sigadd : Code erreur 3 : Partie non trouvée```")
	except FileNotFoundError:
		await channel.send("ERREUR!\n" + 
		"```d!sigadd : Code erreur 4 : Fichier manquant. Contactez le con qui m'a codé.```")
		return