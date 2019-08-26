from django.urls import path
from emsapp import views

app_name = 'emsapp'

urlpatterns = [
    path('employee/', views.employee, name='employee'),
    path('upload/', views.upload, name='upload'),
    path('add/', views.add, name='add'),
    path('delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('updatelogic/', views.updatelogic, name='updatelogic')
]
