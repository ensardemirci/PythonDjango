from django.shortcuts import render,HttpResponse


def home_view(request):
    if request.user.is_authenticated==True:
        context = {
            'isim': request.user.username,
        }
    else:
        context = {
            'isim': 'Misafir',
        }
    return render(request,'home.html',context)

