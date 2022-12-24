from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
serv_obj=Service('C:\\Users\\saamim.hasmi\\Desktop\\Python_test_files\\Drivers\\chromedriver.exe')

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver = webdriver.Chrome(service=serv_obj)
        print("launching chrome")
    elif browser=='firefox':
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Chrome(service=serv_obj)

    return driver



def pytest_addoption(parser):
    parser.addoption("--browser")
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['module Name'] = 'customers'
    config._metadata['Tester'] = 'Saamim'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
