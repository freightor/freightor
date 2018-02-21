from django.core.exceptions import PermissionDenied
# create a check to verify that user has admin privileges


def admin_access_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.profile.role == "admin":
            return function(request, *args, **kwargs)
        raise PermissionDenied

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap


def logout_required(function):
    pass
