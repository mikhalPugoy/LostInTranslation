from googletrans import Translator
from googletrans import LANGUAGES
import random
import LostInTranslation
debug = False

ss = LostInTranslation.ChainTranslator

x = Translator()
inputText = """Imagine there's no heaven
It's easy if you try
No hell below us
Above us only sky
Imagine all the people living for today
Imagine there's no countries
It isn't hard to do
Nothing to kill or die for
And no religion too
Imagine all the people living life in peace, you
You may say I'm a dreamer
But I'm not the only one
I hope some day you'll join us
And the world will be as one
"""
a = inputText
#y = x.translate('hello',dest='tl',src='en')

#print(y.text)
#print(y.src)

# get generate 10 random languages
zzz = ['en']
zzz = zzz + random.sample(list(LANGUAGES.keys()),5) + zzz

# debug flags print the stage by stage translation
if(debug):
  print ("Translating: ",end = "")
  for i in zzz:
    print('%s -> ' % LANGUAGES[i],end = "")
  print("")

for i in range(len(zzz)-1):
  if(debug):  print ("%d: %s to %s:" % (i,LANGUAGES[zzz[i]],LANGUAGES[zzz[i+1]]))
  y = x.translate(a,dest=zzz[i+1],src=zzz[i])
  if(debug):  print ("%d: %s -> %s" % (i, y.origin,y.text))
  a = y.text

print ("")
print ("")
print ("")

for i in zzz:
  print('%s -> ' % LANGUAGES[i],end = "")
print("")

print ("<<<ORIGINAL>>>")
print (inputText)
print ("<<<Lost In Translation>>>")
print (a)
#for z in LANGUAGES:
#  print(z)
#from flask import Flask
#app = Flask('app')

#@app.route('/')
#def hello_world():
#  return 'Hello, World!'
#
#app.run(host='0.0.0.0', port=8080)