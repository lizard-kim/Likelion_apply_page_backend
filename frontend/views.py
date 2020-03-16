from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from apply.models import Apply

def main(request):
    return render(request, 'main.html')

def apply(request):

    if(request.method=='POST' and request.FILES['table']):
        
        
        name = request.POST.get('name')
        school_id = request.POST.get('schoolId')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        major = request.POST.get('major')
        tech_stack = request.POST.get('techStack')
        motivation = request.POST.get('motivation')
        idea = request.POST.get('idea')
        apply_file = request.FILES['table']

        #table = request.POST.get('table')

        new_apply = Apply.objects.create(
            name = name,
            school_id = school_id,
            phone_number = phone_number,
            email = email,
            major = major,
            tech_stack = tech_stack,
            motivation = motivation,
            idea = idea,
            table = apply_file
        )
        return redirect('/')
    
    else:
        return render(request, 'apply.html') 