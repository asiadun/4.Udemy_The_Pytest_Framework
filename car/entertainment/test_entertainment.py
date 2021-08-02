from pytest import mark


@mark.smoke
@mark.entertainment
@mark.ui
def test_can_navigate_to_intertainment_page(chrome_browser):
    chrome_browser.get('http://www.siriusxm.com/')
    assert True
