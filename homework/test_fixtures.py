import pytest
from selene import browser, be, have
from homework.conftest import desktop_browser, mobile_browser

@pytest.mark.usefixtures("desktop_browser")
def test_github_desktop():
    open.browser("https://github.com")
    assert browser.element(".HeaderMenu-link--sign-in").should(be.visible)
    

@pytest.mark.usefixtures("mobile_browser")
def test_github_mobile():
    open.browser("https://github.com")
    assert browser.element("Button-label").should(be.visible)
    
