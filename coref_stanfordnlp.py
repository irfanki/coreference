from stanfordcorenlp import StanfordCoreNLP
from nltk import tokenize
import json


class StanfordNLP:

 def __init__(self, host='http://localhost', port=8080):
  self.nlp = StanfordCoreNLP(host, port=port,
  timeout=30000) # , quiet=False, logging_level=logging.DEBUG)

  self.props = {'annotators': 'coref', 'pipelineLanguage': 'en'}

 def coref(self, text):
  return json.loads(self.nlp.annotate(text, properties=self.props))


if __name__ == '__main__':
 sNLP = StanfordNLP()
 text = '''
 Just A Rather Very Intelligent System a.k.a JARVIS is created by Tony Stark natural-language and a
 sophisticated artificial intelligence user interface computer system, named after Edwin Jarvis. Though its primary duty is to automate Stark’s Malibu estate, the lifelike
 program fulfills many other needs for Stark, like being an information source for him, a diagnostic tool, a
 consultant and a voice of reason in Stark’s life. It was also responsible to provide security for Tony
 Stark's Mansion and Stark Tower. After creating the Mark II armor, Stark uploaded JARVIS into all of
 the Iron Man Armors, as well as allowing him to interact with the other Avengers, giving them valuable
 information during combat. JARVIS may be the one intellect Stark feels most comfortable opening up to.
 JARVIS can object to Stark’s commands if necessary. JARVIS speaks with a refined British accent, and
 is capable of back talk, sarcasm and condescension. During the Ultron Offensive, JARVIS was destroyed
 by Ultron, although his remaining programming codes unknowingly continued to thwart Ultron's plans of
 gaining access to nuclear missiles. His remains were found by Stark, who uploaded them into a synthetic
 body made of vibranium and, in conjunction with Ultron's personality and an Infinity Stone. JARVIS'
 duties were then taken over by FRIDAY.
 '''
 result = sNLP.coref(text)
 sent_list = tokenize.sent_tokenize(text)
 for num, mentions in result['corefs'].items():
  for mention in mentions:
   if mention['type'] == 'PRONOMINAL' and mention['animacy'] != 'INANIMATE':
    if not mention['isRepresentativeMention']:
     coref = '<' + mention['text'] + '>'
     print("Input:", sent_list[mention['sentNum'] -1].strip().replace(mention['text'], coref))
     print("Output:", mentions[0]['text'])
     print(" ", 'The' + coref + 'in the input refers to' + '<' + mentions[0]['text'] + '>' + 'entity')