from django.shortcuts import redirect, render
from .models import user
from .forms import user_form



def list_users(request):
    data = user.objects.all()
    return render(request, "list_users.html",{"data":data})


def create_users(request):
    form = user_form()
    if request.method == "POST":
        form = user_form(request.POST)
        if form.is_valid():
            data1 = user(**form.cleaned_data)
            data1.save()
            return redirect("user list")
    return render (request,"create_users.html",{"form":form})
