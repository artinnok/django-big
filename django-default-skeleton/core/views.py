from django.shortcuts import render


def error404(request):
    return render(request, 'core/404.html', status=404)
