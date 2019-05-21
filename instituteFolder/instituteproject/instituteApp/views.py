from django.shortcuts import render

def main_page(request):
    return render(request,'base.html')


def home_page(request):
    return render(request,'home.html' )


def contact_page(request):
    return render(request,'contact.html')


def courses_page(request):
    return render(request,'courses.html')


def feddback_page(request):
    return render(request,'feedback.html')


def team_page(request):
    return render(request,'team.html')


def gallery_page(request):
    return render(request,'gallery.html')