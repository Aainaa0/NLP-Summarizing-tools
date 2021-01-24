from flask import Flask
from flask import render_template
from flask import request
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from heapq import nlargest
import re

app = Flask(__name__)


#@app.route("/")
#def index():
#    return render_template("homepage.html")

@app.route("/", methods=['POST', 'GET'])
def home_en():
    summary = ""
    text = ""
    sentencesLength = "0"
    if request.method == "POST":
        text=request.form['originalText']
        text=re.sub('\[+(.*)+\]','', text)
        stopwords = list( STOP_WORDS )
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        #tokens = [token.text for token in doc]
        from string import punctuation
        punctuation = punctuation + '\n'
        print(punctuation)
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
        select_length = int(len(sentence_tokens)*0.3)
        sentencesLength = select_length
        print(sentencesLength)
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        
        print("Summary: \n"+summary)
        return render_template("homepage.html", summarizeText=summary, initialText=text, sentences = sentencesLength)
    
    else:
        return render_template("homepage.html")
        
    #some_text="Hello world!"
    #return render_template("homepage.html", summarizeText=summary, initialText=text)   
    #return summary

    
@app.route("/chinese", methods=['POST', 'GET'])
def home_zh():
    summary = ""
    text = ""
    sentencesLength = "0"
    if request.method == "POST":
        text=request.form['originalText']
        text=re.sub('\[+(.*)+\]','', text)
        stopwords = list( STOP_WORDS )
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        #tokens = [token.text for token in doc]
        from string import punctuation
        punctuation = punctuation + '\n'
        print(punctuation)
        word_frequencies = {}
        for word in doc:
            if word.text.lower() not in stopwords:
                if word.text.lower() not in punctuation:
                    if word.text not in word_frequencies.keys():
                        word_frequencies[word.text] = 1
                    else:
                        word_frequencies[word.text] += 1
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = word_frequencies[word]/max_frequency
        sentence_tokens = [sent for sent in doc.sents]
        sentence_scores = {}
        for sent in sentence_tokens:
            for word in sent:
                if word.text.lower() in word_frequencies.keys():
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word.text.lower()]
                    else:
                        sentence_scores[sent] += word_frequencies[word.text.lower()]
        select_length = int(len(sentence_tokens)*0.3)
        sentencesLength = select_length
        print(sentencesLength)
        summary = nlargest(select_length, sentence_scores, key = sentence_scores.get)
        final_summary = [word.text for word in summary]
        summary = ' '.join(final_summary)
        
        print("Summary: \n"+summary)
        return render_template("homepageC.html", summarizeText=summary, initialText=text, sentences = sentencesLength)
    
    else:
        return render_template("homepageC.html")   
    

if __name__ == "__main__":
    app.run()