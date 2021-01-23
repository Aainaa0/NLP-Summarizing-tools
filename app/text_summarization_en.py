#!C:\Users\anist\anaconda3\python.exe
import cgi, os

text = """
The COVID-19 pandemic, also known as the coronavirus pandemic, is an ongoing pandemic of coronavirus disease 2019 (COVID-19) caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). It was first identified in December 2019 in Wuhan, China. The World Health Organization declared the outbreak a Public Health Emergency of International Concern in January 2020 and a pandemic in March 2020. As of 23 January 2021, more than 98.2 million cases have been confirmed, with more than 2.1 million deaths attributed to COVID-19, across 190 countries worldwide.
Symptoms of COVID-19 are highly variable, ranging from none to severe illness. The virus spreads mainly through the air when people are near each other.[b] It leaves an infected person as they breathe, cough, sneeze, or speak and enters another person via their mouth, nose, or eyes. It may also spread via contaminated surfaces. People remain infectious for up to two weeks, and can spread the virus even if they do not show symptoms.[9]
Recommended preventive measures include social distancing, wearing face masks in public, ventilation and air-filtering, hand washing, covering one's mouth when sneezing or coughing, disinfecting surfaces, and monitoring and self-isolation for people exposed or symptomatic. Several vaccines are being developed and distributed. Current treatments focus on addressing symptoms while work is underway to develop therapeutic drugs that inhibit the virus. Authorities worldwide have responded by implementing travel restrictions, lockdowns, workplace hazard controls, and facility closures. Many places have also worked to increase testing capacity and trace contacts of the infected.

"""

import re
text = re.sub('\[+(.*)+\]','', text)

import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation

stopwords = list( STOP_WORDS )

nlp = spacy.load('en_core_web_sm')

doc = nlp(text)

tokens = [token.text for token in doc]

punctuation = punctuation 
#punctuation

word_frequencies = {}
for word in doc:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text] = 1
            else:
                word_frequencies[word.text] += 1
#print(word_frequencies)  

max_frequency = max(word_frequencies.values())
#max_frequency

for word in word_frequencies.keys():
    word_frequencies[word] = word_frequencies[word]/max_frequency
#print(word_frequencies)

sentence_tokens = [sent for sent in doc.sents]
#print(sentence_tokens)

sentence_scores = {}
for sent in sentence_tokens:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            if sent not in sentence_scores.keys():
                sentence_scores[sent] = word_frequencies[word.text.lower()]
            else:
                sentence_scores[sent] += word_frequencies[word.text.lower()]
#sentence_scores

from heapq import nlargest

select_length = int(len(sentence_tokens)*0.3)
#select_length

summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)

# combine sentences together
final_summary = [word.text for word in summary]

summary = ' '.join(final_summary)

print("Summary: \n"+summary)

print("Length of original text: "+str(len(text)))
print("Length of summarized text: "+str(len(summary)))

# source: https://youtu.be/9PoKellNrBc





