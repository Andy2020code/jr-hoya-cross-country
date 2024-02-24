from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/home-page.html')

def about_page(request):
    return render (request, 'main/school-about-page.html')

def schedule_page(request):
    return render (request, 'main/school-game-schedule.html')

def march_schedule_page(request):
    return render (request, 'main/march-schedule.html')

def april_schedule_page(request):
    return render (request, 'main/april-schedule.html')

def coming_soon(request):
    return render (request, 'main/coming-soon.html')

def coach_bios(request):
    return render (request, 'main/coach_bios.html')