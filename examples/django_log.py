# Example: Using VersaLog with Django
#
# In your settings.py, add:
#
#   LOGGING_CONFIG = None  # Disable Django's default logging config
#
#   from VersaLog import VersaLog, setup_django_logging
#   log = VersaLog(enum="detailed", show_tag=True, tag="Django")
#   setup_django_logging(log)

# views.py
from django.http import JsonResponse
import logging

logger = logging.getLogger(__name__)

def index(request):
    logger.info("Hello from Django")
    return JsonResponse({"msg": "ok"})