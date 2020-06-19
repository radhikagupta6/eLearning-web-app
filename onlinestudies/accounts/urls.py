
from django.urls import path
from . import views as ac_views
urlpatterns = [
    path('login/', ac_views.login_view, name="login"),
    path('', ac_views.dashboard, name="dashboard"),
    path('logout/', ac_views.logout_view, name="logout")
]
