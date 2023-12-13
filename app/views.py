from django.shortcuts import render
from datetime import datetime
from .models import relation
# Create your views here.
def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        rel = request.POST.get('rel')
        date= datetime.today()
        print(name,age,rel,date)
        Relation = relation(name=name,age=age,rel=rel,date=date)
        Relation.save()
    
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")
