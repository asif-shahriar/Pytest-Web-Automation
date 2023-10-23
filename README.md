# Web automation using Pytest Selenium
## Prerequisites
* Install **Python** and **PyCharm** in your local device
* Open terminal in the root folder and run the following command:
```
pip install -r prerequisites.txt
```
* Copy the absloute path of [this json file](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/json_factory/registration.json "registration.json") and paste them in [Registration class variable](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/testcases/Registration.py "Registration.py") and also in [Test Run 2 global variable](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/runner/Test_Run2.py "Test_Run2.py")

## How to run this project
* Open terminal in the root folder
* Give the following commands:
```
python -m pytest runner -vv -s --alluredir=allure-results --clean-alluredir
```
```
allure serve allure-results
```
* **Optional:** If you want to run only the **smoke/regression** test cases, give either of the follwing command:
```
python -m pytest -m smoke runner -vv -s --alluredir=allure-results --clean-alluredir
```
```
allure serve allure-results
```
* OR, 

```
python -m pytest -m regression runner -vv -s --alluredir=allure-results --clean-alluredir
```
```
allure serve allure-results
```
