from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')

def result(request):
    sentence=request.GET['sentence']

    wordl = sentence.split()
    print(wordl)

    wordic = {}
    for w in wordl:
        if w in wordic:
            wordic[w] += 1
        else:
            wordic[w] = 1

    return render(request,'result.html',{'fulltext':sentence,'count':len(wordl),'wordic':wordic.items})