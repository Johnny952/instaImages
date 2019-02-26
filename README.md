# instaImages
Tool that automates the upload of images.
Implemented in python 3 using the Selenium module.
It is based on [chromemobiletest](https://gist.github.com/devinmancuso/ec8ae08fa73402e45bf1).

# Requirements
The following modules are needed to be able to run the code:
* Selenium
* PyautoIt

Besides this you need to download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) depending on the OS and the browser used and place it on the same folder as this script.
If you do not use chrome, then, in the nexts steps it will be shown how to modify it to use others browsers as Edge or Safari.

# Intallation
To install this modules use pip as follows:
```
pip install PyAutoIt
```
```
pip install selenium
```

# Before running
## Browser
First, you need to download the driver for selenium to use the browser, the links for the drivers are:
* [Chrome](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Edge](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)
* [Firefox](https://github.com/mozilla/geckodriver/releases)
* [Safari](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)

Once you download the driver, you need to place it in the same folder of the script and change line 87 'chromedriver' for the driver's name (E.g. 'gekodriver' for Firefox).
```
self.browser = webdriver.Chrome(executable_path='chromedriver',
```
## Language
If you use english browser, change the following lines:
In line 107 change "Ahora " for "Not now" and in line 108 "Cancelar" for "Cancel".
```
self.wait_limit(button="//*[contains(text(),'Ahora')]", limit=12, count=0)
self.wait_limit(button="//*[contains(text(),'Cancelar')]", limit=12, count=0)
```

In lines 115 and 106 change "Abrir" for "Open".
```
autoit.win_active("Abrir")
autoit.control_set_text("Abrir", "Edit1", path)
```

In line 136 change "Reintentar" for "Retry" and in line 141 "Ahora" for "Not now".
```
self.browser.find_element_by_xpath("//button[contains(text(),'Reintentar')]").click()
```
```
self.browser.find_element_by_xpath("//button[contains(text(),'Ahora')]").click()
```

In lines 152 and 160 change "Compartir" for "Share".
```
self.browser.find_element_by_xpath("//button[text()='Compartir']").click()
```

The line 118 press the button to resize the image, if it is not clicked then go to the page, right click on the button and Inspect, it will show something like the following:
```
<span class="Szr5J createSpriteExpand">Ampliar</span>
```
Copy the class name, "Szr5J createSpriteExpand" in this case and replace the name of the button "pHnkA" in line 118.
```
self.wait_limit(button="//button[@class='pHnkA']", limit=12, count=0)
```

# How to use it
The main method by default post every image on **images** folder in instagram, first it creates the object, put your email and password.
```
bot = PythonOrgSearchChrome(email='Your Email', password='Your Password')
```
Then, in setUp it opens the browser, then it log in.
The variable **script_path** is the path of the directory where is the script and is used then in the **post_every_image** to upload the images on **images** folder, this folder must only contain images **jpg**, *jpeg**, **png** among others (image fotmats supported by instagram).

# Comments
The module by default emulate the instagram of a BlackBerry Z30 that is what worked for me, but you can try others for more resolution commenting line 32 and uncommenting the line of the device of your preference.