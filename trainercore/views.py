from django.shortcuts import render
from trainer.models import Trainer


# Create your views here.

def trainer(request):
    trainers = Trainer.objects.count()
    data ={"trainers":trainers}
    return render(request, "trainer_page.html", data)