import time
import logging
from selenium import webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


global web_driver

options = webdriver.ChromeOptions()
web_driver = webdriver.Chrome(options)


def get_an_element(xpath, timeout: int = 15):
    """Get an element with xpath.
    Args: xpath(str) - xpath need to locate.
        timeout (int) - Timeout setting for waiting the element.
    Return: element(obj)
    """
    elem = WebDriverWait(web_driver, timeout, 0.5).until(
        EC.presence_of_element_located((By.XPATH, xpath)),
        message="Element not exist",
    )
    return elem

def get_elements(xpath, timeout: int = 15):
    """Get elements with xpath.
    Args: xpath(str) - xpath need to locate
    Return: elements(obj list)
    """
    logging.info(f"elements = '{xpath}'")

    elems = WebDriverWait(web_driver, timeout).until(
        EC.presence_of_all_elements_located((By.XPATH, xpath)),
        message="Element not exist",
    )
    return elems

def input_element(xpath: str, text: str) -> None:
    """Input text to element with xpath.
    Args: xpath(str) - xpath need to locate and input
        text(str) - text need to input
    Return: N/A
    """
    elem = get_an_element(xpath, 15)
    elem.send_keys(text)

def click_element(xpath: str, timeout: int = 15) -> None:
    """Click element with xpath.
    Args: xpath(str) - xpath need to locate and click
    Return: N/A
    """
    elem = get_an_element(xpath, timeout)
    elem.click()

url = "https://typer.io/lobby"
web_driver.get(url)

# Wait for input player name manually
time.sleep(20)

xpath = "//*[@type='submit'][text()='Start Game']"
click_element(xpath)

xpath = "//h3[text()='GO!']"

get_an_element(xpath, 30)

xpath = "//*[contains(@class, 'Gameboard_container')]/*"
elems = get_elements(xpath)

xpath = "//*[@id='input']"

for _ in elems:
    string = _.text
    input_element(xpath, string)
    input_element(xpath, " ")

time.sleep(10)