from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import datetime

date = datetime.datetime.now().strftime("%m-%d-%Y")
time = datetime.datetime.now().strftime("%H:%M")

RECORD_TIME = "03:30:00"
MLB_ACCOUNT_USERNAME = "ajohman@gmail.com"
MLB_ACCOUNT_PASSWORD = "Josh123EU"
OUTPUT_FILE_PATH = "./games/redsox_{0}.mp3".format(date)

driver = webdriver.Chrome()

driver.get("https://securea.mlb.com/enterworkflow.do?flowId=registration.connect.wizard&c_id=mlb&template=mobile&forwardUrl=http://mlb.mlb.com/media/player/mpa/index.jsp")

print "INFO: Starting up... date is {0} and time {1}.".format(date, time)
print "INFO: Opening browser and logging in..."

# start the stream...
# first login to the mlb page
driver.find_element_by_id("emailAddress").send_keys(MLB_ACCOUNT_USERNAME)
driver.find_element_by_id("password-login").send_keys(MLB_ACCOUNT_PASSWORD)
driver.find_element_by_name("submitButton").click()

print "INFO: Successfully logged in."
print "INFO: Starting stream..."

BOS_XPATH = "//span[text()='WEEI']"

# then wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, BOS_XPATH)))

# and when it does click on the "WEEI" button
bos_elem = driver.find_element_by_xpath(BOS_XPATH)
bos_elem.click()

# ...next do the recording

# set the input and output devices to soundflower
os.system("audiodevice input \"Soundflower (2ch)\"")
os.system("audiodevice output \"Soundflower (2ch)\"")

print "INFO: Audio drivers set."
print "INFO: Beginning recording..."

# and start recording (pipe into mp3 using lame)
os.system("rec -c 2 -r 44100 -b 16 -e signed-integer -t raw - trim 0 {0} | lame -r -m s -s 44.1 - {1}".format(RECORD_TIME, OUTPUT_FILE_PATH))

print "INFO: Finished recording. File saved at \"./{0}\".".format(OUTPUT_FILE_PATH)
print "INFO: Cleaning up..."

# reset audio drivers
os.system("audiodevice input \"Internal Microphone\"")
os.system("audiodevice output \"Internal Speakers\"")

print "INFO: Completed."
