from django.urls import path
from . import views

urlpatterns = {
    path('hello/', views.hello, name='hello'),
    path('greet/', views.greet, name='greet'),
    path('rules/', views.rules, name='rules'),
    path('page/', views.page, name='page'),
}
