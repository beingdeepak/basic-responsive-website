from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

#def index(request):
    return HttpResponse("hello")

#def capitalizefirst(request):
    return HttpResponse("capitalize first")

#def newlineremove(request):
    return HttpResponse("newlinremove")


#def charcount(request):
    return HttpResponse("char count")

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    print(removepunc)
    print(djtext)
    
    if removepunc == "on":
        #analyzed = djtext
        punctuations = '''!()-[];:'"\,<>./?@#$%^&*_-'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
               analyzed = analyzed + char
        params = {'purpose' : 'Removed punctuations', 'analyzed_text' : analyzed} 
            
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose' : 'Changed to Uppercase', 'analyzed_text' : analyzed}     
        return render(request, 'analyze.html', params)    

    elif(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
             if char !="\n":
                analyzed = analyzed + char
        params = {'purpose' : 'Removed Newlines', 'analyzed_text' : analyzed}     
        return render(request, 'analyze.html', params)   
    
    else:
        return HttpResponse("error")
            

#def about(request):
   # return HttpResponse('''<h1>about Deepak<hi> ''')

#def spaceremove(request):
    #return HttpResponse("space remover <a href='/'<a>back</a> ")

#def removepunc(request):
    #get the text
    #djtext= request.GET.get('text', 'default')
   # print(djtext)
    #analyze the text 
  #  return HttpResponse("Welcome deepak")