from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Contact
@login_required
def home(request):
    contacts = Contact.objects.filter(user=request.user)
    return render(request, 'contact_manager/home.html', {'contacts': contacts})

@login_required
def view_contact(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    return render(request, 'contact_manager/view_contact.html', {'contact': contact})

@login_required
def add_contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        mobile_number = request.POST['mobile_number']
        Contact.objects.create(user=request.user, name=name, mobile_number=mobile_number)
        return redirect('home')
    return render(request, 'contact_manager/add_contact.html')


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'
    

def edit_contact(request, contact_id):
    # Retrieve the contact object from the database
    contact = get_object_or_404(Contact, pk=contact_id)
    
    # Add logic for editing the contact here

    return render(request, 'edit_contact.html', {'contact': contact})
   
