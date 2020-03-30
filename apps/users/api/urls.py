from django.urls import path, include
from rest_auth.registration.views import SocialAccountListView, SocialAccountDisconnectView

from apps.users.api import views

app_name = 'api_users'

urlpatterns = [
    path('', include('rest_auth.urls')),
    path('register/', include('rest_auth.registration.urls')),
    path('facebook/', views.FacebookLogin.as_view()),
    path('twitter/', views.TwitterLogin.as_view()),
    path('github/', views.GithubLogin.as_view()),
    path('facebook/connect/', views.FacebookConnect.as_view()),
    path('twitter/connect/', views.TwitterConnect.as_view()),
    path('github/connect/', views.GithubConnect.as_view()),
    path('connected/', SocialAccountListView.as_view()),
    path('connected/<int:pk>/disconnect/', SocialAccountDisconnectView.as_view())
]
