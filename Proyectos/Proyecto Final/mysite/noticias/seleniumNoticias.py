import pandas as pd
import numpy as np
import selenium
import time
from selenium import webdriver

from bs4 import BeautifulSoup as bs4
import requests
from unidecode import unidecode
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class Twitter():
    def __init__(self, username, password):
        self.contenido = []
        self.password= password
        self.username = username
        self.browser = self.cargarNavegador()
        self.browser = self.login(self.browser, username, password)

        #print(self.obtenerContenidoUrl(url, self.browser), "\n")
        #print(self.obtenerCantidadTweets(self.browser, numbers_tweets))

    def cargarNavegador(self):
        options = webdriver.FirefoxOptions()
        options.add_argument('-headless')
        options.add_argument('-no-sandbox')
        options.add_argument('-disable-dev-shm-usage')
        driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
        return driver

    def login(self, driver, username, password):
        driver.get("https://twitter.com/login")
        time.sleep(2)
        driver.find_element_by_name("session[username_or_email]").send_keys(username)
        driver.find_element_by_name("session[password]").send_keys(password, Keys.ENTER)
        time.sleep(4)
        return driver

    def obtenerContenidoUrl(self, url):
        driver = self.browser.get(url)
        time.sleep(3)
        content = self.browser.find_element_by_xpath("//div[starts-with(@class,'css-901oao r-1fmj7o5 r-1qd0xha r-1blvdjr r-16dba41 r-vrz42v r-bcqeeo r-bnwqim')]")

        return content.text

    def obtenerCantidadTweets(self, numbers_tweets):
        # este metodo funcionara para obtener las noticias destacadas del tema
        self.browser.get("https://twitter.com/home")
        #driver = self.browser.get("https://twitter.com/search?q=economia&src=typed_query")
        tweets = []
        # tiempos de espera explicitos
        time.sleep(2)
        WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((By.XPATH, "//input[@data-testid='SearchBox_Search_Input']"))).send_keys("economía", Keys.ENTER)
        time.sleep(2)
        while True:
            if int(len(tweets)) >= numbers_tweets:
                break
            for div in self.browser.find_elements_by_xpath("//div[@data-testid='tweet']"):
                spans = div.find_elements_by_xpath(".//div/span")
                tweets.append(self.limpiezaTextoTweet(spans))
                if int(len(tweets)) >= numbers_tweets:
                    break
                else:
                    continue
            self.browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(3)
        return tweets

    def limpiezaTextoTweet(self, spans):
        tweets = '|'.join([span.text for span in spans])
        split = tweets.split('|')
        split.remove(split[-1])
        split.remove(split[-1])
        split.remove(split[-1])
        split.remove(split[0])
        split.remove(split[0])
        split.remove(split[0])
        return (''.join([i for i in split]))

