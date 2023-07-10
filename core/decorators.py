from django.shortcuts import redirect
from django.contrib import messages


# Check si un utilisateur est déjà connecté
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        # L'utilisateur est déjà connecté
        if request.user.is_authenticated:
            return redirect('core:listing_pays')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func


# Autorise l'accès à la page en fonction du type d'utilisateur
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            # L'utilisateur appartient à un groupe
            if request.user.groups.exists:
                group = request.user.groups.all()[0].name

            # Si le groupe de l'utilisateur appartient au groupe autorisé
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                messages.warning(request, "Vous n'êtes pas autorisé à accéder à cette page.", extra_tags='warning')
                return redirect('core:listing_pays')
        return wrapper_func
    return decorator
