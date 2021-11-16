from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from colorama import init
from colorama import Fore, Style
import os, sys, time, traceback, pickle, random, colorama, crayons


def clear():
    
    os.system("cls" if os.name == "nt" else "echo -e \\\\033c")
    os.system("mode con: cols=105 lines=30")
    os.system('title ' + 'Rewards Automation')
    

def logo():
    try:
        text = """                                   
           ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗    ██████╗  ██████╗ ████████╗
           ╚══██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝    ██╔══██╗██╔═══██╗╚══██╔══╝
              ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝     ██████╔╝██║   ██║   ██║   
              ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗     ██╔══██╗██║   ██║   ██║   
              ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗    ██████╔╝╚██████╔╝   ██║   
              ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝    ╚═════╝  ╚═════╝    ╚═╝   
                                                                            
                                                                             
                                                                             \n                    
        """
        bad_colors = ['LIGHTRED_EX', 'RED']
        codes = vars(colorama.Fore)
        colors = [codes[color] for color in codes if color in bad_colors]
        colored_chars = [random.choice(colors) + char for char in text]
        print(''.join(colored_chars))
        print(Fore.RESET + "\t\t\t               Coded by: xFijo#0999\n")

    except KeyboardInterrupt:
        sys.exit()

clear()
logo()

maxi = 0
start = '/@'
end = '/video/'
views = ' '

def countdown(t):
    
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

options = webdriver.ChromeOptions()
options.add_argument('window-size=1000,900')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
browser = webdriver.Chrome(options=options)
browser.minimize_window()
wait = WebDriverWait(browser, 2)

from selenium import webdriver
os.system('title ' + 'TikTok Bot Setup Mode.')

link = input('{}\n[>] {}TikTok Video Link ?: {}'.format(Fore.RESET, Fore.LIGHTCYAN_EX, Fore.RESET))
username = link[link.find(start)+len(start):link.rfind(end)]
os.system('title ' + f'Logged in as: {username} ')


browser.get('https://zefoy.com/')
print((crayons.cyan('You have 10 seconds to complete the captcha.')))
print((crayons.yellow('Once the captcha has been complete, please wait.')))
time.sleep(4)
browser.maximize_window()
time.sleep(10)
toggle = input(crayons.cyan('•Views\n•Followers\n•Shares\n•Likes\n[>] What would you like to bot ? : '))
if toggle == 'views':
    print(crayons.green('succesfully chosen to bot views.'))
    time.sleep(3)
    views = browser.find_element(By.XPATH,'//*[@id="main"]/div/div[4]/div/button').click()
    view_box = browser.find_element(By.XPATH, '//*[@id="sid4"]/div/form/div/input')
    view_box.send_keys(link)
    view_box.send_keys(Keys.RETURN)
    print((crayons.yellow('Please wait 90 seconds for the bot to register your video.')))
    search_button = browser.find_element(By.XPATH, '//*[@id="sid4"]/div/form/div/div/button').click()
    time.sleep(90)
    view_add_button = browser.find_element(By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9V"]/div[1]/div/form/button').click()
    print((crayons.green('ADDED: 1000 Views')))
    print(crayons.green('Automation Complete. Please restart the tool.'))
    pass
else:
    print(crayons.red('Not a valid botting option.'))
    sys.exit()
if toggle == 'shares':
    print(crayons.green('succesfully chosen to bot shares.')) 
    time.sleep(3)
    shares = browser.find.element(By.XPATH, '//*[@id="main"]/div/div[4]/div/button').click()
    shares_box = browser.find.element(By.XPATH, '//*[@id="sid7"]/div/form/div/input')
    shares_box.send_keys(link)
    shares_box.send_keys(Keys.RETURN)
    print(crayons.yellow('Please wait 90 seconds for the bot to register your video.'))
    share_add_button = browser.find_element(By.XPATH, '//*[@id="sid7"]/div/form/div/div/button').click()
    time.sleep(90)
    share_add_button = browser.find_element(By.XPATH, '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button').click()
    print(crayons.green('ADDED: 10 Shares'))
    print(crayons.green('Automation Complete. Please restart the tool.'))
    pass
elif toggle == 'followers':
    print(crayons.red('successfully chosen to bot followers.'))
    time.sleep(3)
    followers = browser.find_element(By.XPATH, '//*[@id="main"]/div/div[1]/div/button').click()
    
    sys.exit()
elif toggle == 'likes':
    print(crayons.red('Followers are currently not available. Please contact/wait for your supplier to send you the updated bot.'))
    sys.exit()
