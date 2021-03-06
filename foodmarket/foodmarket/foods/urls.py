from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from foods.views import HomeDetailView, delete
from foodslogic.views import HomeListView, FoodCreateView, FoodEditView, MyProjectLoginView, RegisterUserView, MyProjectLogout


urlpatterns = [
    path('order/<int:pk>', HomeDetailView.as_views(), name="order"),
    path('delete/<int:pk>', delete, name="delete"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)