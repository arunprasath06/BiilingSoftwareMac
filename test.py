from subprocess import Popen
import os

def GetChromeLocation():
    chrome_path = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if os.path.exists(chrome_path):
        return chrome_path
    else:
        if os.path.exists('data/browser.cfg'):
            with open('data/browser.cfg','r') as f:
                location = f.readline().strip()
                if os.path.exists(location):
                    return location
                else:
                    notification_msg('Chrome Location Incorrect', 'Please set up the browser location in "data/browser.cfg".')
                    return False
        else:
            with open('data/browser.cfg','w') as f:
                f.write('')
            notification_msg('Chrome Not Found', 'Please set up the browser location in "data/browser.cfg".')
            return False

ch = GetChromeLocation()

if ch:
    print(ch == '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome')

    cmd = [
        ch,
        '--incognito',
        '--app=file:///Users/arumugamk/Documents/TECH REFERNCES/LuvorkBilling/data/outputs/invoice.html'
    ]

    Popen(cmd)
else:
    print("Chrome location not found or invalid.")
