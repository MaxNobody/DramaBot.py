#!/usr/bin/python3

import sys
import os
import discord
import asyncio
import logging
import random

async def roll(args, channel):
	if len(args) < 1:
		await channel.send("ERREUR!\n" + 
		"```d!roll : Code Erreur 1 : Nombre d'argument insuffisant" + 
		"Rappel : d!roll <nombre de dés>d<nombre de faces>[<+/-bonus>] avec différents dés séparés par des espaces\n" + 
		"Exemple : d!roll 3d5 5d100+15 8d10-8```", delete_after=20)
		return
	i = 0
	total = 0
	message = ""
	while i < len(args):
		bonus = 0
		rolls = 0
		faces = 0
		subtotal = 0
		if "d" not in args[i]:
			await channel.send("ERREUR!\n" + 
			"```d!roll : Code Erreur 2 : Un argument ne respecte pas le format!" + 
			"Rappel : d!roll <nombre de dés>d<nombre de faces>[<+/-bonus>] avec différents dés séparés par des espaces\n" + 
			"Exemple : d!roll 3d5 5d100+15 8d10-8```", delete_after=20)
			return
		if "+" in args[i] and not "-" in args[i]:
			bonus = int(args[i].split("+")[1])
			args[i] = args[i].split("+")[0]
		elif "-" in args[i] and not "+" in args[i]:
			bonus = int(args[i].split("-")[1]) * -1
			args[i] = args[i].split("-")[0]
		elif "+" in args[i] and "-" in args[i]:
			await channel.send("ERREUR!\n" + 
			"```d!roll : Code Erreur 3 : Vous ne pouvez pas ET ajouter ET soustraire```")
			return
		rolls = int(args[i].split("d")[0])
		faces = int(args[i].split("d")[1])
		j = 0
		message = message + "Lancer n°" + str(i) + " : "
		while (j < rolls):
			rand = random.randint(1, faces)
			subtotal = subtotal + rand
			message = message + str(rand)
			j = j + 1
			if (j < rolls):
				message = message + " "
		subtotal = subtotal + bonus
		total = total + subtotal
		message = message +  "\n"
		i = i + 1
	await channel.send(message)