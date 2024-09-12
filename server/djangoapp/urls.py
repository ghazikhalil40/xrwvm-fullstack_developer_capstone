from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import registration

app_name = 'djangoapp'

urlpatterns = [
    # # path for registration

    # path for login
    path('login', views.login_user, name='login'),
        path(route='get_cars', view=views.get_cars, name ='getcars'),
    path('register/', registration, name='register'),

    # path for logout
    path('logout/', views.logout_user, name='logout'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
