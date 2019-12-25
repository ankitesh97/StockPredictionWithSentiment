

from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn
from nltk import sent_tokenize, word_tokenize, pos_tag
import pandas as pd

lemmatizer = WordNetLemmatizer()


def penn_to_wn(tag):

    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None


def clean_text(text):
    text = text.replace("<br />", " ")
    text = text.decode("utf-8")

    return text


def swn_polarity(text):

    text = clean_text(text)

    positive_sent = 0
    negative_sent = 0
    raw_sentences = sent_tokenize(text)
    for raw_sentence in raw_sentences:
        tagged_sentence = pos_tag(word_tokenize(raw_sentence))

        for word, tag in tagged_sentence:
            wn_tag = penn_to_wn(tag)
            if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV):
                continue

            lemma = lemmatizer.lemmatize(word, pos=wn_tag)
            if not lemma:
                continue

            synsets = wn.synsets(lemma, pos=wn_tag)
            if not synsets:
                continue

            synset = synsets[0]
            swn_synset = swn.senti_synset(synset.name())

            sentiment = swn_synset.pos_score() - swn_synset.neg_score()
            if sentiment>=0:
                positive_sent += sentiment
            else:
                negative_sent += sentiment

    return positive_sent,negative_sent

def readTweets():
    return list(pd.from_csv('data/tweets.csv'))


def main():
    #read tweets
    tweets = readTweets()
    data = []
    for tweet in tweets:
        pos,neg = swn_polarity(tweet[2])
        data.append([tweet[0],tweet[1],pos,neg])
    pd.DataFrame(data).to_csv('data/generated_scores.csv')



main()
