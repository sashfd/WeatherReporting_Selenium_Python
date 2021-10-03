class WeatherUILocators(object):
    location_search_input_xpath = "//input[@id='LocationSearch_input']"
    arrow_down_xpath = "//header/div[1]/div[2]/div[2]/button[1]/div[1]/*[2]"
    metric_unit_xpath = "//span[contains(text(),'°C')]"
    temperature_xpath = "//body/div[@id='appWrapper']/main[@id='MainContent']/div[2]/main[1]/div[1]/div[1]/section[" \
                        "1]/div[1]/div[2]/div[1]/span[1] "
