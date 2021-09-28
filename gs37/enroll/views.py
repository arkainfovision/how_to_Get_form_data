from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.


def showformdata(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
          print('Form Validated')
          name = fm.cleaned_data['name']
          email = fm.cleaned_data['email']
          print('Name', name)
          print('Email', email)

    else:

     fm =  StudentRegistration()

     print('get se aaya hai')


    
    return render(request, 'enroll/userregistration.html', {'form': fm})
