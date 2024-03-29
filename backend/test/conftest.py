import pytest

from init.app import init_app


@pytest.fixture()
def app():
    app = init_app()
    app.config.update({"TESTING": True})

    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
