from django.shortcuts import render

from first_app.forms import StudentForm
# Create your views here.
def home(request):
    if request.method == "POST":
        std= StudentForm(request.POST)
        if std.is_valid():
            std.save()
            std= StudentForm()
    else:
        std= StudentForm()
    return render(request, "home.html",{"student":std})
   