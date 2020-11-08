from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from foods.views import HomeDetailView, delete
from .views import HomeListView, FoodCreateView, FoodEditView, MyProjectLoginView, RegisterUserView, MyProjectLogout


urlpatterns = [
    path('', HomeListView.as_views(), name="home"),
    path('create', FoodCreateView.as_views(), name="create"),
    path('edit/<int:pk>', FoodEditView.as_views(), name="edit"),
    path('login', MyProjectLoginView.as_views(), name="login"),
    path('register', RegisterUserView.as_iews(), name="register"),
    path('logout', MyProjectLogout.as_views(), name="logout"),
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)