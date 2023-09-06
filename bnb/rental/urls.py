
from django.urls import path
from . import views

app_name = 'rental'

urlpatterns = [

#(in browser it will be localhost/rental/bnb/create/)

    path('bnb/create/', views.bnb_create,name='bnb_create'),
    path('bnb/list/', views.bnb_list, name='bnb_list'),
    path('user/create/', views.user_create, name='user_create'),
    path('user_list/', views.user_list, name='user_list'),
    path('booking/create/', views.booking_create, name='booking_create'),
    path('booking/list/', views.booking_list, name='booking_list'),
    path('review/create/', views.review_create, name='review_create'),
    path('review/list/', views.review_list, name='review_list'),
]

#urlpatterns = [
 #   path('your-url-pattern/', views.your_view_function, name='your-url-name'),
    # Add more URL patterns as needed
#]
