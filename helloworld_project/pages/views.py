from django.http import HttpResponse

def homePageView(request):
	return HttpResponse("The Home page!")