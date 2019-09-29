from django.urls import path
from .views import ItensList, ItensCreate, ItensDelete, ItensUpdate

urlpatterns = [
    path('', ItensList.as_view(), name='itens_list'),
    path('create/', ItensCreate.as_view(), name='itens_create'),
    path('delete/<int:pk>/', ItensDelete.as_view(), name='itens_delete'),
    path('update/<int:pk>/', ItensUpdate.as_view(), name='itens_update'),
]