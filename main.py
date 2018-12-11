#!/usr/bin/python3

import sys
import os
import discord
import asyncio
import logging
import json

client = discord.Client()

@client.event
async def on_ready():
    print("Connected")

@client.event
async def on_message(message):
	if message.content.startswith("d!") and (message.author != client.user or message.content.startswith("d!afk")):
		print(message.content)
		from sigmanager import sigcreate, sigadd, sigsend
		command = message.content.split(" ")[0]
		command = command.split("!")[1]
		args = message.content.split(" ")[1:]
		if 'command' not in locals():
			print("Oops")
		elif command == "sigcreate":
			await sigcreate(args, message.channel)
		elif command == "sigadd": 
			await sigadd(args, message.channel)
		elif command == "sigsend":
			await sigsend(args, message.channel)
		elif command == "sigremove":
			print(command)
		elif command == "afk":
			print(command)
			#Marks user as afk and sends a message to everyone mentionning him
		elif command == "back":
			print(command)
			#Marks user as not-afk
		elif command == "roll":
			print(command)
			#Roll the dice noted.
		elif command == "lmgtfy":
			print(command)
			#Returns a lmgtfy query
		elif command == "google":
			print(command)
			#returns a google query
		elif command == "linksave":
			print(command)
			#saves a link to be retrieved later
		elif command == "link":
			print(command)
			#retrieves a link saved earlier
		elif command == "afkmeter":
			print(command)
			#Returns the afkmeter of the member or of argument summonner.
		elif command == "disconnect":
			await client.logout()
			await client.close()
	elif len(message.mentions) != 0:
		print("Il y a " + str(len(message.mentions)) + " mentions dans ce message")


client.run("NTIxNjI4NDI1NTEzOTkyMTky.Du_Qow.btsespRp5lO-CWaExP4mM6fgAJw")