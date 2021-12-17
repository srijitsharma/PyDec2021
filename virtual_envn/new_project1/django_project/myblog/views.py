from django.shortcuts import render
from django.http import HttpResponse


posts = [

		{
		'author':'John',
		'title':'blog post 1',
		'content':'first post',
		'date_posted': 'Dec 14, 2021'
		},


		{
		'author':'Tom',
		'title':'blog post 2',
		'content':'Second post',
		'date_posted': 'Dec 15, 2021'
		}
]

# Create your views here.
def home(request):
	context = {'posts':posts}
	return render(request, 'myblog/home.html',context)

def about(request):
	
	return render(request, 'myblog/about.html')



