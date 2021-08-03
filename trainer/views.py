from django.shortcuts import render
from .forms import TrainerRegistrationForm

# Create your views here.
def register_trainer(request):
    if request.method =="POST":
        form = TrainerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else: 
         #creating an instance of the form

         form = TrainerRegistrationForm()
    return render(request,"register_trainer.html",{"form":form})
    