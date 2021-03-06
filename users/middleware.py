from django.http.response import JsonResponse
from django.utils import timezone
from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework import status
from rest_framework_simplejwt import authentication


class LastActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')

        # need to separately detect user when used middleware with JWT (else AnonymousUser)
        try:
            auth_res = authentication.JWTAuthentication().authenticate(request)
        except InvalidToken:
            return JsonResponse({'error': 'Invalid token'}, status=status.HTTP_401_UNAUTHORIZED)

        if auth_res:
            request.user = auth_res[0]

        # save last_activity on each authenticated request
        if request.user.is_authenticated:
            request.user.last_activity = timezone.now()
            request.user.save()
