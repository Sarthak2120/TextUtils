from django.http import HttpResponse
from django.shortcuts import render
# i have created this file
def index(request):
    #isse home page me index.html dikhega
    return render(request,'index.html')
    #return HttpResponse("home")
def about(request):
    return HttpResponse("hello about")

def analyze(request):
    #get the text
    djtext=request.POST.get('text','default')#request.GET.get ye apne jo bhi apne dala hai kese idar text mera name tha jisme mera text me jo value store  hogi wo usko lega or usko dega
    #djtext me isleia stor kiya ki isko html me leke jayege backend me to output dera user ko kese dikhega to djtext me store krliya djtext ko html file me use karege 
    #check checbox value
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    
    #check which checkbox is on
    if removepunc=="on":
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
    

        params={'purpose':'Removed punctuations','analyzed_text':analyzed}
        djtext=analyzed
       
       
       # return render(request,'analyze.html',params)
   
   
    if(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    

    if(extraspaceremover=="on"):
        analyzed=""
        for index,char in enumerate(djtext): #for loop konsi value par chalra hai text m e wo janne k liye enumerate use krte hai
            if not(djtext[index]==" " and djtext[index+1]== " "): 
                analyzed=analyzed+char
        params={'purpose':'extraspaceremover','analyzed_text':analyzed}
        djtext=analyzed
        #return render(request,'analyze.html',params)
    

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed=analyzed+char
            else:
                print("no")
        print("pre",analyzed)
        params={'purpose':'Removed NewLines','analyzed_text':analyzed}
        
    if(removepunc != "on" and newlineremover!="on" and extraspaceremover!="on" and fullcaps!="on"):
        return HttpResponse("please select the operation and try again")



    return render(request,'analyze.html',params)
    



