
import datetime

class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url==result
        print("Good value URL")


    """Method Screenshot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M")
        name_screenshot = 'screenshot' + now_date + ".png"
        self.driver.save_screenshot('C:\\Users\\eva19\\PycharmProjects\\boomkids\\screen\\' + name_screenshot)


