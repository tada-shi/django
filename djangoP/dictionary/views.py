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
        'Noun' : meaning['Noun'][0],
        'Verb' : meaning['Verb'][0],
        'Adjective' : meaning['Adjective'][0],
        'antonyms': antonyms,
        'synonyms':synonyms
    }
    return render(request, 'search.htm', context)