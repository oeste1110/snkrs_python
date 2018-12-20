import time

import requests
from urllib.parse import urlencode
from requests.cookies import RequestsCookieJar
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import execjs

req_url = 'https://store.nike.com/cn/zh_cn/'
launch_url = 'https://www.nike.com/cn/launch/'
order_url = 'https://store.nike.com/cn/zh_cn/orders/'
login_url = 'https://unite.nike.com/login?'

def login_in():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images":2}
    options.add_experimental_option("prefs",prefs)
    #options.add_argument('headless')
    #options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)

    driver.get(req_url)
    try:
        WebDriverWait(driver,20,0.5).until(lambda x:x.find_element_by_xpath('//li[@js-hook="exp-join-login"]').is_displayed())
        #print(driver.current_url)
    except TimeoutException:
        print('超时')
    else:
        driver.find_element_by_xpath('//li[@js-hook="exp-join-login"]').click()
        driver.find_element_by_xpath('//div[@class="mobileNumber-div"]/input').send_keys("13126682752")
        driver.find_element_by_xpath('//form[@id="nike-unite-mobileLoginForm"]//div[contains(@class,"password")]/input').send_keys("Huang123")
        driver.find_element_by_xpath('//div[contains(@class,"mobileLoginSubmit")]').click()
        #if driver.find_element_by_xpath('//li[@class="js-listItem"]//a[@js-hook="logout"]'):
        #    print("登陆成功")
        time.sleep(10)
        driver.get("https://unite.nike.com/session.html")
        userInfo = driver.execute_script(
            "return localStorage.getItem('com.nike.commerce.nikedotcom.web.credential');")
        print(userInfo)
        #driver.get(order_url)
        #print(driver.current_url)
        #cookies = driver.get_cookies()
        #requests_cookies = {cookie['name']:cookie['value'] for cookie in cookies}
        #result = requests.get(req_url,cookies=requests_cookies)
        #result = requests.get(req_url)
        #print(result.url)
        #time.sleep(15)
    finally:
        driver.close()
        driver.quit()
    # 关闭浏览器
    #driver.close()
    # 关闭chreomedriver进程
    #driver.quit()

def test_login():
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)
    driver.get(order_url)
    time.sleep(5)
    print(driver.current_url)

def only_request():
    result = requests.get(order_url,allow_redirects=False)
    print(result.status_code)

def login_requests():
    options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    # options.add_argument('headless')
    # options.add_argument('window-size=1200x600')
    driver = webdriver.Chrome(options=options)

    driver.get(req_url)
    requests_cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}

    headers = {
            'Accept':'*/*',
            'Content-Type':'application/json',
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-us',
            'origin':'https://store.nike.com',
            'referer':'https://store.nike.com/cn/zh_cn/'
    }

    params = {
        'appVersion':525,
        'experienceVersion':423,
        'uxid':'com.nike.commerce.nikedotcom.web',
        'locale':'zh_CN',
        'backendEnvironment':'identity',
        'browser':'Google Inc.',
        'os':'undefined',
        'mobile':'false',
        'native':'false',
        'visit':1,
        'visitor':gen_visitorId()
    }

    post_data = {
        "username":"+8613126682752",
        "password":"Huang123",
        "client_id":"HlHa2Cje3ctlaOqnxvgZXNaAs7T9nAuH",
        "ux_id":"com.nike.commerce.nikedotcom.web",
        "grant_type":"password"
    }

    log_url = login_url + urlencode(params)
    #response = requests.post(log_url,data=post_data,headers=headers,cookies=requests_cookies)
    response1 = requests.options(log_url, headers=headers, cookies=requests_cookies)
    print(response1.status_code)
    response2 = requests.post(log_url, data=post_data, headers=headers, cookies=requests_cookies)
    print(response2.status_code)


def gen_visitorId():
    j = '''
                function e() {
                    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function(A) {
    					var z = Math.random() * 16 | 0,
    						y = A == "x" ? z : (z & 3 | 8);
    					return y.toString(16)
    				})
                }
            '''
    p = execjs.compile(j)
    return p.call('e')


if __name__ == '__main__':
    login_in()
    #only_request()
    #test_login()
    #print(gen_visitorId())
    #login_requests()