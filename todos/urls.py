
from django.urls import path
from rest_framework_simplejwt.views import(
    TokenObtainPairView,
    TokenRefreshView
)

from .views import(
    RegisterView,
    TodoListCreateView,
    TodoDetailView,
    LogoutView,
)

urlpatterns=[
    # Authentication

    path('register/',RegisterView.as_view(),name='register'),
    path('login/',TokenObtainPairView.as_view(),name='login'),
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('logout/',LogoutView.as_view(),name='logout'),

    # --------todocrud

    path('todos/',TodoListCreateView.as_view(),name='todo_list_create'),
    path('todo/<int:pk>/',TodoDetailView.as_view(),name='todo_detail'),
]