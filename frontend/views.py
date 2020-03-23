from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib import auth

from apply.models import Apply

def main(request):
    return render(request, 'main.html')

def apply(request):
    if(request.method=='POST' and request.FILES.get('table')):
        name = request.POST.get('name')
        school_id = request.POST.get('schoolId')
        phone_number = request.POST.get('phoneNumber')
        email = request.POST.get('email')
        major = request.POST.get('major')
        fglp = request.POST.get('fglp')
        tech_stack = request.POST.get('techStack')
        expectation = request.POST.get('expectation')
        motivation = request.POST.get('motivation')
        idea = request.POST.get('idea')
        apply_file = request.FILES['table']
        apply_file_format = apply_file.content_type
        filename = ""
        find_dot = 0
        for i in range(len(apply_file_format)):
            if(find_dot == 1):
                filename += apply_file_format[i]
            if(apply_file_format[i] == '/'):
                find_dot = 1
        apply_file.name = school_id + "." + filename

        new_apply = Apply.objects.create(
            name = name,
            school_id = school_id,
            phone_number = phone_number,
            email = email,
            major = major,
            fglp = fglp,
            table = apply_file,
            tech_stack = tech_stack,
            motivation = motivation,
            expectation = expectation,
            idea = idea,
        )

        return redirect('/')
    
    else:
        return render(request, 'apply.html') 

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/adminpage')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'login.html')


def detail(request, id):
    apply_info = Apply.objects.filter(id = id)
    return render(request, 'detail.html',{
        'apply_info': apply_info
    })

def admin(request):
    apply_info = Apply.objects.all()
    return render(request, 'admin.html', {
        'apply_info': apply_info
    })

def adminlist(request):
    apply_info = Apply.objects.all()
    return render(request, 'adminlist.html',{
        'apply_info' : apply_info
    })