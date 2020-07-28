from django.shortcuts import render
from .models import Company, Order, Review


def index_view(request):
    return render(request, 'usersapp/index.html')

def objects_list_view(request, categoryCode='all', idOfActivity='all'):
    if categoryCode == 'all':
        objects = Company.objects.all()
    else:
        objects = Company.objects.filter(categoryCode=categoryCode, idOfActivity=idOfActivity).all()
    context = {'objects': objects }
    return render(request, 'usersapp/objects_list.html', context)

def object_details_view(request, slug):
    objects = Company.objects.filter(slug=slug).all()
    context = {'objects': objects}
    return render(request, 'usersapp/object_info.html', context)


def user_page_view(request):
    pass

def orders_view(request):
    pass

def new_order_view(request):
    pass

def reviews_view(request):
    pass

def new_review_view(request):
    pass

def register_view(request):
    pass

def login_view(request):
    pass

