import datetime
from test_utility import create_log


class ScreenShot(object):
    @staticmethod
    def capture_screen_shot(driver, test_case_name):

        directory = "screen_shots/"
        path = directory + test_case_name + "_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S")) + ".png"
        driver.get_screenshot_as_file(path)
        create_log.create_log(" Screen shoot captured... ")
