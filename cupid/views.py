from django.shortcuts import render
from .models import person

# Create your views here.


def home(request):
    data = dict()

    if request.method == 'POST':
        p = person()
        p.gsb_id = request.POST.get('gsb_id')
        p.mate1_id = request.POST.get('mate1_id')
        p.mate2_id = request.POST.get('mate2_id')
        p.mate3_id = request.POST.get('mate3_id')
        p.save()

    return render(request, 'home.html', context=data)


def submit(request):
    data = dict()

    if request.method == 'POST':
        p = person()
        p.gsb_id = request.POST.get('gsb_id')
        p.mate1_id = request.POST.get('mate1_id')
        p.mate2_id = request.POST.get('mate2_id')
        p.mate3_id = request.POST.get('mate3_id')
        p.save()

    return render(request, 'submit.html', context=data)