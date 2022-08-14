from django.urls import path
from . import views
urlpatterns = [
    path('createusers/',views.createAllUsersTest,name='createusers'),
    # path('message/',views.message,name='message'),
]
