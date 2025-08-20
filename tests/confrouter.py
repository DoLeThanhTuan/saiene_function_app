from api.healthcheck import healthcheck_app, healthcheck_route
from api.healthcheck_db import healthcheck_db_app, healthcheck_db_route
from api.ui012 import ui012_app, ui012_route

from core.utils.application import create_fastapi


def test_app():
    testApp = create_fastapi()
    testApp.mount(healthcheck_route, healthcheck_app)
    testApp.mount(healthcheck_db_route, healthcheck_db_app)
    testApp.mount(ui012_route, ui012_app)

    return testApp
