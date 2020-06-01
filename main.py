def main():
  from LostInTranslation import ChainTranslator

  text = """It was all a dream, I used to read Word Up! magazine
Salt-n-Pepa and Heavy D up in the limousine
Hangin' pictures on my wall
Every Saturday Rap Attack, Mr. Magic, Marley Marl
I let my tape rock 'til my tape popped
Smokin' weed in Bambu, sippin' on Private Stock
Way back, when I had the red and black lumberjack
With the hat to match
Remember Rappin' Duke? Duh-ha, duh-ha
You never thought that hip-hop would take it this far
Now I'm in the limelight 'cause I rhyme tight
Time to get paid, blow up like the World Trade
Born sinner, the opposite of a winner
Remember when I used to eat sardines for dinner
Peace to Ron G, Brucie B, Kid Capri
Funkmaster Flex, Lovebug Starski
I'm blowin' up like you thought I would
Call the crib, same number, same hood
It's all good (It's all good)
And if you don't know, now you know, nigga
  """

  trans = ChainTranslator(5)
  print ("Translation Chain:")
  print (trans.translationChain , "\n")
  print ("Original:")
  print (text)
  print ("Lost In Translaton:")
  print (trans.Translate(text))
  
  # Debug to see all steps, note intermediate steps stored in chain translator list of x translators
  #trans.ShowAllTranslationSteps()
  

if __name__ == "__main__":
  main()