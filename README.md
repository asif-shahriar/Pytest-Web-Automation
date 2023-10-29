# Web automation using Pytest Selenium
## Prerequisites
* Install **Python** and **PyCharm** in your local device
* Clone the project 
* Open terminal in the root folder and run the following command:
```
pip install -r prerequisites.txt
```
* Copy the absloute path of [this json file](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/json_factory/registration.json "registration.json") and paste them in [Registration.py > registration_json_directory](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/testcases/Registration.py "Registration.py") and also in [Test Run 2.py > registration_directory](https://github.com/asif-shahriar/Pytest-Web_Automation/blob/master/runner/Test_Run2.py "Test_Run2.py"). The directory should look like this: **"D:\\\Your Folder name\\\json_factory\\\registration.json"**

## How to run this project
* Open terminal in the root folder
* Run the following set of commands:
```
python -m pytest runner -vv -s --alluredir=allure-results --clean-alluredir
```
```
allure serve allure-results
```
* **Optional:** If you want to run only the **smoke/regression** test cases, run either of the follwing set of commands:
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
## Allure Report Screenshot
![allure](https://github.com/asif-shahriar/Pytest-Web_Automation/assets/71173675/307defeb-3736-4e15-bcde-9a29852f8a41)


