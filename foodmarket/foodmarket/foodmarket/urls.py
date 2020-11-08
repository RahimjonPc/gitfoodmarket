from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from foods.views import HomeDetailView, delete
from foodslogic.views import HomeListView, FoodCreateView, FoodEditView, MyProjectLoginView, RegisterUserView, MyProjectLogout


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('foods.urls')),
    path('foodslogic/', include('foodslogic.urls'))
]

urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



