import pytest
from selene import browser, be, have

@pytest.fixture(params=[(1920, 1080), (1366, 768), (1440, 900)])
def desktop_browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.fixture(params=[(720,1280), (1080,1920)])
def mobile_browser(request):
    width, height = request.param
    browser.config.window_width = 375
    browser.config.window_height = 667
    yield
    browser.quit()