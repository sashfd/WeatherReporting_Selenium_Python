import json

from test_base.environment_setup import EnvironmentSetup
from test_utility import screen_shot
import time
from test_utility.utility_methods import UtilMethods
from test_utility import create_log
from page_objects.pages.weather_ui_page import WeatherUIPage


class TestWeatherComparator(EnvironmentSetup):

    def setUp(self):
        self.startTime = time.time()
        self.util_obj = UtilMethods(self.driver)
        self.result = None
        create_log.create_log(self.id() + ' ' + 'started.')
        self.page_obj = WeatherUIPage(self.driver)
        f = open('input_files/input.json', )
        self.input = json.load(f)
        print(self.input)

    def tearDown(self):
        test_method_name = self._testMethodName
        if self.result is not True:
            screen_shot.ScreenShot.capture_screen_shot(self.driver, test_method_name)
        t = float(time.time() - self.startTime)
        execution_time = self.util_obj.execution_time(t)
        print("<br/>\n", execution_time)
        create_log.create_log(
            self.id() + ' ' + 'completed. - ' + str(create_log.logic_for_pass_fail_error(self.result)))

    def test_001_comparator(self):
        city_list = self.input['City']
        for city in city_list:
            self.phase1_temp = self.page_obj.get_phase1_temperature(city)
            self.phase2_temp = self.page_obj.get_phase2_temperature(city)
            with self.subTest(i=city):
                self.assertEqual(self.phase1_temp, self.phase2_temp,
                                 msg=f'Phase1 temperature: {self.phase1_temp}, Phase2 temperature: {self.phase2_temp}')

    def test_002_temperature_variance(self):

        city_list = self.input['City']
        max_variance_percent = self.input['Variance']
        for city in city_list:
            self.phase1_temp = self.page_obj.get_phase1_temperature(city)
            self.phase2_temp = self.page_obj.get_phase2_temperature(city)
            with self.subTest(i=city):
                actual_variance = self.page_obj.verify_with_variance(self.phase1_temp, self.phase2_temp)
                self.assertLessEqual(actual_variance, max_variance_percent,
                                     msg=f'Phase1 temperature: {self.phase1_temp}, '
                                         f'Phase2 temperature: {self.phase2_temp}, '
                                         f'input_variance: {max_variance_percent}, '
                                         f'actual_variance: {actual_variance}.')
