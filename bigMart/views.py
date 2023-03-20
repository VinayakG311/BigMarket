from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt 
def index(request):
    if(request.method== 'POST'):
        print(request.POST['checker'])
    return render(request,"index.html")