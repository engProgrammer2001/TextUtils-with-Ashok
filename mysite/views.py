# this files is create by ashok bhai
# for run server= python manage.py runserver

from django.http import  HttpResponse
from django.shortcuts import render  # import templates from this line.

def index(request):
    # params={'name':'ashok','place':'Jabalpur'}
    return render(request, 'index.html') # we can pass dictionary in this render function
    # return HttpResponse('''<h1>Hello ashok</h1> <a href="https://github.com/engProgrammer2001">
    #  Ashok GithubProfile <a href="https://www.hackerrank.com/skills-verification">
    #  Ashok HackerrankProfile''')
def about(request):
    return HttpResponse('''<h1>about ashok</h1> <a href="http://codeashok.unaux.com/">
     About Ashok''')

def ex1(request):
    sites = ['''<h1>For Entertainment </h1><a href = "https://www.youtube.com" >youtube video</a>''',
             '''<h1>For Interaction </h1><a href = "https://www.facebook.com" >Facebook</a>''',
             '''<h1>For Insight   </h1><a href = "https://www.ted.com/talks" >Ted Talk</a>''',
             '''<h1>For Internship   </h1><a href="https://internshala.com" >Intenship</a>''',
             ]
    return HttpResponse((sites))


def analyze(request):
    # GET the text
    djangotext = request.POST.get('text','default') # we can access djangotext data by using this line

    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    ExtraSpaceRemover = request.POST.get('ExtraSpaceRemover','off')
    print(removepunc)
    print(djangotext)

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djangotext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Remove punctuation','analyzed_text': analyzed}
        djangotext = analyzed
        # return render(request,'analyze.html',params)

    if(fullcaps=="on"):
        analyzed = ""
        for char in djangotext:
            analyzed = analyzed + char.upper()
        params={'purpose':'Change to UpperCase','analyzed_text':analyzed}
        djangotext = analyzed
        # return render(request,'analyze.html',params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djangotext:
            if char !="\n" and char!="\r":
                analyzed = analyzed + char
        params={'purpose':'Remove new line','analyzed_text':analyzed}
        djangotext = analyzed
        # return  render(request,'analyze.html',params)

    if(ExtraSpaceRemover=="on"):
        analyzed = ""
        for index,char in enumerate(djangotext):
            if not (djangotext[index] == " " and djangotext[index+1] == " "):
                analyzed = analyzed + char
        params={'purpose':'ExtraSpaceRemove','analyzed_text':analyzed}

    if(removepunc != "on" and fullcaps!="on" and newlineremover != "on" and ExtraSpaceRemover!="on"):
        return  HttpResponse ("Error! Plese select any one Operations")

    return render(request, 'analyze.html', params)


def about(request):
    return render(request,'about.html')



# def capitalize(request):
#     return HttpResponse("capitalize punc")
# def newlineremove(request):
#     return HttpResponse("newlineremove punc")
# def spaceremove(request):
#     return HttpResponse("spaceremove punc")
# def charcount(request):
#     return HttpResponse("charcount punc")



