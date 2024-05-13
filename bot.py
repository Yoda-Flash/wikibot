import os
import wikipediaapi
import wikipedia
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client(intents=discord.Intents.default())
bot = discord.Bot()

wiki_wiki = wikipediaapi.Wikipedia("Discord Wikipedia Bot (WikiBot#0487)", "en")

wiki = bot.create_group("search", "Search Wikipedia for a result")
@bot.event
async def on_ready():
  print(f'{bot.user} has connected to Discord!')

def get_sections(sections, level=0):
  final_sections = ""
  for s in sections:
    final_sections += "%s: %s - %s" % ("*" * (level + 1), s.title, s.text[0:20])
  return final_sections

@wiki.command(description="Get the first ten sections from a wikipedia page")
async def get_ten_sections(ctx, search_topic: str):
  page = wiki_wiki.page(search_topic)
  if page.exists():
    if "may refer to" in page.summary:
      links = page.links
      links_with_keyword = []
      for link in links:
        if search_topic in link:
          links_with_keyword.append(link)

      await ctx.respond(f"Please use one of the following topics to try again! {links_with_keyword}")
    else:
      await ctx.respond(get_sections(page.sections[0:10]))
  else:
   await ctx.respond("Please try again with a different topic; page doesn't exist.")

@wiki.command(description="Returns information from a specific section of a topic, please use get_all_sections first")
async def return_section(ctx, search_topic: str, section_name: str):
  page = wiki_wiki.page(search_topic)
  await ctx.respond(page.section_by_title(section_name))
@wiki.command(description="Return a summary from wikipedia, if there are multiple options returns the first result")  # this decorator makes a slash command
async def first_result_summary(ctx, search_topic: str):  # a slash command will be created with the name "ping"
  # await ctx.respond(f"Pong! Latency is {bot.latency}")
  page = wiki_wiki.page(search_topic)
  if page.exists():
    if "may refer to" in page.summary:
      links = page.links
      links_with_keyword = []
      for link in links:
        if search_topic in link:
          links_with_keyword.append(link)

      page = wiki_wiki.page(links_with_keyword[0])
      print(page)
      await ctx.respond(page.summary[0:1999])
    else:
      await ctx.respond(page.summary[0:1999])
  else:
   await ctx.respond("Please try again with a different topic; page doesn't exist.")

@wiki.command(description="Return a summary from wikipedia, if there are multiple options returns a list of options")  # this decorator makes a slash command
async def list_summary(ctx, search_topic: str):  # a slash command will be created with the name "ping"
  # await ctx.respond(f"Pong! Latency is {bot.latency}")
  page = wiki_wiki.page(search_topic)
  if page.exists():
    if "may refer to" in page.summary:
      links = page.links
      links_with_keyword = "Please search again with one of the following: \n"
      for link in links:
        if search_topic in link:
          links_with_keyword += str(link)
          links_with_keyword += "\n"

      await ctx.respond(links_with_keyword)
    else:
      await ctx.respond(page.summary[0:1999])
  else:
   await ctx.respond("Please try again with a different topic; page doesn't exist.")

# client.run(TOKEN)
bot.run(TOKEN)
