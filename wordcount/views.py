from django.http import HttpResponse
from django.shortcuts import render


def homepage(Request):
	
	return render(Request,'home.html')

def count(Request):
	fulltext =Request.GET['fulltext']
	wlist =fulltext.split()
	wordic ={}
	
	for words in wlist:
		
		if words in wordic:
			#increse
			wordic[words] += 1
		
		else:
			#add to dic
			wordic[words] = 1
	
	sorted_words =sorted(wordic.items())
	
	return render(Request,'count.html',{'fulltext':fulltext, 'nword':len(wlist), 'sorted_words':sorted_words })

def about(Request):
	return render(Request,'about.html')

def summa(Request):
	
	return HttpResponse('<h1>summa lololaiku..!</h1>')