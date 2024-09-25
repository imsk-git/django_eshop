

from django.urls import path

from . import views


urlpatterns = [
    path('contact-us/', views.contact_us, name='contact_us'),
    path('store-contact-us/', views.store_contact_us, name='store_contact_us'),
]