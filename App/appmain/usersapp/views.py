from django.shortcuts import render
from .models import Company, Order, Review


def index_view(request):
    return render(request, 'usersapp/index.html')

def objects_list_view(request):
    pass

def object_details_view(request):
    pass

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

