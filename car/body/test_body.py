from pytest import mark

@mark.body
@mark.ui
class BodyTest:
    @mark.door
    def test_can_navigate_to_body_page(self, chrome_browser):
        chrome_browser.get('http://www.motortrend.com/')
        assert True

    @mark.body
    def test_bumper(self):
        assert True

    @mark.body
    def test_windshield(self):
        assert True
