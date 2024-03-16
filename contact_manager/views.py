from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render, get_object_or_404
from .models import Contact
from .models import Password

# @login_required
# def home(request):
#     contacts = Contact.objects.filter(user=request.user)
#     return render(request, 'contact_manager/home.html', {'contacts': contacts})

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

@login_required
def home(request):
    # Retrieve all contacts initially
    contacts = Contact.objects.all()

    # Check if a search query is present
    query = request.GET.get('q')
    if query:
        # Filter contacts based on the search query
        contacts = contacts.filter(name__icontains=query)  # Adjust this as per your model fields

    return render(request, 'home.html', {'user': request.user, 'contacts': contacts})   
   
def personal_contracts(request):
    # Add logic to retrieve personal contracts or any relevant data
    # Retrieve all contacts initially
    contacts = Contact.objects.all()

    # Check if a search query is present
    query = request.GET.get('q')
    if query:
        # Filter contacts based on the search query
        contacts = contacts.filter(name__icontains=query) 
    return render(request, 'personal_contracts.html', {'user': request.user, 'contacts': contacts})   



@login_required
def save_password(request):
    if request.method == 'POST':
        # Process form submission
        url = request.POST.get('url')
        username = request.POST.get('username')
        website_name=request.POST.get('website_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if url and username and email and password:
            # Create and save the password object
            password_obj = Password.objects.create(
                user=request.user,
                url=url,
                username=username,
                email=email,
                password=password
            )
            return redirect('password_list')
    return render(request, 'save_password.html')

@login_required
def password_list(request):
    passwords = Password.objects.filter(user=request.user)
    return render(request, 'password_list.html', {'passwords': passwords})