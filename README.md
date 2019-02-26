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

Once you download the driver, you need to place it in the same folder of the script and change line 87 'chromedriver' for the driver's name.
```
self.browser = webdriver.Chrome(executable_path='chromedriver',
```