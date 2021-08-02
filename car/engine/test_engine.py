#Just a simple note
from pytest import mark

@mark.engine
@mark.ui
def test_can_navigate_to_intertainment_page(chrome_browser):
    chrome_browser.get('http://www.onliner.by/')
    assert True
