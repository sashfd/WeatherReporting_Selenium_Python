import unittest
from test_utility.HtmlTestRunner import HTMLTestRunner
from test_scripts import test_script_001_weather_comparison
from test_utility import create_log
import sys
import os

os.makedirs("logs/", exist_ok=True)

os.makedirs("screen_shots/", exist_ok=True)
os.makedirs("reports/", exist_ok=True)


class MyTestSuite(unittest.TestCase):
    @staticmethod
    def test_suite_1():
        weather_comparison_test_script = unittest.TestLoader().loadTestsFromTestCase(
            test_script_001_weather_comparison.TestWeatherComparator)

        suite1 = unittest.TestSuite([
            weather_comparison_test_script,
        ])

        runner = HTMLTestRunner(output='reports', report_title='Functional Test Cases Execution Report',
                                report_name="TestExecutionReport", verbosity=0, add_timestamp=True,
                                combine_reports=True, stream=sys.stdout)
        runner.run(suite1)


if __name__ == '__main__':
    create_log.initialize_log()
    unittest.main()
