import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


driver = webdriver.Remote(
    command_executor='http://firefox:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX,
)

driver.get('http://app.{BASE_DOMAIN}/'.format(**os.environ))
WebDriverWait(driver, 10).until(EC.title_is('My App'))
assert 'My App' in driver.title

value = driver.find_element_by_id('name').get_attribute('value')
assert value == 'Your name...', value

print('All passed!')
