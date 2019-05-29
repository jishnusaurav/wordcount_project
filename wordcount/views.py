from django.http import HttpResponse
from django.shortcuts import render
import operator


'''
def home(request):
    return HttpResponse('Hi there !')
'''

def home(request):
    return render(request,'home.html')

def count(request):
    #print(request)
    txt = request.GET['fulltext']
    t = txt.split()
    n = len(t)
    #dict d;
    d={}
    for x in t:
        if(x not in d):
            d[x] = 1
        else:
            d[x]+=1
    sortedwords = sorted (d.items(), key = operator.itemgetter(1) ,reverse = True )
    return render(request,'count.html',{'text':txt , 'words':n,'dict':d ,'list' :sortedwords })

def about(request):
    return render(request,'about.html')