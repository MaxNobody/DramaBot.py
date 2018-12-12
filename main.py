#!/usr/bin/python3

import sys
import os
import discord
import asyncio
import logging

client = discord.Client()

@client.event
async def on_ready():
    print("Popcorn is ready")

@client.event
async def on_message(message):
	if message.content.startswith("d!") and (message.author != client.user or message.content.startswith("d!afk")):
		print(message.content)
		from sigmanager import sigcreate, sigadd, sigsend
		from afk import set_afk, rem_afk
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
			await set_afk(args, message.author, message.channel)
		elif command == "back":
			await rem_afk(message.author.id, message.channel)
		elif command == "roll":
			roll(args, message.channel)
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
		await message.delete()
	elif len(message.mentions) != 0 and message.author != client.user:
		from afk import ping_afks
		await ping_afks(message.mentions, message.channel, message.author)
	

if __name__ == '__main__':
    fd = open("private/token")
    client.run(fd.readlines()[0])
    fd.close()