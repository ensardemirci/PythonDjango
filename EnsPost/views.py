from django.shortcuts import render,HttpResponse


def post_index(request):
    return HttpResponse('Burası Post İndex Sayfası')

def post_detail(request):
    return HttpResponse('Burası Post Detail Sayfası')

def post_create(request):
    return HttpResponse('Burası Post Create Sayfası')

def post_update(request):
    return HttpResponse('Burası Post Update Sayfası')

def post_delete(request):
    return HttpResponse('Burası Post Delete Sayfası')


