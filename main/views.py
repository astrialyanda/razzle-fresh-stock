from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'fruit': 'Apple',
        'price': '20000'
    }

    return render(request, "main.html", context)