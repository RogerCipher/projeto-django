from django.shortcuts import render

# Create your views here.
def home_page_view(request):
	return render(request, 'website/home.html')

def printer_page_view(request):
	return render(request, 'website/printer.html')

def aboutme_page_view(request):
	return render(request, 'website/aboutme.html')
