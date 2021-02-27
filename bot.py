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
      

@bot.command(name="helpme", help="Gives a list of commands.")
async def help(ctx):
      await ctx.send("!42 -- This supplies a random Hitchhiker\'s Guide to the Galaxy Quote.")
      await ctx.send ("!POSW -- This supplies a random quote from Internet shipwreck Steve McRae")
      await ctx.send ("!62iq -- This supplies one of three memorable bits of stupidity from the shipwreck\'s attack goblin.")
      await ctx.send ("!squirreljudge <question>.  Find out what the Squirrel Judge thinkgs you're guilty of.")
      await ctx.send ("!RedDwarf -- Get some wisdom about how not to be a smeghead from Red Dwarf.")


@bot.command(name= '42', help="Get a random Hitchhiker's Guide Quote")
async def  the_old_forty_two(ctx):
      Hitchhiker_quotes = [ "Seven and a half million years and all you come up with is 42?",
                                     "Don\'t Panic",
                                     "Far out in the uncharted backwaters...",
                                     "I want a Pan Galactic Gargle Blaster." ,
                                     "The modern elevator has in much in common with an ancient elevator as the entire wing of the Sirius Cybernetics Marketing Division has in common with a packet of mixed nuts.",
                                     "That's just perfectly normal paranoia. Everyone in the universe has that.",
                                     "You'll have a national philosopher's strike on  your hands!",
                                     "The Hitchhiker's Guide the Galaxy defines the marketing division of the Sirius Cybenetics corporatoin as a bunch of mindless jerks who'll be the first against the wall when the revolution comes.",
                                     "The marketing divsion of the Sirius Cybernetics Corporation defines a robot as your plastic pal who's fun to be with!",
                                     "The Vogon Constructor ships hung in the sky in much the same way that bricks don\'t",
                                      "It has been said the Vogons are not above bribery and corruption in the same way that the sea is not above the clouds.",
                                      "This planet has or rather had a problem. The problem was that most of the people  on it [even those with digital watches] were unhappy.",
                                      "Although the parking lot was nearly empty, Ford nevertheless weaved his way through it.",
                                      "So long and thanks for all the fish!",
                                      "The Vogon Constructor Ships hung in the sky in much the same way that bricks don\'t",
                                      "\"Myself? I'd trust him until the end of the world,\" said Ford. \How long away is that?\" replied Arthur. \"About 12 minutes.\"",
                                      "What do you mean you've never visited Alpha Centauri? For heaven\'s sake mankind. It\'s only four light years away."]
      



  
      response = random.choice(Hitchhiker_quotes)
      await  ctx.send(response)
      return

@bot.command(name = "Steve_McRae", help="Well, the squirrels are worried about being equated with Steve Mcrae.")
async def Steve(ctx):
         
      await  ctx.send(f'Put that camera down! That\'s Squirrel Abuse!')
      return

@bot.command(name = 'POSW', help="Get a random bit of Wisdom from Petty Officer ShipWreck Steve McRae")
async def posw(ctx):
      Steve_quotes = [ 'You\'re stealing money from my daughter, Kyle!',
                                        'We don\'t do drama!',
                                        'I\'ve never faked a screenshot.',
                                        'I\'ve never said rocks are atheists!',
                                        'I\'ve never engaged in rape apologetics!',
                                        'Black People do Coke',
                                        'Cheshire has borderline psychopathic tendencies.',
                                        'I remember she told me that she was mentally ill.',
                                        'The worst mistake you can make is underestimating Cheshire.',
                                        'I live very frugally.',
                                        'I have zero disability rating from the VA.',
                                        'Kyle stole $60,000 from the fans.',
                                        'I don\'t get why people compare me to Donald Trump.',
                                        'She got my video taken down in the [Indiana] UK!',
                                        'If you think I\'ve said someone is dumb, you\'re stupid',
                                        '.9999999999..... = 1',
                                        'I\'m astronomically honest.',
                                        'I never lie.',
                                        'I\'ve never had a restraining order.',
                                        'I have the equivalent of a PhD [from the Navy\'s Nuke School]',
                                        'How dare you bring my daughter into this?',
                                        'Kyle is going to gel.',
                                        'We only respond to evidence not accusations.',
                                        '100% sure Nate Broady is Kyles lawyer.',
                                        'I am unleashed.',
                                        'That\'s  how it\'s used in philosophy.',
                                        'Have you read Draper?',
                                        'I talk to PhDs',
                                        'I have never been part of any teen mom group!',
                                        'It\'s not a troll group. It\'s the opposite of a troll group.',
                                        'You\'re inept in philosophy.',
                                        'I am exceptionally clear and it is quite unreasonble to make what is normative and understood by anyone who is competent enough to discuss any of this require such unreasonable explicistness.',
                                        'I have never once had any philosopher say I use dishonest rhetorical tacics. NEVER ONE.']
     

            
      response = random.choice(Steve_quotes)
      await  ctx.send(response)
      return

 #===================================================
# And now for 62iq....
 #===================================================
@bot.command(name = '62iq',help='Quotes from a Low IQ Trash Goblin.')
async def  _62iq (ctx):
            Cheshire_quotes = [ "I\'m not convinced second hand smoke is a thing.",
                                            "I give my dog small amounts of chocolate.",
                                            "You can abort children up to 3 years old.",
                                            "Not all dogs are allergic to chocolate.",
                                            "He made me build roofs in minecraft. It was hard.",
                                            "Sinister Porpoise wanted to debate me. [Note: The Sinister Porpoise did *not* want to debate her.]" ]

          

            response = random.choice(Cheshire_quotes)
            await  ctx.send(response)
            return

@bot.command(name = 'nut', help="Give a Squirrel a Nut.")
async def nut(ctx):
              await ctx.send('Yes, please! May I have another?')
              return


@bot.command(name="RedDwarf", help="Get a Red Dwarf quote.")
async def RedDwarf(ctx):
      redDwarfQuotes = [ "Now kindly kluck off before I extract your giblet and shove a large seasoned onion between the lips you never kiss with.",
                                     "Call it extreme if you like, but I propose we hit it hard and hit it fast with a major - and I mean major - leaflet campaign.",
                                     "I\'ve been so worried. I haven\'t buffed my shoes in two days.",
                                     "I\'ve seen Westerns. I know how to speak cowboy. Dry white wine and Perrier, please.",
                                     "I tell you one thing. I\'ve been to a parallel universe. I've seen time running backwards. I\'ve playe pool with planets, and I\'ve given birth to twins, but I never thought in my entire life I\'d taste an edible Pot Noodle.",
                                     "It\'s better to have loved and lost than to listen to an album by Olivia Newton-John.",
                                     "[Reading Hitler's Diary] Things to do: Stop milk, pay papers, invade Czechoslovakia!",
                                     "I knew I was lying. No silicon heaven? Perposterous! Where would all the calculators go?",
                                     "Has anyone ever told you that the configuration and juxtaposition of your features is extraordinarily apposite?",
                                    "Of course, lager! The only thing that can kill a vindaloo!",
                                     "How come you need more memory? Over the hyears you\'ve had more RAM than a field of sheep!",
                                     "There's only three alternatives: it thinks we're either a threat, food or a mate.... It\'s either gonna kill us, eat us or hump us. Either we persuade him we're not that kinda oceanic salvage vessel, or we scarper pronto.",
                                     "Let\'s at least ask someone who's at least going to give us a slightly more intelligent opinion. Hello, wall! What do you think?",
                                     "I\'m so gorgeous, there\'s a six month waiting list for birds to suddenly appear every time I am near!",
                                     "Last time we met I was wearing a cute little black number with peach trim and gold spangles, and although it looks like I\'m wearing the same outfit today, it is in fact an entirely different cute little black number, with completely different gold spangles!",
                                     "Your nickname was never Ace. Maybe Ace Hole. ",
                                     "I am Holly the ship\'s computer with an IQ of 6000. The same IQ as 6000 PE teachers",
                                     "David Lister, Technician, 3rd class. Captain\'s remarks: \"Has requested sick leave due to diarrhea on no less than 500 occasions. Left his previous job as a supermarket trolley attendant after ten years because he didn\'t want to get tied down to a career. Promotion prospects: zero.",
                                     "Arnold Rimmer, Technician, 2nd Class. Captain's remarks: \"There's a saying amongst the officers: If a job\'s worth doing, it\'s worth doing well. If it\'s not worth doing, give it to Rimmer. Promotion prospects: comical." ,
                                     "The aforementioned Rimmer, to whit, me, attended inspection parade. He was totally naked except for a pair of mock-leather driving gloves and some blue swimming goggles. Under the influence of this psychedelic breakfast he went on to attack two senior officers, believing them to be giraffes who were armed and dangerous.",
                                     "I was in love once. A Sinclair ZX81. People said, no, Holly, she\'s not for you. She\'s cheap, she\'s stupid and she wouldn\'t load, well, not for me anyway.",
                                     "Well, the thing about a black hole - its main distinguishing feature - is it\'s black. And the thing about space, the colour of space, your basic space colour, is black. So how are you supposed to see them.",
                                     "Pub. Ah, yes: a meeting place where people attempt to achieve advanced states of mental incompetence by the repeated consumption of fermented vegetable drinks.",
                                     "I haven't been this embarrassed since I was loosening my adjustment screws, and my entire groinal box dropped into Mr Rimmer's soup.",
                                     "How did I end up like this, on a ship where the fourth most popular pastime is going down to the laundry room and watching my knickers spin dry?",
                                     "Christian rock music. If that doesn\'t scare her off, nothing will.",
                                     "You once spent an afternoon on the Samaritans switchboard and four people committed suicide. Your middle name is Judas but you tell everyone that it's Jonathan. You sign all your official letters 'Arnold Rimmer BSc' and the BSc stands for 'Bronze Swimming Certificate'. You\'re a cheating, weasley, low-life scumbucket with all the charm and social grace of a pubic louse.",
                                     "Kryten, kindly get to the point before I jam your nose between your cheeks and make it the filling of a buttock sandwich.",
                                     "Get real man. Most eunuchs have got more balls than you.",
                                     "Rimmer, real dumplings, proper dumplings when they are properly cooked to perfection, proper dumplings should not bounce!" ]

      response = random.choice(redDwarfQuotes)
      await ctx.send (response)
                                     
#===============================================================================================================
# And now we are putting in the Squirrel of Judgment so he can decide what you're guilty of.
#===============================================================================================================
@bot.command(name = "squirreljudge", help="Get judged by the Squirrel of Judgment.")
async def judge(ctx):

      judgments = [ "Guilty",
                           "Not guilty.",
                           "Not guilty by reason of mental disease or defect.",
                           "You're gulty of crimes agaisnt squirrel kind, porpoise.",
                           "Guilty of High Treason.",
                           "Guilty of starving squirrels by keeping them from their bird feeder."]

      
      response = random.choice(judgments)
      await ctx.send (response)
                                     
                                     
                                     
                                     
                                     
                                          
      return

@bot.command (name = "8ball", help = "Ask the Eight Ball a question.")
async def _8ball(ctx):
      
      choices = [ "yes", "no", "Ask again", "Hard to See", "Ok, Boomer!", "Difficult to Tell.", "Most Definitely", "Maybe.", "Ask the Squirrel of Judgment."]
      response = random.choice(choices)
      await ctx.send (response)

      return;

bot.run(TOKEN)

