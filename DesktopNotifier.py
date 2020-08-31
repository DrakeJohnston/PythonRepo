import time
from win10toast import ToastNotifier
import keyboard
from googlesearch import search
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

toaster = ToastNotifier()
escaped = False
was_pressed = False

toaster.show_toast("Attention!", "Hello World!", icon_path=None, duration=5, threaded=True)

while not escaped:
    if not toaster.notification_active():
        time.sleep(10)

        query = "Computers"
        browser = webdriver.Chrome(executable_path=r'C:\Users\Jason\Desktop\chromedriver_win32\chromedriver.exe')
        browser.get('https://www.google.com/')

        elem = browser.find_element_by_name('q')
        elem.send_keys(query + Keys.RETURN)

        browser.quit()
        toaster.show_toast("Attention!", "Hello World!", icon_path=None, duration=5, threaded=True)
        # print('notified')

    if keyboard.is_pressed('q'):
        if not was_pressed:
            escaped = True
            # print(escaped)
            was_pressed = True
    else:
        was_pressed = False

while toaster.notification_active():
    time.sleep(0.1)
