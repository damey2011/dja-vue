from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from django.conf import settings
from rest_auth.registration.views import SocialLoginView, SocialConnectView
from rest_auth.social_serializers import TwitterLoginSerializer, TwitterConnectSerializer


class FacebookLogin(SocialLoginView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    adapter_class = FacebookOAuth2Adapter


class TwitterLogin(SocialLoginView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class GithubLogin(SocialLoginView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client


class FacebookConnect(SocialConnectView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    adapter_class = FacebookOAuth2Adapter


class TwitterConnect(SocialConnectView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter


class GithubConnect(SocialConnectView):
    """
        Find docs for this at: https://django-rest-auth.readthedocs.io/en/latest/
    """
    adapter_class = GitHubOAuth2Adapter
    callback_url = settings.GITHUB_CALLBACK_URL
    client_class = OAuth2Client
