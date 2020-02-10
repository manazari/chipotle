"""
                INSTRUCTIONS:
INPUT
there should be a 'input.txt' file in the same
folder as this python file

AS LONG AS there are 20 digits PER LINE in the input file,
the survey codes  can be seperated and read. The digits can be
seperated by '-' or ' ' or whatever. between the '###' is
an example of proper formatting for 'input.txt'
    ###
    031 002 100 082  010   561 94
    021- 002-100 -082- 010-531-14
    ###

CHROME DRIVER
you should change path_to_chromedriver_exe to where ever
it is on your pc
"""

__author__ = "Phuong Pham and Matthew Nazari"
__copyright__ = "Copyright 2020, The Coleman Minor Union"
__credits__ = ["Phuong Pham", "Matthew Nazari"]
__version__ = "1.1.0"
__email__ = ["phuong.pham01@sjsu.edu", "matthewnazari@harvard.edu"]

from selenium import webdriver
import time, re, random

path_to_chromedriver_exe = 'C:\Windows\chromedriver.exe'
input_path = 'input.txt'
feedback = []
try:
    with open('feedback.txt') as f:
        feedback = [line.rstrip() for line in f.readlines()]
except IOError:
    print('Cannot find "feedback.txt", will not input feedback')

driver = webdriver.Chrome(executable_path = path_to_chromedriver_exe)

class SurveyCode:
    """docstring for SurveyCode"""
    def __init__(self, code):
        super(SurveyCode, self).__init__()
        self.__code = self.__format_code(code)

    def __repr__(self):
        return self.__code

    def __str__(self):
        return '-'.join([self.__code[i:i+3] for i in range(0, len(self.__code), 3)])

    def __iter__(self):
        return iter(self.__repr__())

    def __format_code(self, code):
        code = re.sub('[^0-9]','', str(code))
        assert len(code) == 20, 'Survey code must be 20 digits!'
        return code

def complete_survey(code):
    def click_circle(xpath):
        circle = driver.find_element_by_xpath(xpath)
        circle.click()
    
    def click_next():
        next_button = driver.find_element_by_id('NextButton')
        next_button.click()

    driver.get('http://chipotlefeedback.com/')
    code = SurveyCode(code)

    # Please select the type of survey invite you recieved
    click_circle('/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div[1]/span/span')
    click_next()

    # 20-digit survey code
    for i, digit in enumerate(code):
        box = driver.find_element_by_id("CN{0}".format(1 + i//3))
        box.send_keys(digit)
    click_next()

    # Please answer the following questions about this Chipotle experience
    click_circle('/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span')
    click_next()

    # What type of experience did you have? How did you place your order? DINE-IN, IN-PERSON
    for i in range(1, 5):
        option_xpath  = '/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div[{0}]/'.format(i)
        if driver.find_element_by_xpath(option_xpath + 'label').get_attribute('innerHTML') == 'Carry-out':
            click_circle(option_xpath + 'span/span')
    for i in range(1, 6):
        option_xpath  = '/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div[{0}]/'.format(i)
        if driver.find_element_by_xpath(option_xpath + "label").get_attribute('innerHTML') == 'In-person':
            click_circle(option_xpath + 'span/span')
    click_next()

    # Which of the following did you order? OTHER
    click_circle('/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div[7]/span/span')
    click_next()

    # Based on your recent experience, please rate your satisfaction with the following
    for tr_number in range(2, 10):
        click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[{0}]/td[2]/span".format(tr_number))
        click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span")
    click_next()

    # Based on your recent experience, please rate your satisfaction with the following
    for tr_number in range(2, 5):
        click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[{0}]/td[2]/span".format(tr_number))
    click_next()
    
    # Did you have a problem during your experience? NO
    click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span")
    click_next()
    
    # Based on your experience, what is the likelihood that you will reccommend...
    for tr_number in range(2, 4):
        click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[{0}]/td[2]/span".format(tr_number))
    click_next()

    # Please tell us why you were Highly Satisfied
    driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[2]/form/div/div[1]/div[2]/div/div/textarea").send_keys(random.choice(feedback))
    click_next()
    time.sleep(0.500)

    # Describe the amount of food in your entree
    click_circle("/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div[2]/label")
    click_next()

    # Was the restaurant environment pleasant...
    for tr_number in range(2, 9):
        click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[{0}]/td[2]/span".format(tr_number))
    click_next()
    
    # Did you scan your Chipotle Rewards member QR code? YES
    click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[2]/span")
    click_next()
    
    # Please select your age
    click_circle("/html/body/div[1]/div[3]/div[2]/form/div/div[2]/div[2]/div/div[{0}]/label".format(random.randint(1, 5)))
    click_next()

    # Would you like to enter our sweepstakes?
    click_circle("/html/body/div[1]/div[3]/div[2]/form/div/table/tbody/tr[2]/td[3]/span")
    click_next()

surveys_completed = 0
with open(input_path) as f:
    for line in f:
        code = SurveyCode(line)
        print('> Completing survey with code "{0}"...'.format(code))
        complete_survey(code)
        surveys_completed += 1
        print('> Survey completed! ({0} total)\n'.format(surveys_completed))

print('END')