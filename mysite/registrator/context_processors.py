from django.conf import settings


def subscribe_enabled(request):
    return {"SUBSCRIBE_ENABLED": settings.SUBSCRIBE_ENABLED}
