from django.shortcuts import render

# Create your views here.
def info_page_view(request):
    return render(request, 'info_page.html')