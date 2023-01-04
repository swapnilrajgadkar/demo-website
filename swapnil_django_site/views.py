from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def analyze(request):
    django_text = request.POST.get('text', 'default')
    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in django_text:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps == "on":
        analyzed = ""
        for char in django_text:
            analyzed = analyzed + char.upper()
        params = {'purpose':'Capitalized Text', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if newlineremover == "on":
        analyzed = ""
        for char in django_text:
            if char != '\n' and char != '\r':
                analyzed = analyzed + char
            else:
                del char
        params = {'purpose':'New Line Remover', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(django_text):
            if not(django_text[index] == " " and django_text[index+1]==" "):
                analyzed = analyzed + char
        params = {'purpose':'Extra Space Remover', 'analyzed_text': analyzed}
        django_text = analyzed
        # return render(request, 'analyze.html', params)

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("Please Select Any Operation & Try Again !")

    return render(request, 'analyze.html', params)