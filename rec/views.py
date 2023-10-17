from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def user(request):
    context = {
        "name": request.GET.get("name"),
        "message": request.GET.get("message")
    }

    return render(request, "index.html", context=context)

#  http://127.0.0.1:8000/?name=Tom&message=Давай дружить