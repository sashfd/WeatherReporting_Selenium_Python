from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import base64


class UtilMethods(object):
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.wait = WebDriverWait(self.driver, 30)

    def dropdown_visible_text(self, locator, text):
        # common method to select a value from the dropdown menu
        # Explicit waits halt the execution until 30 seconds or till the dropdown is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        select = Select(self.driver.find_element_by_xpath(locator))
        sleep(0.5)
        select.select_by_visible_text(text)

    def is_displayed(self, locator):
        # common method to verify if the element is displayed
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element_by_xpath(locator)
        # if the element is visible boolean TRUE is returned
        return element.is_displayed()

    def click(self, locator):
        # common method to click an element
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        # element is clicked
        self.driver.find_element_by_xpath(locator).click()

    def click_execute_script(self, locator):
        # common method to execute a click operation
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        # click even is executed using script method
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(locator))

    def send_keys(self, locator, value):
        # common method to send the text value to a variable
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        self.clear_text_field(locator)
        # Text value is sent to the element
        self.driver.find_element_by_xpath(locator).send_keys(value)

    def clear_text_field(self, locator):
        # common method to clear already existing value in a text field
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)

        self.driver.find_element_by_xpath(locator).clear()

    def get_text(self, locator):
        text = ""
        # common method to get a value from a element
        # Explicit waits halt the execution until 30 seconds or till the text element is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
            # text value is retrieved from the element
            text = self.driver.find_element_by_xpath(locator).text
        except TimeoutError:
            pass
        return text

    @staticmethod
    def execution_time(end_time):
        # Method to find the time taken for an Test case to execute
        # if end time is converted into minutes from seconds
        if end_time > 60:
            mins = int(end_time / 60)
            secs = end_time % 60
            return "Execution Time: " + str(mins) + "mins %.2f" % secs + 's'
        else:
            return "Execution Time: %.2f" % end_time + 's'

    def dropdown_first_select_text(self, locator):
        # Explicit waits halt the execution until 30 seconds or till the text element is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        # loading the dropdown element using xpath
        dropdown_element = self.driver.find_element_by_xpath(locator)
        # Using select function creating an object for the dropdown element
        dropdown_obj = Select(dropdown_element)
        # extracting text from the selected value in the dropdown object
        dropdown_text = dropdown_obj.first_selected_option.text
        # Returning the extracted text
        return dropdown_text

    def element_is_enabled(self, locator):
        # common method to verify if the element is enabled
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.visibility_of_element_located((By.XPATH, locator)))
        except Exception as e:
            print(e)
        sleep(0.5)
        element = self.driver.find_element_by_xpath(locator)
        # if the element is enabled boolean TRUE is returned
        return element.is_enabled()

    @staticmethod
    def decode_base64(string_to_decode):
        base64_bytes = string_to_decode.encode("ascii")
        sample_string_bytes = base64.b64decode(base64_bytes)
        decoded_value = sample_string_bytes.decode("ascii")
        return decoded_value

    def send_keys_without_clearing_field(self, locator, value):
        # common method to send the text value to a field without removing any existing data
        # Explicit waits halt the execution until 30 seconds or till the element is visible.
        try:
            self.wait.until(ec.element_to_be_clickable((By.XPATH, locator)))
        except Exception as e:
            print(e)
        # Text value is sent to the element
        self.driver.find_element_by_xpath(locator).send_keys(value)
