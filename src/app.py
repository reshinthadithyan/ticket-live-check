import re
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import logging

from selenium.webdriver.remote.webelement import WebElement

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



class MoviePage:
    def __init__(self,url) -> None:
        self.driver = webdriver.Chrome()
        logger.info("Opening webdriver...")
        self.page = self.driver.get(url)
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
    def check_for_theatre(self,movie_name=None):
        """
        Function to check if a specific theatre is being opened inplace
        """
        theatre_list =  self.driver.find_element(By.ID, "venuelist").find_elements(By.TAG_NAME,"li")
        for theatre in theatre_list:
            theatre_name = theatre.find_element(By.CSS_SELECTOR,"data-name").text
            logger.info(f"Theatre List is {theatre_name.get_attribute('data-name')}")
        
    def __call__(self,theatre_name:str=None):

        theatre_flag = self.check_for_theatre(theatre_name)
        return theatre_flag


if __name__ =="__main__":
    test_url = "https://in.bookmyshow.com/buytickets/vikram-pondicherry/movie-pond-ET00138591-MT/20220603"
    reqd_page = MoviePage(test_url)
    reqd_page()
    reqd_page.driver.close()