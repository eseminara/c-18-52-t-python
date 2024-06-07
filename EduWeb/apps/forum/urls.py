from django.urls import path
from .views import forum_list, forum_detail, create_forum, delete_message, ForumView

urlpatterns = [
    path('', forum_list, name='forum_list'),
    path('create/', create_forum, name='create_forum'),
    path('<int:pk>/', forum_detail, name='forum_detail'),
    path('delete_message/<int:pk>/', delete_message, name='delete_message'),
    path('api/forum/', ForumView.as_view(), name='api_forum'),  # Añade esta línea
]