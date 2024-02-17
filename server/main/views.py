from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/home-page.html')

def about_page(request):
    return render (request, 'main/school-about-page.html')