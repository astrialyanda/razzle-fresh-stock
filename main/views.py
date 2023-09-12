from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Apple',
        'amount': '100'
    }

    return render(request, "main.html", context)