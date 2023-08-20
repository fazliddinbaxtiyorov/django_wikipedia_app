from django.shortcuts import render, HttpResponse
import wikipedia


# Create your views here.
def index(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            result = wikipedia.summary(search, sentences=10)
        except Exception as error:
            return HttpResponse(f"Wrong input. {error}")
        return render(request, "wiki/index.html", {"result": result})

    return render(request, "wiki/index.html")
