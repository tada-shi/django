from django.shortcuts import render,redirect
from PyDictionary import PyDictionary

# Create your views here.
def index(request):
    return render(request, 'dictionary.htm')

def search(request):
    value = request.GET.get('text')
    dictionary = PyDictionary()
    meaning = dictionary.meaning(value)
    antonyms = dictionary.antonym(value)
    synonyms = dictionary.synonym(value)
    context = {
        'meaning' : meaning,
        'antonyms': antonyms,
        'synonyms':synonyms
    }
    return render(request, 'search.htm', context)