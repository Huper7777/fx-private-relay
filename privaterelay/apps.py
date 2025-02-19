from typing import Any
import requests
import os

from django.apps import AppConfig
from django.conf import settings


ROOT_DIR = os.path.abspath(os.curdir)


class PrivateRelayConfig(AppConfig):
    name = "privaterelay"

    def __init__(self, app_name, app_module):
        super(PrivateRelayConfig, self).__init__(app_name, app_module)
        self.fxa_verifying_keys: list[dict[str, Any]] = []

    def ready(self):
        import privaterelay.signals  # noqa: F401

        resp = requests.get(
            "%s/jwks" % settings.SOCIALACCOUNT_PROVIDERS["fxa"]["OAUTH_ENDPOINT"]
        )
        if resp.status_code == 200:
            resp_json = resp.json()
            self.fxa_verifying_keys = resp_json["keys"]
