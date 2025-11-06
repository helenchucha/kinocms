from django.core.exceptions import PermissionDenied
from functools import wraps

def staff_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_staff:
            raise PermissionDenied()
        return view_func(request, *args, **kwargs)
    return _wrapped_view