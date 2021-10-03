### **Weather Reporting**

This automation suite compares weather reporting done by 2 sources.

Source 1 : The website https://weather.com/

Source 2 : The public weather API by https://openweathermap.org/

**Python Version**: Python 3.7 or later

**How to Run**

To Run the execution, please follow below steps
1. Clone this repository
2. Create a virtual environment for the project
```
$ python -m venv venv
```
3. Activate the virtual environment as per your operating system
4. Install the requirements
```
(venv)<>$ pip install -r requirements.txt
```
5. Update the input json _WeatherReporting/input_files/input.json_ with the desired values for the comparison

    _example_:
```
{
   "City" : ["Delhi", "Chandigarh", "Indore", "Mumbai", "Kolkata", "New york", "Texas"],
   "Variance" : 4
}
```
6. Update the variable **app_id** at line 34 of the _C:\Projects\BlueStack_Proj\WeatherReporting\page_objects\pages\weather_ui_page.py_ with correct APPID value
```
if API Token is '123507e5732a4f5a4c407639a0d9d9b4'
app_id = '123507e5732a4f5a4c407639a0d9d9b4'
```
7. Start the execution using below command from the root folder
```
(venv)<>$ python test_runner.py
```
7. An Excel report will be generated post execution and placed can be found under _WeatherReporting/reports_ directory, results can be verified from 
the latest report
8. Screenshots will be captured in all cases (pass/fail) and can be found under _WeatherReporting/screen_shots_

_**Note**: No browser driver is required, but chrome is required to be installed as the execution will run on chrome browser._