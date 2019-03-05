# Import time module to implement
import time

# Import the Selenium 2 module (aka "webdriver")
from selenium import webdriver

# For automating data input
from selenium.webdriver.common.keys import Keys

# For providing custom configurations for Chrome to run
from selenium.webdriver.chrome.options import Options
import autoit
import os
import selenium


# --------------------------------------
class PythonOrgSearchChrome:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    def setUp(self):
        # Select which device you want to emulate by uncommenting it
        # More information at: https://sites.google.com/a/chromium.org/chromedriver/mobile-emulation
        mobile_emulation = {
            # "deviceName": "Apple iPhone 3GS"
            # "deviceName": "Apple iPhone 4"
            # "deviceName": "Apple iPhone 5"
            # "deviceName": "Apple iPhone 6"
            # "deviceName": "Apple iPhone 6 Plus"
            # "deviceName": "BlackBerry Z10"
            "deviceName": "BlackBerry Z30"
            # "deviceName": "Google Nexus 4"
            # "deviceName": "Google Nexus 5"
            # "deviceName": "Google Nexus S"
            # "deviceName": "HTC Evo, Touch HD, Desire HD, Desire"
            # "deviceName": "HTC One X, EVO LTE"
            # "deviceName": "HTC Sensation, Evo 3D"
            # "deviceName": "LG Optimus 2X, Optimus 3D, Optimus Black"
            # "deviceName": "LG Optimus G"
            # "deviceName": "LG Optimus LTE, Optimus 4X HD"
            # "deviceName": "LG Optimus One"
            # "deviceName": "Motorola Defy, Droid, Droid X, Milestone"
            # "deviceName": "Motorola Droid 3, Droid 4, Droid Razr, Atrix 4G, Atrix 2"
            # "deviceName": "Motorola Droid Razr HD"
            # "deviceName": "Nokia C5, C6, C7, N97, N8, X7"
            # "deviceName": "Nokia Lumia 7X0, Lumia 8XX, Lumia 900, N800, N810, N900"
            # "deviceName": "Samsung Galaxy Note 3"
            # "deviceName": "Samsung Galaxy Note II"
            # "deviceName": "Samsung Galaxy Note"
            # "deviceName": "Samsung Galaxy S III, Galaxy Nexus"
            # "deviceName": "Samsung Galaxy S, S II, W"
            # "deviceName": "Samsung Galaxy S4"
            # "deviceName": "Sony Xperia S, Ion"
            # "deviceName": "Sony Xperia Sola, U"
            # "deviceName": "Sony Xperia Z, Z1"
            # "deviceName": "Amazon Kindle Fire HDX 7″"
            # "deviceName": "Amazon Kindle Fire HDX 8.9″"
            # "deviceName": "Amazon Kindle Fire (First Generation)"
            # "deviceName": "Apple iPad 1 / 2 / iPad Mini"
            # "deviceName": "Apple iPad 3 / 4"
            # "deviceName": "BlackBerry PlayBook"
            # "deviceName": "Google Nexus 10"
            # "deviceName": "Google Nexus 7 2"
            # "deviceName": "Google Nexus 7"
            # "deviceName": "Motorola Xoom, Xyboard"
            # "deviceName": "Samsung Galaxy Tab 7.7, 8.9, 10.1"
            # "deviceName": "Samsung Galaxy Tab"
            # "deviceName": "Notebook with touch"

            # Or specify a specific build using the following two arguments
            # "deviceMetrics": {"width": 900, "height": 900, "pixelRatio": 3.0},
            # "userAgent": "Mozilla/5.0"
        }

        # Define a variable to hold all the configurations we want
        chrome_options = webdriver.ChromeOptions()

        # Add the mobile emulation to the chrome options variable
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        # Create driver, pass it the path to the chromedriver file and the special configurations you want to run
        # If you don't use chrome, download the driver of your browser from the following links and place it on the folder of this script:
        # Edge: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
        # Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/
        # Firefox: https://github.com/mozilla/geckodriver/releases
        self.browser = webdriver.Chrome(executable_path='chromedriver',
                                       options=chrome_options)


    def tearDown(self):
        # Close the browser.
        # Note close() will close the current tab, if its the last tab it will close the browser. To close the browser entirely use quit()
        self.browser.close()


    def login(self):
        # Log into instagram's account
        self.browser.get('https://www.instagram.com/accounts/login/')
        emailInput = self.browser.find_elements_by_css_selector('form input')[0]
        passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
        emailInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(1)
        # Change "Ahora" and "Cancelar" for "Not now" and "Cancel"
        self.wait_limit(button="//*[contains(text(),'Ahora')]", limit=12, count=0)
        self.wait_limit(button="//*[contains(text(),'Cancelar')]", limit=12, count=0)

    def post_image(self, path):
        # Post an image inside the folder path on instagram
        self.browser.find_element_by_xpath("/html/body/span/section/nav/div/div/div/div/div/div[3]").click()
        time.sleep(1)
        # Change "Abrir" for "Open" and "Siguiente" for "Next"
        autoit.win_active("Abrir")
        autoit.control_set_text("Abrir", "Edit1", path)
        autoit.control_send("Abrir", "Edit1", "{ENTER}")
        self.wait_limit(button="//button[text()='Ampliar']", limit=12, count=0)
        self.wait_limit(button="//button[text()='Siguiente']", limit=30, count=0)
        self.compartir()
        self.reintentar()

    def wait_limit(self, button, limit, count):
        # Try to click a button until it appears or a count limit is reached
        if count < limit:
            try:
                self.browser.find_element_by_xpath(button).click()
            except Exception:
                time.sleep(1)
                self.wait_limit(button, limit, count + 1)

    def reintentar(self):
        # Try to click retry button, if the main screen appear, it clicks on "Not now" button
        # Change "Reintentar" and "Ahora" for "Retry" and "Not now"
        try:
            self.browser.find_element_by_xpath("//button[contains(text(),'Reintentar')]").click()
            time.sleep(0.5)
            self.reintentar()
        except Exception:
            try:
                self.browser.find_element_by_xpath("//button[contains(text(),'Ahora')]").click()
            except Exception:
                upload = self.browser.find_elements_by_xpath("/html/body/span/section/nav/div/div/div/div/div/div[3]")
                if len(upload) == 0:
                    time.sleep(0.5)
                    self.reintentar()

    def compartir(self):
        # Try to click "Share" button until it is clicked
        # Change "Compartir" for "Share"
        try:
            self.browser.find_element_by_xpath("//button[text()='Compartir']").click()
            self.compartir_clickeado()
        except Exception:
            time.sleep(1)
            self.compartir()
    def compartir_clickeado(self):
        # Try to click "Share" button until it desappears
        try:
            self.browser.find_element_by_xpath("//button[text()='Compartir']").click()
            time.sleep(1)
            self.compartir_clickeado()
        except Exception:
            pass

    def post_every_image(self, path):
        # Post every image on folder path
        if os.path.exists(path):
            images = get_images(path)
            for image in images:
                time.sleep(1)
                self.post_image(image)

def get_images(path):
    # Get the name of the files is the directory path
    files = os.listdir(path)
    full_path = [path + '\\' + f for f in files]
    return full_path

def main():
    # This is the main method, this will be executed when you run the script
    bot = PythonOrgSearchChrome(email='Your Email', password='Your Password')
    bot.setUp()
    print("Set up")
    bot.login()
    print("Logged in")
    script_path = os.path.dirname(os.path.realpath(__file__))
    print(script_path)
    bot.post_every_image(script_path + '\\images')
    bot.tearDown()

if __name__ == "__main__":
    main()
