import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    my_wiki = wikipedia.summary(name, length)
    return my_wiki


def search_wiki(name):
    results = wikipedia.search(name)
    return results


def phrase(name):
    page = wiki(name)
    blob = TextBlob(page)
    phrases = blob.noun_phrases
    return phrases
