import spacy
import neuralcoref

nlp = spacy.load('en_core_web_sm')
neuralcoref.add_to_pipe(nlp)

text_str = '''
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
doc = nlp(text_str)
# for ent in doc.ents:
# print(ent, ent._.coref_cluster)


# for token in doc:
#  if (token.pos_ == 'PRON' or token.dep_ == 'poss') and token._.in_coref:
#   for cluster in token._.coref_clusters:
#    print(token.text + " => " + cluster.main.text)

for sent in doc.sents:
    input_sent = []
    corefrences =[]
    for token in sent:
     input_sent.append(token.text)
     if (token.pos_ == 'PRON' or token.dep_ == 'poss') and token._.in_coref:
      for cluster in token._.coref_clusters:
       input_sent.pop()
       input_sent.append('<' + token.text + '>')
       # print(token.text + " => " + cluster.main.text)
       corefrences.append('The <' + token.text+'> in the input refers to <'+cluster.main.text+'> entity')
       break

    if corefrences:
     print('Input:', ' '.join(input_sent).strip('/n'))
     print('Output:')
     for corefrence in corefrences:
      print('       ', corefrence)




#Desired Output
# Input: Though <its> primary duty is to automate Stark’s Malibu estate
# Output: JARVIS, a sophisticated artificial intelligence created by Tony Stark
#           The <its> in the input refers to <JARVIS> entity

