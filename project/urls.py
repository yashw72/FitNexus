from django.contrib import admin
from django.urls import path, include
from gym import views as gym_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', gym_views.login_view, name='login'),
    path('logout/', gym_views.logout_view, name='logout'),
    path('', include('gym.urls')),
]
