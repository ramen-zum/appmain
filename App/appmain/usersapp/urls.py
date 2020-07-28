from django.urls import path
from .views import *

urlpatterns = [
    # Главная страница
    path('', index_view, name='index_url'),
    # заведения
    path('all/', objects_list_view, name='objects_list_url'),
    path('<str:slug>', object_details_view, name='object_detail_url'),
    # Профиль пользователя
    path('userprofile/<str:slug>', user_page_view, name='user_page_url'),
    # Заказы
    path('orders/<str:slug>', orders_view, name='order_list_url'),
    path('new_order/', new_order_view, name='order_url'),
    # Отзывы
    path('reviews/<str:slug>', reviews_view, name='review_list_url'),
    path('new_review/', new_review_view, name='review_url'),
    # Авторизация и регистрация
    path('register/', register_view, name='register_url'),
    path('login/', login_view, name='login_url'),
]