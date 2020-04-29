from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('index/', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('show/<int:post_id>', views.show, name="show"),
    path('edit/<int:post_id>', views.edit, name="edit"),
    path('update/<int:post_id>', views.update, name="update"),
]
