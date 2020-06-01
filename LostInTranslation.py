from googletrans import Translator
from googletrans import LANGCODES as LangDict
import random

class ChainTranslator:

  
  def __init__(self,n):
    # generate translation chain
    # note the .__func__ to unwrap a static method when calling within the class
    self.__translationChain = generateTranslationChain.__func__(n)

    # use translation chain to generate list of translators
    self.__translatorList = generateTranslators.__func__(self.__translationChain)

  @property
  def translationChain(self):
      return self.__translationChain
  
  # No set and delete implemented as read only value
  #@translatorList.setter
  #def translatorList(self, value):
  #    self.__translationChain=value
  #@translatorList.deleter
  #def translatorList(self, value):
  #    print('Deleting..')
  #    del self.__translationChain

  @property
  def translatorList(self):
    return self.__translatorList

  def Translate(self,text):
    temp = text
    for i in range(len(self.__translatorList)):
      self.__translatorList[i].translate(temp)
      temp = self.__translatorList[i].translated.text
    return temp    

  def ShowAllTranslationSteps(self):
    print ("ORIGINAL Text: <translated %d times>" % len(self.__translatorList))
    print (self.__translatorList[0].translated.origin)
    for i in range(len(self.__translatorList)):
      print("%.3d: %s" % (i,self.__translatorList[i]))
      print(self.__translatorList[i].translated.text)

# Generates a list of n translations, book ending them with english
@staticmethod
def generateTranslationChain(n):
  # get generate n random languages
  li = ['english']
  li = li + random.sample(list(LangDict.keys()),n) + li
  return li

@staticmethod
def generateTranslators(li):
  translators = []
  for i in range(len(li)-1):
    # note, using the xTranslator inheritend class
    x = xTranslator(li[i],li[i+1])
    translators.append(x)
  return translators

# extension of google Translator class, stores source and destination language keys
class xTranslator(Translator):
  def __init__(self,source,target):
    super().__init__()
    self.__source = source
    self.__target = target
    self.__translated = ""

  @property
  def source(self):
    return self.__source

  @property
  def target(self):
    return self.__target

  @property
  def translated(self):
    return self.__translated

  # override of Translate()
  def translate(self, text):
    translate = super().translate(text,dest=self.__target,src=self.__source)
    self.__translated = translate
    return translate

  # printer friendly string why printing the class
  def __str__(self):
    x = self.__source + " -> " + self.__target
    return x