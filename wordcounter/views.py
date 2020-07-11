from django.http import HttpResponse
from django.shortcuts import render
from operator import itemgetter
import re
def HomePage(request):
    return render(request, "home.html")

def counts(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddict = {}
    for word in wordlist:
        word = word.lower()
        match = re.match('^[-a-z-A-Z0-9]+$',word)
        if match:
            if word in worddict:
            #Increase
                worddict[word]+=1
            else:
            #add to dictionary
                worddict[word]=1

    sortedwords = sorted(worddict.items(), key = itemgetter(1), reverse=True)

    return render(request,"count.html", {'fulltext':fulltext, 'count':len(wordlist), 'sortedwords':sortedwords})

def about(request):
    return render(request, "about.html")
