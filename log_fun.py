
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import json
import requests

driver = webdriver.Chrome()

driver.maximize_window()
payload = {
        "email": "mykhailo.kovtun.work@gmail.com",
        "password": "Aa12345678",
        "token": "native-client-token"
    }

res = requests.post("https://api.singit.io/Users/Login", data=payload)

print(res.json())
driver.refresh()
driver.get("https://singit.io/explore")
time.sleep(2)
