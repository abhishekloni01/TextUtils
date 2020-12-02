from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


def analyse(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalize = request.GET.get('capitalize', 'off')
    newlinermv = request.GET.get('newlinermv', 'off')
    rmvextspc = request.GET.get('rmvextspace', 'off')

    punctuations = '''!()-[]{};:'=+",<>./?@#$%^&*_~`'''
    if removepunc == 'on':
        analysed = ""
        for char in djtext:
            if char not in punctuations:
                analysed += char
        params = {'purpose': 'Remove Punctuations',
                  'analysed_text': analysed
                  }
        djtext = analysed

    if newlinermv == 'on':
        analysed = ""
        for char in djtext:
            if char != '\n' and char != '\r':
                analysed += char
        params = {'purpose': 'New line remover',
                  'analysed_text': analysed
                  }
        djtext = analysed

    if rmvextspc == 'on':
        analysed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] == " ":
                pass
            else:
                analysed += char
        params = {'purpose': 'Remove extra space',
                  'analysed_text': analysed
                  }
        djtext = analysed

    if capitalize == 'on':
        analysed = ""
        for char in djtext:
            analysed += char.upper()

        params = {'purpose': 'Capitalize',
                  'analysed_text': analysed
                  }
        djtext = analysed

    if removepunc != 'on' and newlinermv != 'on' and rmvextspc != 'on' and capitalize != 'on':
        return HttpResponse('Error')

    return render(request, 'analyse2.html', params)
