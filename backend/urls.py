from django.contrib import admin
from django.urls import path
from dealers.views import get_dealers, get_dealer_by_id

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_dealers),
    path('dealers', get_dealers),
    path('dealers/<int:id>', get_dealer_by_id),
]