import time

import requests
from selenium.webdriver.common.keys import Keys

from page_objects.locators.weather_ui_locators import WeatherUILocators
from test_utility.utility_methods import UtilMethods


class WeatherUIPage(WeatherUILocators):

    def __init__(self, driver):
        self.driver = driver
        self.util_obj = UtilMethods(self.driver)
        self.location_search_input_xpath = WeatherUILocators.location_search_input_xpath
        self.arrow_down_xpath = WeatherUILocators.arrow_down_xpath
        self.metric_unit_xpath = WeatherUILocators.metric_unit_xpath
        self.temperature_xpath = WeatherUILocators.temperature_xpath

    def get_phase1_temperature(self, location):
        self.util_obj.send_keys(self.location_search_input_xpath, location)
        time.sleep(2)
        self.util_obj.send_keys(self.location_search_input_xpath, Keys.ENTER)
        time.sleep(2)
        self.util_obj.click(self.arrow_down_xpath)
        time.sleep(2)
        self.util_obj.click(self.metric_unit_xpath)
        time.sleep(2)
        temperature = self.util_obj.get_text(self.temperature_xpath)[:-1]
        return float(temperature)

    @staticmethod
    def get_phase2_temperature(location):
        app_id = '123507e5732a4f5a4c407639a0d9d9b4' # this app_id is invalid and cannot be used, please obtain and API toke from the website https://api.openweathermap.org
        url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&APPID={app_id}'
        payload = {}
        headers = {'content-type': 'application/json'}
        params = {}

        response = requests.post(url, data=payload, headers=headers, params=params, allow_redirects=True).json()
        phase2_temp = float(response['main']['temp'])
        return phase2_temp

    @staticmethod
    def verify_with_variance(temp1, temp2):
        actual_variance = (abs(temp1 - temp2) / temp1) * 100.0
        return actual_variance
