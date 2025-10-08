import pytest
from selene.support.shared import browser
from selene import be, have

@pytest.fixture(params=[(1920, 1080), (1366, 768), (720,1280), (1080,1920)])
def browser(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    if width >= 1080:
        yield 'desktop_browser'
    else:
        yield 'mobile_browser'
    browser.quit()