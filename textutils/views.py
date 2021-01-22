#This file is created by me - Anuran Jan 16 21:22
from django.http import HttpResponse
#def index(request):
#	return HttpResponse("<h1>hello world</h1>")
from django.shortcuts import render

def about(request):
	return HttpResponse("Hello there! I am Anuran")	

def index(request):
	#return HttpResponse("Home")
	#params={'name':'Anuran','place':'Hachinasu'}
	return render(request,'index.html')#,params)
	
#def removepunc(request):
	#Get the text
#	djtext = request.GET.get('text', 'default')
	#Analyze the text
#	print(djtext)
#	return HttpResponse("Remove Punc")
def analyze(request):
	purpose=[]
	#Get the text
	djtext = request.POST.get('text', 'default')
	#Analyze the text
	punc='''!-/?.,;':{}[]\&()@#$%^*_=+<>'"'''
	removepunc = request.POST.get('removepunc', 'off')
	newlineremove = request.POST.get('newlineremove', 'off')
	spaceremove = request.POST.get('spaceremove', 'off')
	fullcaps=request.POST.get('fullcaps', 'off')
	charcount=request.POST.get('charcount', 'off')
	#print(djtext)
	resp=[removepunc,newlineremove,spaceremove,fullcaps,charcount]
	if 'on' in resp:
		if removepunc == 'on':
			analyzed=""	
			for char in djtext:
				if char in punc:
					continue
				else:
					analyzed=analyzed+char
					djtext=analyzed	
			purpose.append('Remove Punctuation')		
			params={'purpose':purpose,'analyzed_text': djtext}	

			#print(removepunc)
			#return render(request,'analyze.html',params)
		if fullcaps=='on':
			djtext=djtext.upper()
			purpose.append('Upper case')
			params={'purpose':purpose,'analyzed_text': djtext}
			#return render(request,'analyze.html',params)					

			
		if newlineremove=="on":
			analyzed=""
			text=djtext.splitlines()	
			for i in text:
				analyzed+=i
			djtext=analyzed
			purpose.append('Remove newline')
			params={'purpose':purpose,'analyzed_text': djtext}
			#return render(request,"analyze.html",params)
				
		if spaceremove=="on":
			analyzed=djtext.replace("  "," ")
			analyzed=analyzed.strip()
			#for char in djtext:
			#	if char == " ":
			#		continue
			#	else:
			#		analyzed=analyzed+char	
			djtext=analyzed
			purpose.append('Remove space')
			params={'purpose':purpose,'analyzed_text': djtext}
			#return render(request,"analyze.html",params)
		if charcount=='on':
			c=0
			characters="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
			for char in djtext:
				if char in characters:
					c+=1
			purpose.append('Character count')
			djtext+="\n(Number of characters in the string="+str(c)+")"	
			params={'purpose':purpose,'analyzed_text': djtext}	
			#return render(request,"analyze.html",params)
		return render(request,"analyze.html",params)	
	else:
		return render(request,"error.html")	
	
def capfirst(request):
	return HttpResponse("Capitalize First")		

def newlineremove(request):
	return HttpResponse("Remove newline")					

def spaceremove(request):
	return HttpResponse("Remove space")		
			
def charcount(request):
	return HttpResponse("Count characters")
