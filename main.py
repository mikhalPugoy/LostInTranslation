from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', var1="Enter Translation Here",var2="",var3='The Translator',var4 = "5")

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/', methods=['POST'])
def my_form_post():
    print("Post!")
    originalText = format(request.form['input'])
    n = int(format(request.form['times']))
    (translatedText,b) = testTranslate (originalText,n)
    
    return render_template('home.html', var1=originalText,var2=translatedText,var3=b,var4="5")


def testTranslate(text,n):
  from LostInTranslation import ChainTranslator

  trans = ChainTranslator(n)
  print ("Translation Chain:")
  y = translateChainString(trans.translationChain)
  print (translateChainString(trans.translationChain) , "\n")
  print ("Original:")
  print (text)
  print ("Lost In Translaton:")
  print (trans.Translate(text))
  
  return (trans.Translate(text),y)
  # Debug to see all steps, note intermediate steps stored in chain translator list of x translators
  #trans.ShowAllTranslationSteps()
  
def translateChainString(li):
  x = 'Translating from '
  for i in range(len(li)-1):
    x = x + li[i] + ' to '
  x = x + li[i+1]
  return x

if __name__ == "__main__":
  # dont run the main function, instead launch flask
  #testTranslate("testing",5)
  app.run(host='0.0.0.0', port=8080, debug=True)