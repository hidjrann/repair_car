from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from carApp.forms import RepairForm
from carApp.models import Repair
from django.conf import settings
from .models import Manufacturer
from .forms import FixRequestForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def gallery_view(request):
    return render(request, 'gallery.html')

def offers_view(request):
    return render(request, 'offers.html')



@csrf_exempt
def send_estimate_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Burda email göndərə, ya da DB-ə yaza bilərsən
        print(name, email, message)
        return redirect('index')  # ya da təşəkkür səhifəsinə yönləndir
    return redirect('index')

def repairs(request):
    form = RepairForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('repairs')
    repairs = Repair.objects.all()
    return render(request, 'repairs.html', {'form': form, 'repairs': repairs, 'MEDIA_URL': settings.MEDIA_URL})


def deleteRepair(request, repair_id):
    repair = Repair.objects.filter(id=repair_id).get()
    if request.method == 'POST':
        repair.delete()
        return redirect('repairs')
    else:
        return redirect('repairs')


def editRepair(request, repair_id):
    repair = get_object_or_404(Repair, id=repair_id)
    if request.method == 'POST':
        form = RepairForm(request.POST, request.FILES, instance=repair)
        if form.is_valid():
            form.save()
            return redirect('repairs')
    else:
        form = RepairForm(instance=repair)

    return render(request, 'edit.html', {'form': form})



def manufacturer_list(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, 'manufacturer_list.html', {'manufacturers': manufacturers})




def fix_request_view(request):
    if request.method == 'POST':
        form = FixRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Uğurlu sorğudan sonra ana səhifəyə yönləndirsin
    else:
        form = FixRequestForm()
    
    return render(request, 'fix_request.html', {'form': form})
