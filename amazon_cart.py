# importing libraries
import pyautogui
import webbrowser
import time

cart_pos = 1615,1017
url="https://www.amazon.in/Apple-MacBook-Chip-13-inch-256GB/dp/B08N5XSG8Z/ref=sr_1_1_sspa?crid=S20LW5LUZLIX&keywords=macbook&qid=1650552159&sprefix=macbook%2Caps%2C204&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzRUJJMllJRUtFS0hYJmVuY3J5cHRlZElkPUEwNTcwOTA4MkU2Tk9ISENFT0FaSSZlbmNyeXB0ZWRBZElkPUEwNzA2NjQ2MzVaOFdZN0pKQ0hQMSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
webbrowser.open(url)
time.sleep(5)
pyautogui.click(cart_pos)