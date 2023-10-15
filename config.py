from selenium import webdriver

base_url = 'https://www.makemytrip.com/'

depart = 'Hydrabad'
arrive = 'Chennai'
departure_date = 'Fri Oct 20 2023'
secure = 'y'
covid = 'y'


def get_chrome_web_driver(options):
    return webdriver.Chrome('./chromedriver',chrome_options=options)


def get_web_driver_options():
    return webdriver.ChromeOptions()


def set_ignore_certificate_error(options):
    options.add_argument('--ignore-certificate-errors')
