from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def home(request):
    context={
      'jobs':Job.objects.all()
}

    return render(request, 'homepage/home.html',context)
def about(request):
    return render(request, 'homepage/about.html')