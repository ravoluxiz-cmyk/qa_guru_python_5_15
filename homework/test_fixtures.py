import pytest
from selene.support.shared import browser
from selene import be, have
from homework.conftest import desktop_browser, mobile_browser

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


@pytest.mark.usefixtures("browser")
def test_github_desktop():
    if browser == 'desktop_browser':
        browser.open("https://github.com")
        assert browser.element(".HeaderMenu-link--sign-in").should(be.visible)
    else:
        pytest.skip("Skipped for mobile browser")

@pytest.mark.usefixtures("browser")
def test_github_mobile():
    if browser == 'mobile_browser':
        browser.open("https://github.com")
        assert browser.element('.HeaderMenu-link--sign-in').should(be.visible)
    else:
        pytest.skip("Skipped for desktop browser")

