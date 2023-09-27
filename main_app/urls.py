from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name='index'),
    path('finches/<int:finch_id>', views.finches_detail, name='detail'),
    # new route used to show a form and create a finch
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    # new route used to show a form and update a finch
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
    # new route used to show a form and delete a finch
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
    #---------- Feeding ---------
    path('finches/<int:finch_id>/add_feeding', views.add_feeding, name='add_feeding'),
    #---------- Toy ---------
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
    # new route used to show a form and show a feeding
    path('toys/', views.ToyList.as_view(), name='toys_index'),
    # new route used to show a form and create a feeding
    path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),

    
]