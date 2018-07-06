from django.shortcuts import render
from .models import employee

# Create your views here. 
from django.http import HttpResponse

def index(request):
	return HttpResponse("hello world")

def home(request):
	e=employee.objects.all()
	#context={"employees":e}#is a scope and is a dictionaries format print and it is must
	return render(request,"website/home.html",{"employees":e})
	#output=",".join([str(person.age) for person in e])#here use in comprehension and (person.age) is work on the return and person to itrete the database value one by one and strore the person.age on value
	#return HttpResponse(output)

def detail(request,e_id):
	e=employee.objects.get(pk=e_id)
	return render(request,"website/detail.html",{"employee":e})


def about(request):
	return HttpResponse("hello about")





