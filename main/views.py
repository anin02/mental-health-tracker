from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306218111',
        'name': 'Anindhyaputri Paramitha',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)
