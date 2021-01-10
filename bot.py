import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import random

load_dotenv(".env.txt")
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix= '!')



@bot.event
async def on_ready():
      print(f'{bot.user.name} has connected to Discord!')
      



@bot.command(name= '42')
async def  the_old_forty_two(ctx):
      Hitchhiker_quotes = [ "Seven and a half million years and all you come up with is 42?",
                                     "Don\'t Panic"
                                     "Far out in the uncharted backwaters...",
                                     "I want a Pan Galactic Gargle Blaster." ,
                                     "The modern elevator has in much in common with an ancient elevator as the entire wing of the Sirius Cybernetics Marketing Division has in common with a packet of mixed nuts.",
                                     "That's just perfectly normal paranoia. Everyone in the universe has that.",
                                     "You'll have a national philosopher's strike on  your hands!",
                                     "The Hitchhiker's Guid the Galaxy defines the marketing division of the Sirius Cybenetics corporatoin as a bunch of mindless jerks who'll be the first against the wall when the revolution comes.",
                                     "The marketing divsion of the Sirius Cybernetics Corporation defines a robot as your plastic pal who's fun to be with!"]



  

    
    
      response = random.choice(Hitchhiker_quotes)
      await  ctx.send(response)
      return

@bot.command(name = "Steve_McRae")
async def Steve(ctx):
         
      await  ctx.send(f'Put that camera down! That\'s Squirrel Abuse!')
      return

@bot.command(name = 'POSW')
async def posw(ctx):
      Steve_quotes = [ 'You\'re stealing money from my daughter, Kyle!',
                                        'We don\'t do drama!',
                                        'I\'ve never faked a screenshot.',
                                        'I\'ve never said rocks are atheists!',
                                        'I\ve never engaged in rape apologetics!',
                                        'Black People do Coke',
                                        'Cheshire hase borderline psychopathic tendencies.',
                                        'I remember she told me that she was mentally ill.',
                                        'The worst mistake you can make is underestimating Cheshire.',
                                        'I live very frugally.',
                                        'I have zero disability rating from the VA.',
                                        'Kyle stole $60,000 from the fans.',
                                        'I don\'t get why people compare me to Donald Trump.',
                                        'She got my video taken down in the [Indiana], UK!' ]
     

            
      response = random.choice(Steve_quotes)
      await  ctx.send(response)
      return

 #===================================================
# And now for 62iq....
 #===================================================
@bot.command(name = '62iq')
async def  _62iq (ctx):
            Cheshire_quotes = [ "I\'m not convinced second hand smoke is a thing.",
                                            "I give my dog small amounts of chocolate.",
                                            "You can abort children up to 3 years old.",
                                            "He made me build roofs in minecraft it was hard.",
                                            "Sinister Porpoise wanted to debate me. [Note: She never did.]" ]

          

            response = random.choice(Cheshire_quotes)
            await  ctx.send(response)
            return
 

bot.run(TOKEN)

